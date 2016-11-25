#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '16/7/19 21:03'

import requests
from contextlib import closing
import time
import json
from com.kute.http.example.getcookiefrom163 import GetCookieFrom163Util


def posturl(docId):
    return "http://comment.news.163.com/api/v1/products/a2869674571f77b5a0867c3d71db5856/" \
           "threads/{}/comments?ibc=newspc&t={}".format(docId, time.time())


def tokenurl(docId):
    return "http://comment.news.163.com/api/v1/products/a2869674571f77b5a0867c3d71db5856/" \
           "threads/BPO97R58008535RB/comments/gentoken?ibc=newspc&t={}".format(docId, time.time())


def gettoken(docId, cookies):
    url = tokenurl(docId)
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
        "Referer": "http://comment.news.163.com/video_bbs/BPO97R58008535RB.html"
    }
    response = requests.post(url=url, headers=headers, cookies=cookies)
    if response and response.status_code == 200:
        resobj = json.loads(response.text, encoding="utf-8")
        if resobj:
            return resobj['gentoken']
    return None


def postcomment(docId, content, parentId, cookies, ntoken):
    url = posturl(docId)
    body = dict(
        board="news_bbs",
        content=content,
        parentId=parentId,
        ntoken=ntoken
    )

    cookies['WEB_TOKEN'] = ntoken
    print(cookies)
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
        "Referer": "http://comment.news.163.com/video_bbs/BPO97R58008535RB.html"
    }

    # 每次响应生成后调用
    hooks = dict(
        response=printInfo
    )

    try:
        with closing(requests.post(
            url=url,
            data=body,
            headers=headers,
            cookies=cookies,
            stream=True,  # 延迟下载response,直到访问res.content时才下载
            timeout=1000,
            hooks=hooks
        )) as res:
            print("over")
    except Exception as e:
        print(e.message)


def main():
    docId = "BPO97R58008535RB"
    content = "不知道今天行不行"
    parentId = 2569390807
    cookies = {
        "NTES_SESS": "T114ZH_6R80K.7VG4s2ltqM08Tow1P_CRLEmzo7L4JY7XQ9oyGH_5xc_f1yTRVn2CtwyUcq9dmyh108D.OxR3WxRqa"
                     "klnU2W4PJm7KrRuAEPsu5p0xHUKMVRdhjUdQ6XD8HkKgR8FJuOku55VFTZRrfPjtVQsLCQOSDsbZhec_kHOrOVLmogNl6x1"
    }

    ntoken = gettoken(docId, cookies)
    print(ntoken)
    if ntoken:
        postcomment(docId, content, parentId, cookies, ntoken)


def printInfo(res, *args, **kwargs):
    # print(res.url)
    print(res.status_code)
    print(res.text)
    # print(res.content)
    # print(res.headers)
    # print(res.cookies)
    # print(res.request.headers)


if __name__ == '__main__':
    main()
