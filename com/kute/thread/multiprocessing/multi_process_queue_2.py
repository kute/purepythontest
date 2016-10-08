#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: longbai 
@ __file__: multi_process_queue.py
@ __mtime__: 2016/10/8 13:06

开启多个进程 消费 同一个队列中的消息（注意 是 串行消费，数据被串行取出，但不一定是哪个进程消费）

map

"""

import multiprocessing
from kute.easylog.easylog import geteasylog

easylog = geteasylog()


# 每个进程启动之前执行
def before_start_process():
    print("Current start process: {}".format(multiprocessing.current_process().name))


def getdata(current_data):
    print("getdata from queue:data={}, processid={}".format(current_data, multiprocessing.current_process().name))
    return current_data


# 每个进程处理完结果返回进行回调
totallist = []
def process_callback(data):
    totallist.append(data)


def main():
    processcount = 5
    queuesize = 100
    poolsize = multiprocessing.cpu_count()  # 子进程个数，根据计算机配置
    try:
        # 构建共享数据队列并填充测试数据
        mylist = multiprocessing.Manager().list()
        for i in range(10, 20):
            mylist.append(i)

        # 开启进程池 消费 队列数据
        applylist = []
        with multiprocessing.Pool(processes=poolsize, initializer=before_start_process) as pool:
            mapresult = pool.map_async(func=getdata, iterable=mylist, callback=process_callback)
            applylist.append(mapresult.get())
            pool.close()
            pool.join()
        print("you have total callback data:{}".format(totallist))
        print("you have total apply data:{}".format(applylist))

    except Exception as e:
        easylog.error(e)


if __name__ == "__main__":
    main()
