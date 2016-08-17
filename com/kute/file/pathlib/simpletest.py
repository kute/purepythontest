#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '16/8/17 21:24'

"""

"""

from pathlib import Path


def main():
    path = Path(".")

    # 当前目录下的所有文件(或者目录)
    print([x.name for x in path.iterdir()])

    # resources 目录下的所有匹配文件
    print(list(path.glob("../resources/*.txt")))

    path = Path("/Users/kute/work/pycharmwork/purepythontest")

    # 定位到具体文件或者目录
    pathlibdir = path / "com" / "kute" / "file" / "pathlib"
    print(pathlibdir, pathlibdir.exists(), pathlibdir.is_dir())
    print([x for x in pathlibdir.iterdir()])

    # 定位到具体文件
    urlspath = path / "com" / "kute" / "file" / "resources" / "urls.txt"
    with urlspath.open() as f:
        print(f.readlines())


if __name__ == '__main__':
    main()
