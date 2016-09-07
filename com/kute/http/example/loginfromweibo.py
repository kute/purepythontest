#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '16/9/7 21:15'

"""

模拟微博登陆

"""

import requests
import base64
import time
import datetime
import json
from kute.easylog.easylog import geteasylog


easylog = geteasylog()


class WeiBoLogin(object):
    """
    模拟微博登陆
    """
    def __init__(self, username, userpwd):
        self.username = username
        self.encodeusername = self._base64encode()
        self.userpwd = userpwd

        self.servertime = ""
        self.pcid = ""
        self.rsakv = ""
        self.nonce = ""
        self.smsurl = ""

    def prelogin_request(self):
        preloginurl = self._pre_login_url()
        response = requests.get(preloginurl)
        easylog.info(response.text)
        if response.status_code == 200:
            resjson = json.loads(response.text, encoding="utf-8")
            self.servertime = resjson["servertime"]
            self.pcid = resjson["pcid"]
            self.rsakv = resjson["rsakv"]
            self.nonce = resjson["nonce"]
            if "smsurl" in resjson:
                self.smsurl = resjson["smsurl"]
            return self
        else:
            raise Exception


    def _base64encode(self, encoding="utf-8"):
        """
        对用户名base64编码
        """
        return base64.b64encode(self.username.encode(encoding="utf-8")).decode("utf-8")

    def _pre_login_url(self):
        return "https://login.sina.com.cn/sso/prelogin.php?entry=weibo&su={}&rsakt=mod&client=" \
               "ssologin.js(v1.4.18)&_={}".format(self.encodeusername, time.mktime(datetime.datetime.now().timetuple()))


def main():
    login = WeiBoLogin("xxxx", "xxx")
    print(login.prelogin_request().__dict__)


if __name__ == '__main__':
    main()
