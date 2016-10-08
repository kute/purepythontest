#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '16/9/7 21:15'

"""

模拟微博登陆

https://github.com/yoyzhou/weibo_login/blob/master/weibo_login.py

"""

import requests
import base64
import time
import datetime
import json
import rsa
import binascii
from kute.easylog.easylog import geteasylog


easylog = geteasylog()


class WeiBoLogin(object):
    """
    模拟微博登陆
    """
    def __init__(self, username, userpwd):
        self.username = username
        self.encodeusername = self._base64encode(orginstr=self.username)
        self.userpwd = userpwd

        self.servertime = ""
        self.pcid = ""
        self.rsakv = ""
        self.nonce = ""
        self.smsurl = ""
        self.pubkey = ""


    def prelogin_request(self):
        """
        call before login_request
        """
        preloginurl = self._pre_login_url()
        response = requests.get(preloginurl)
        # easylog.info(response.text)
        if response.status_code == 200:
            resjson = json.loads(response.text, encoding="utf-8")
            self.servertime = resjson["servertime"]
            self.pcid = resjson["pcid"]
            self.rsakv = resjson["rsakv"]
            self.nonce = resjson["nonce"]
            self.pubkey = resjson["pubkey"]
            if "smsurl" in resjson:
                self.smsurl = resjson["smsurl"]
            return self
        else:
            raise Exception

    def login_request(self):
        params = self._build_login_param()
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:47.0) Gecko/20100101 Firefox/47.0"
        }
        try:
            response = requests.post(
                url=self._login_url(),
                headers=headers,
                data=params
            )
            if response.status_code == 200:
                easylog.info(response.text)
            else:
                raise Exception
        except Exception as e:
            easylog.error(e)

    def _get_pwd(self):
        rsaPublickey = int(self.pubkey, 16)
        key = rsa.PublicKey(rsaPublickey, 65537)
        message = str(self.servertime) + '\t' + str(self.nonce) + '\n' + str(self.userpwd)
        passwd = rsa.encrypt(message.encode("utf-8"), key)
        # binascii module please download https://pypi.python.org/pypi/micropython-binascii/2.4.0-3 and install
        passwd = binascii.b2a_hex(passwd)
        return passwd.decode("utf-8")

    def _build_login_param(self):
        """
        构建login参数
        """
        self.prelogin_request()
        return {
            "encoding": "utf-8",
            "entry": "weibo",
            "from": "",
            "gateway": "1",
            "nonce": self.nonce,
            "pagerefer": "http://login.sina.com.cn/sso/logout.php?entry=iniblog&r=ttp%3A%2F%2Fwe""ibo.com%2Flogout.php%3Fbackurl%3D%252F",
            "prelt": "47",
            "pwencode": "rsa2",         # 密码加密算法
            "returntype": "META",
            "rsakv": self.rsakv,
            "savestate": "7",
            "servertime": self.servertime,
            "service": "miniblog",
            "sp": self._get_pwd(),                    # 加密密码
            "sr": "1280*800",
            "su": self.encodeusername,   # base64加密用户名
            "url": self._ajax_login_url(),
            "useticket": "1",
            "vsnf": "1",
            "door": ""    # 验证码
        }

    def _base64encode(self, orginstr, encoding="utf-8"):
        """
        对用户名base64编码
        """
        return base64.b64encode(orginstr.encode(encoding="utf-8")).decode("utf-8")

    def _ajax_login_url(self):
        return "http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack"

    def _login_url(self):
        return "http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.18)"

    def _pre_login_url(self):
        return "https://login.sina.com.cn/sso/prelogin.php?entry=weibo&su={}&rsakt=mod&client=" \
               "ssologin.js(v1.4.18)&_={}".format(self.encodeusername, time.mktime(datetime.datetime.now().timetuple()))


def main():
    login = WeiBoLogin("18311441603", "bailong")
    # print(login.prelogin_request().__dict__)
    print(login.login_request())


if __name__ == '__main__':
    main()
