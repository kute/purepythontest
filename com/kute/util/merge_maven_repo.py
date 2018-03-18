#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '2018/3/16 下午5:19'

"""
合并 maven 仓库
用 pyinstaller 打包为可执行程序

./merge_maven_repo -h

sage: merge_maven_repo [-h] [-l LEFT] [-r RIGHT]

This purpose is used to merge two maven repo into one by merge right repo into
left repo and will not override library which left already has. Finally the
right repo will be merged into left repo.

optional arguments:
  -h, --help            show this help message and exit
  -l LEFT, --left LEFT  the left repo dir, that is the dest repo
  -r RIGHT, --right RIGHT
                        the right repo dir, that is the src repo

"""

import os
import re
import shutil
import argparse


pattern = re.compile("\d+(\.*-*\d*\w*)*")


def filter_illegal(name):
    """
    filter dir-name which startwith "." or equals "unknown"
    :param name:
    :return:
    """
    return not name.startswith(".") and "unknown" == name


def merge(src, dest):
    """
    merge operation
    :param src:
    :param dest:
    :return:
    """
    check_empty(src, dest)

    difference, intersection = difference_and_intersection(src, dest)
    if difference:
        for sub in difference:
            print("src-dir[{}] ready copy to dest-dir[{}]".format(os.path.join(src, sub), os.path.join(dest, sub)))
            shutil.copytree(os.path.join(src, sub), os.path.join(dest, sub))
    if intersection:
        if not check_is_version(intersection[0]):
            for sub in intersection:
                merge(os.path.join(src, sub), os.path.join(dest, sub))


def check_is_version(sub):
    """
    check sub is the version dir
    :param sub:
    :return:
    """
    return re.fullmatch(pattern, sub)


def difference_and_intersection(src, dest):
    """
    get difference-dir and intersection-dir between src and dest
    :param src:
    :param dest:
    :return:
    """
    check_empty(src, dest)

    def do_get(sub):
        """
        get list dir by filter illegal
        :param sub:
        :return:
        """
        return list(filter(filter_illegal, os.listdir(sub)))
    src_dirs, dest_dirs = do_get(src), do_get(dest)
    return list(set(src_dirs).difference(set(dest_dirs))), list(set(src_dirs).intersection(set(dest_dirs)))


def check_empty(src, dest):
    """
    check dir empty
    :param src:
    :param dest:
    :return:
    """
    if not src or not dest:
        raise ValueError("src[{}] or dest[{}] must not be emtpy".format(src, dest))


def main():
    # src = "/Users/kute/work/logs/repo/repo2"
    # src = "/Users/kute/work/mvnrepo"
    # dest = "/Users/kute/work/logs/repo/repo1"
    # dest = "/Users/kute/.m2/repository"
    # merge(src, dest)
    parser = argparse.ArgumentParser(description="This purpose is used to merge two maven repo into one by merge "
                                                 "right repo into left repo and will not override library which left"
                                                 " already has. Finally the right repo will be merged into left repo.")

    parser.add_argument("-l", "--left",
                        help="the left repo dir, that is the dest repo",
                        type=str)
    parser.add_argument("-r", "--right",
                        help="the right repo dir, that is the src repo",
                        type=str)
    args = parser.parse_args()
    if args.left and args.right:
        merge(args.left, args.left)
    else:
        print("Please input repo")


if __name__ == '__main__':
    main()
