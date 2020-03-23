#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : greenletOne.py
# @Author: akexiu
# @Date  : 2020/3/23
# @Desc  : greenlet 可以替换 yield 实现多任务
from greenlet import greenlet
import time


def task_1():
    while True:
        print(1)
        t2.switch()
        time.sleep(1)


def task_2():
    while True:
        print(2)
        t1.switch()
        time.sleep(1)


t1 = greenlet(task_1)
t2 = greenlet(task_2)

t1.switch()
t2.switch()