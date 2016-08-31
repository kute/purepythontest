#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '16/8/30 20:37'

"""
正则匹配
"""

import requests
import re
from kute.easylog.easylog import geteasylog


easylog = geteasylog()


class GetCookieFrom163Util(object):
    """测试模拟登陆163.com并取得登陆后的cookie"""

    loginurl = "https://reg.163.com/logins.jsp"

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def _dologin(self):
        try:
            post_data = dict(
                username=self.username,
                password=self.password,
                product="content",
                savelogin=1,
                url="http://comment.api.163.com/api/v1/products/a2869674571f77b5a0867c3d71db5856/users/checklogin?"
                    "url=http://comment.news.163.com/video_bbs/BPO97R58008535RB.html&ibc=newspc"
            )
            response = requests.post(url=self.loginurl, data=post_data)
            return response.text.replace("\n", "")
        except Exception as e:
            easylog.error("wrong")
        return None

    @property
    def cookie(self):
        res = self._dologin()
        if res:
            reg = r'http://reg\.youdao\.com/crossdomain\.jsp\?username=' + self.username + '&loginCookie=(.*)&persistCookie'
            text = re.search(reg, res).group(0)
            return text[text.index("loginCookie=") + 12:text.index("&persistCookie")]
        return None


def main():
    util = GetCookieFrom163Util("xxxxx@qq.com", "xxxxxx")
    print(util.cookie)


if __name__ == '__main__':
    main()
