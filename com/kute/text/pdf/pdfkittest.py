#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: longbai 
@ __file__: pdfkittest.py
@ __mtime__: 2016/6/4 12:27

"""

import pdfkit


def main():
    try:
        url = 'https://github.com/JazzCore/python-pdfkit'
        headers = {
            '--header-line': 'this is a head line',
            '--load-error-handling': 'ignore',
            '--header-left': 'header left text====='
        }
        config = pdfkit.configuration(wkhtmltopdf='D:/softers/wkhtmltopdf/bin/wkhtmltopdf.exe')
        pdfkit.from_url(url=[url],
                        output_path='./pdfkit2.pdf',
                        configuration=config, options=headers)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
