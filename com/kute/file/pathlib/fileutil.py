#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: longbai 
@ __file__: fileutil.py
@ __mtime__: 2016/8/18 18:31

获取 resources目录下的文件,只需引入即可
@see com.kute.file.imghdr.detect_imgage_type.py

"""

from pathlib import Path


typedict = {
    "XML": "xml",
    "TEXT": "txt",
    "PROPERTIES": "properties",
    "IMAGE": "jpg"
}


class FileUtil(object):
    XML = "XML"
    TEXT = "TEXT"
    PROPERTIES = "PROPERTIES"
    IMAGE = "IMAGE"

    @staticmethod
    def getfilepath(filetype=TEXT, filename=None):
        if filetype not in typedict:
            raise FileNotFoundError("filetype [{}] is wrong".format(filetype))
        dirname = str(filetype).lower()
        if not filename:
            raise FileNotFoundError("filename [{}] is wrong".format(filename))
        if "." not in filename:
            filename = ".".join([filename, typedict[filetype]])
        #  定位到resources目录
        _resources_dir = Path(__file__).parent.parent.parent.parent.parent / "resources"
        filedir = _resources_dir / dirname
        if not filedir.is_dir():
            raise FileNotFoundError("dir [{}] not found".format(dirpath))
        filepath = filedir / filename
        if not filepath.is_file():
            raise FileNotFoundError("file [{}] not found".format(filepath))
        return str(filepath)


def main():
    filepath = FileUtil.getfilepath(FileUtil.PROPERTIES, "test.properties")
    # print(filepath)
    with open(file=filepath) as f:
        print(f.readline())
    # path = Path(__file__)
    # print(path.parent.parent.parent.parent.parent / "resources")


if __name__ == "__main__":
    main()
