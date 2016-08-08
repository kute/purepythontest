#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '16/8/6 11:48'

"""

入门例子

"""

from whoosh.index import create_in, open_dir
from whoosh.fields import *
from whoosh.qparser import QueryParser
from kute.caltime.caltime import perf_counter, process_time
import random
import logging
import os
import sys


def create_index_dir(dirname):
    path = sys.path[0] + "/" + dirname
    if not os.path.exists(path):
        os.makedirs(path)
    return path


class MySchema(SchemaClass):
    """
        schema创建的第二种方式
    """
    title = TEXT(stored=True)
    path = ID(stored=True)
    content = TEXT(stored=True)


@process_time
def create_schema():
    """随机使用两种创建schema的方式"""
    if random.randint(0, 1):
        return Schema(
            title=TEXT(stored=True),
            path=ID(stored=True),
            content=TEXT(stored=True)
        )
    return MySchema


@process_time
def create_index(schema, indexdir):
    ix = open_dir(indexdir)
    if not ix:
        logging.info("open failed, then created")
        ix = create_in(dirname=indexdir, schema=schema)
    return ix


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
    # writer.add_document(title="index title", _stored_title="store title", content="content8")
    writer.commit()


@process_time
def search(ix, qstr):
    """

    parser.parse(u"render shade animate")  <=> And([Term("content", "render"), Term("content", "shade"), Term("content", "animate")])
    parser.parse(u"render OR (title:shade keyword:animate)")  <=>  Or([Term("content", "render"), And([Term("title", "shade"), Term("keyword", "animate")])])
    parser.parse(u"rend*")  <=>  Prefix("content", "rend")

    """
    with ix.searcher() as searcher:
        query = QueryParser("content", ix.schema).parse(qstr)
        results = searcher.search(query)
        print([r for r in results])


if __name__ == '__main__':
    # 1. create schema
    schema = create_schema()

    # 2. create index by schema
    index = create_index(schema, create_index_dir("indexdir"))

    # 3. add document
    create_writer(index, 10000)

    # 4. search
    querystr = "content8"
    search(index, querystr)
