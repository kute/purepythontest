#coding=utf-8
from lxml import etree
from io import StringIO, BytesIO


def main():
    # read local string
    xml = '<a xmlns="test"><b xmlns="arb">中文</b></a>'
    root = etree.fromstring(xml)
    print etree.tostring(root)

    root = etree.XML(xml)
    print etree.tostring(root)

    # read local string like file,并申明编码
    # about 'parse()' see: http://lxml.de/parsing.html
    root = etree.parse(StringIO(unicode(xml.decode(encoding="utf-8"))))
    print etree.tostring(root, encoding="utf-8", method="xml", pretty_print=True)

    # read file
    root = etree.parse("../../../xml/plant.xml")
    print etree.tostring(root)

if __name__ == '__main__':
    main()
