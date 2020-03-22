#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : threadTwo.py
# @Author: akexiu
# @Date  : 2020/3/22
# @Desc  :
import threading
import time

# 多线程恭喜变量  线程不安全
# 可以创建锁来解决 lock = threading.Lock()
g_num = 0
# 创建互斥锁，默认不上锁
lock = threading.Lock()


def test1(num):
    global g_num
    # 上锁
    lock.acquire()
    for i in range(num):
        g_num += 1
    print("test1:%d" % g_num)
    lock.release()  # 解锁


def test2(num):
    global g_num
    # 上锁
    lock.acquire()
    for i in range(num):
        g_num += 1
    print("test2:%d" % g_num)
    lock.release()  # 解锁


def main():
    threading.Thread(target=test1, args=(10000000,)).start()
    threading.Thread(target=test2, args=(10000000,)).start()


if __name__ == "__main__":
    main()
