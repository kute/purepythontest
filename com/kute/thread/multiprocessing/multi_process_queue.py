#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: longbai 
@ __file__: multi_process_queue.py
@ __mtime__: 2016/10/8 13:06

开启多个进程 消费 同一个队列中的消息（注意 是 串行消费）

"""

import multiprocessing
from kute.easylog.easylog import geteasylog

easylog = geteasylog()


# 每个进程启动之前执行
def before_start_process():
    print("Current start process: {}".format(multiprocessing.current_process().name))


def getdata(myqueue):
    # data = myqueue.get(block=True)  # 布尔 标识 是否阻塞
    # data = myqueue.get(False)
    data = myqueue.get_nowait()  # 相当于  get(False)
    print("getdata from queue:data={}, processid={}".format(data, multiprocessing.current_process().name))
    return data + 1


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
        # myqueue = multiprocessing.Queue(maxsize=queuesize)  #  进程间不能使用此 Queue共享数据，应该用下面的Manager里的Queue
        myqueue = multiprocessing.Manager().Queue()
        for i in range(10, 20):
            myqueue.put(i, block=True)

        # 开启进程池 消费 队列数据
        applylist = []
        with multiprocessing.Pool(processes=poolsize, initializer=before_start_process) as pool:
            while not myqueue.empty():
                # 异步执行，快速返回，如果你调用applyresult.get() 则会一直等待进程处理完结果返回
                applyresult = pool.apply_async(func=getdata, args=(myqueue,), callback=process_callback)
                applylist.append(applyresult.get())
            pool.close()
            pool.join()
        print("you have total callback data:{}".format(totallist))
        print("you have total apply data:{}".format(applylist))

    except Exception as e:
        easylog.error(e)


if __name__ == "__main__":
    main()
