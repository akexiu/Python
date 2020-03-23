#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : gevent.py
# @Author: akexiu
# @Date  : 2020/3/23
# @Desc  : gevent 代替 yeild
import time

from setuptools import monkey

import gevent

monkey.patch_all()  ##将gevent中的耗时操作改为gevent自己的实现模块


def g():
    for i in range(10):
        print(gevent.getCurrent(), i)
        time.sleep(1)

        # gevent.sleep(1)


g1 = gevent.spawn(g)
g2 = gevent.spawn(g)
g3 = gevent.spawn(g)

g1.join()
g2.join()
g2.join()

gevent.joinall([
    gevent.spawn(g, 'w1'),
    gevent.spawn(g, 'w2')
])
