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
from whoosh.index import EmptyIndexError
from kute.caltime.caltime import perf_counter, process_time
from kute.easylog.easylog import geteasylog
import os
import sys
import time
import datetime


easylog = geteasylog()


def create_index_dir(dirname):
    path = sys.path[0] + "/" + dirname
    if not os.path.exists(path):
        os.makedirs(path)
    return path


class MySchema(SchemaClass):
    url = ID(stored=True)
    docid = TEXT(stored=True)
    pdocid = TEXT
    useremail = TEXT(stored=True)
    posttime = DATETIME(stored=True, sortable=True)
    postid = TEXT(stored=True)
    ip = ID
    source = TEXT(stored=True)
    fpid = TEXT
    ppid = TEXT
    buildlevel = NUMERIC
    channelid = TEXT(stored=True)
    userc = ID
    usertype = TEXT


@process_time
def create_index(schema, indexdir):
    try:
        ix = open_dir(indexdir)
        return (ix, True)
    except EmptyIndexError as error:
        easylog.info("open failed, then created")
        return (create_in(dirname=indexdir, schema=schema), False)


@process_time
def create_writer(index, filepath):
    """
       从文件读取构建writer
    """
    writer = index.writer(procs=1)
    with open(filepath) as f:
        for line in f:
            t = tuple(line.split(","))
            if len(t) == 14:
                url, docid, pdocid, useremail, posttime, postid, ip, source, fpid, ppid, buildlevel, channelid, userc, usertype = t
                # print(url, docid, pdocid, useremail, posttime)
                writer.add_document(
                    url=url,
                    docid=docid,
                    pdocid=pdocid,
                    useremail=useremail,
                    posttime=datetime.datetime.strptime(posttime, '%Y-%m-%d %H:%M:%S'),
                    postid=postid,
                    ip=ip,
                    source=source,
                    fpid=fpid,
                    ppid=ppid,
                    buildlevel=int(buildlevel),
                    channelid=channelid,
                    userc=userc,
                    usertype=usertype
                )
            else:
                easylog.info(line)
    writer.commit()


if __name__ == '__main__':
    # 1. create schema
    schema = MySchema

    # 2. create index by schema
    index, hasindex = create_index(schema, create_index_dir("indexdir"))

    # 3. add document
    # easylog.info(hasindex)
    if not hasindex:
        easylog.info("not exist index and then created")
        filepath = os.path.join(os.path.dirname(__file__), "resources", "data.log")
        easylog.info(filepath)
        create_writer(index, filepath)

    # 4. search
    start = time.process_time()
    querystr = "BUJVD45B0521A11R_2559033966"
    with index.searcher() as searcher:
        query = QueryParser("postid", index.schema).parse(querystr)
        results = searcher.search(query)
        easylog.info([r for r in results])
        easylog.info("end time {}".format(time.process_time() - start))
