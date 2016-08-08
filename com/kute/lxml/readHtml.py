#coding=utf-8
from lxml import etree
from io import StringIO, BytesIO


def main():
    # read local html
    broken_html = "<html><head><title>test<body><h1>page title</h3>"
    parser = etree.HTMLParser(encoding="utf-8")
    document = etree.parse(StringIO(unicode(broken_html)), parser)
    print etree.tostring(document, pretty_print=True, method="html")

    document = etree.HTML(unicode(broken_html), parser)
    print etree.tostring(document, pretty_print=True, method="html")

    # read html url
    document = etree.parse("http://lxml.de/parsing.html", parser)
    print etree.tostring(document, pretty_print=True, method="html")

if __name__ == '__main__':
    main()
