#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : ProcessOne.py
# @Author: akexiu
# @Date  : 2020/3/22
# @Desc  :多任务进程


import time
import threading
import multiprocessing


# 唱歌
def sing():
    for i in range(5):
        print("正在唱【我是一只羊】")
        time.sleep(1)


# 唱歌
def dance():
    for i in range(5):
        print("跳舞中")
        time.sleep(1)


def main():
    # 多进程
    t1 = multiprocessing.Process(target=sing)
    t2 = multiprocessing.Process(target=dance)
    t1.start()
    t2.start()


if __name__ == '''__main__''':
    main()
