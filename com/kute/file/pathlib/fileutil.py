#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: longbai 
@ __file__: fileutil.py
@ __mtime__: 2016/8/18 18:31

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
        dirname = str(filetype)
        if dirname not in typedict:
            raise FileNotFoundError("filetype [{}] is wrong".format(filetype))
        if not filename:
            raise FileNotFoundError("filename [{}] is wrong".format(filename))
        if "." not in filename:
            filename = ".".join([filename, typedict[dirname]])
        basepath = Path(".").parent.parent.parent / "resources"
        dirpath = basepath / dirname
        if not dirpath.is_dir():
            raise FileNotFoundError("dir [{}] not found".format(dirpath))
        filepath = dirpath / filename
        if not filepath.is_file():
            raise FileNotFoundError("file [{}] not found".format(filepath))
        return filepath.absolute()


def main():
    print(FileUtil.getfilepath(FileUtil.PROPERTIES, "test.properties"))
    with open(file=FileUtil.getfilepath(FileUtil.PROPERTIES, "test.properties")) as f:
        print(f.readline())


if __name__ == "__main__":
    main()
