#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '16/8/6 11:48'

"""

"""

from whoosh.index import create_in
from whoosh.fields import *
from whoosh.qparser import QueryParser
from kute.caltime.caltime import perf_counter, process_time
import os
import sys


def create_index_dir(dirname):
    path = sys.path[0] + "/" + dirname
    if not os.path.exists(path):
        os.makedirs(path)
    return path


@process_time
def create_schema():
    return Schema(
        title=TEXT(stored=True),
        path=ID(stored=True),
        content=TEXT(stored=True)
    )


@process_time
def create_index(schema, indexdir):
    return create_in(dirname=indexdir, schema=schema)


@process_time
def create_writer(index, maxnumber):
    """
       add_document里的fidld可以比schema里的少,但不可以多
    """
    writer = index.writer(procs=1)
    for i in xrange(maxnumber):
        writer.add_document(
            title="document title-%s" % i,
            path="./path-%s" % i,
            content="content%s" % i
        )
    writer.add_document(title="index title", _stored_title="store title", content="content8")
    writer.commit()


@process_time
def search(ix):
    with ix.searcher() as searcher:
        query = QueryParser("content", ix.schema).parse("content8")
        results = searcher.search(query)
        print([r for r in results])


if __name__ == '__main__':
    schema = create_schema()
    index = create_index(schema, create_index_dir("indexdir"))

    create_writer(index, 10000)

    search(index)
