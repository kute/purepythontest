#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: kute 
@ __file__: task_example.py
@ __mtime__: 2017/8/23 19:30

三个任务共需要4s时间，任务1在1s后继续执行，任务2类似

使用

"""

import asyncio
import aiohttp
import requests

import time

now = lambda: time.time()
loop = asyncio.get_event_loop()

async def get_response(url):
    async with requests.get(url) as response:
        assert response.status == 200
        return await response.text

async def do_some_work(item):

    url = "https://www.reddit.com/r/{}/top.json?sort=top&t=day&limit=5".format(item)

    result = await get_response(url)
    print(result)

start = now()

items = ['nbs', 'funny', 'soccer']
tasks = [asyncio.ensure_future(do_some_work(item)) for item in items]


loop.run_until_complete(asyncio.wait(tasks))
loop.close()

print('TIME: ', now() - start)


def main():
    print("hello")


if __name__ == "__main__":
    main()
