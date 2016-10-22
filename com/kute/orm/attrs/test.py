#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: kute 
@ __file__: test.py
@ __mtime__: 2016/10/21 16:48


1. 以 _ 开头的私有成员 需要声明在 有 default 值的成员之前
2. 类初始化可以使用  位置参数 或者 关键字参数
3. init = False 表示不允许初始化

"""

import attr

# 设置是否在运行时验证
attr.set_run_validators(True)


@attr.s
class PersonList(object):
    persons = attr.ib()
    id = attr.ib()
    num = attr.ib()


def valid_name(instance, attribute, value):
    # instance: 当前实例
    # attribute: 当前的成员名
    # value: 当前成员对应的值
    return True


@attr.s
class Person(object):
    name = attr.ib(validator=valid_name)
    _salary = attr.ib(validator=attr.validators.instance_of(int))  # 验证当前类型为int
    age = attr.ib(default=18, convert=int)  # convert run before validator, 转换传参
    weight = attr.ib(default=200, init=False)

    @property
    def tall(self):
        return self.weight ** 2


@attr.s(these={"_x": attr.ib()})
class Square(object):
    @property
    def y(self):
        return self._x ** 2


def main():
    p = Person(name="kute", salary=1000, age=18)
    print(p)
    print(p.tall)
    print(attr.asdict(p))  # 字典转换
    print(attr.astuple(p))  # 元组
    print(attr.fields(Person))

    s = Square(5)
    print(s, s.y)

    personlist = PersonList(persons=[
        Person("kute", 1000, 18),
        Person("bai", 2000, 20),
        Person("yalong", 3000, 22)
    ], id="10086", num=76)
    result = attr.asdict(personlist, filter=filter_pro)  # 过滤方式1
    print(result)
    # 过滤 id 和 num成员,以及 值类型为 str 的值
    result = attr.asdict(personlist, filter=attr.filters.exclude(
        attr.fields(PersonList).id, str, attr.fields(PersonList).num
    ))
    print(result)

    # 创建一个类
    C = attr.make_class("C", ["x", "y"])
    B = attr.make_class("B", {
        "x": attr.ib(),
        "y": attr.ib()
    })
    c = C(x=1, y=2)
    b = B(2, 3)
    print(c, b)


def filter_pro(attr, value):
    # attr: 表示 PersonList中的每个成员
    # value: 表示 这个成员的值
    # print(attr)
    # print(value)
    return attr.name != "id" or value == 76  # 过滤成员名 为 id 的成员和值 为76的成员


if __name__ == "__main__":
    main()
