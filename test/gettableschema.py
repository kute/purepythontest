#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '2017/5/8 20:18'

"""

"""

import requests
import logging


logging.basicConfig(level=logging.DEBUG,
                    format='%(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='createtables.log',
                    filemode='a')


def main():
    # cookies = {
    #     "sessionid": "n6z6xckhssoyn96387d9kx1u8oizs71z"
    # }
    # url = "http://owl.hz.netease.com/netease/idb/query/db/"
    # with open('tables.txt', encoding='utf-8') as f:
    #     for line in f:
    #         body = dict(
    #             action="EXECUTE",
    #             useremail="longbai@corp.netease.com",
    #             sql="show create table {}".format(line.strip()),
    #             dbclutser=4585,
    #             dbtype="DDB",
    #             database="comment-mirror",
    #             serviceid=45
    #         )
    #         response = requests.post(url, data=body, cookies=cookies)
    #         if response.status_code == 200:
    #             # print(response.text)
    #             result = response.json()
    #             logging.info(result['result']['data'][0][1])
    kexue = 5.80042542002e+2
    print('%f' % kexue)


if __name__ == '__main__':
    main()
