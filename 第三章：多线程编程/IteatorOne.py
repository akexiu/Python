#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : IteatorOne.py
# @Author: akexiu
# @Date  : 2020/3/23
# @Desc  :迭代器
import time
from collections import Iterable
from collections import Iterator


class ClassMete(object):
    def __init__(self):
        self.names = list()
        #初始化数据，用于记录需要迭代的个数，
        self.current_num = 0;

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_num < len(self.names):
            ret = self.names[self.current_num]
            self.current_num += 1
            return ret
        else:
            raise StopIteration  ##抛出异常，终止迭代

    def add(self, name):
        self.names.append(name)


calssmate = ClassMete()
calssmate.add("张三")
calssmate.add("张三分")
calssmate.add("张三峰")

for name in calssmate:
    print(name)
    time.sleep(1)