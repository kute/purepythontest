#!/usr/bin/env python
# coding=utf-8
import requests
import json

'''
  http://cn.python-requests.org/zh_CN/latest/user/quickstart.html
  http://cn.python-requests.org/zh_CN/latest/user/advanced.html
'''


def main():
    # get请求
    url = "https://github.com/timeline.json"
    getparams = {"a": "1", "b": 2}
    response = requests.get(url=url, params=getparams)
    print(response.content)
    print( response.text)
    print( response.encoding)
    print( response.json())
    print( response.url)
    print( response.status_code == requests.codes.ok)
    print( response.headers)
    print( response.headers['X-Request-Id'], response.headers.get('X-Request-Id'))
    # 使用响应对象的 history 方法来追踪重定向, 列表按照从最老到最近的请求进行排序
    print( response.history)

    # 将读取的大文本数据写入文件
    filename = "content.txt"
    with open(filename, "wb") as fd:
        for chunk in response.iter_content(100):
            fd.write(chunk)

    print("\n")

    # 添加header
    url = "https://api.github.com/some/endpoint"
    params = {'some': 'data'}
    headers = {'content-type': 'application/json'}
    response = requests.post(url, params, headers)

    # 表单文件(设置文件类型)
    files = {'file': ('report.xls', open('content.txt', 'rb'), 'multipart/form-data', {'Expires': '0'})}
    response = requests.post(url=url, files=files)

    # 发送文件类型为 multipart/form-data,以流的方式,参阅第三方包:requests-toolbelt: https://toolbelt.rtfd.org/


if __name__ == '__main__':
    main()
