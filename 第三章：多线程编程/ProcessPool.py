#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : ProcessPool.py
# @Author: akexiu
# @Date  : 2020/3/22
# @Desc  : 进程池

from multiprocessing import Pool
import os, time, random


def worker(msg):

    start = time.ctime()
    print("%s进程id：%s" % (msg,os.getpid()))
    time.sleep(random.random() * 2)
    stop = time.ctime()

    print('执行完毕%d' % msg)


def main():
    po = Pool(3)
    for i in range(0, 10):
        po.apply_async(worker, (i,))

    print("------start-----")
    po.close() #关闭进程池，不在接收信息
    po.join()  # 等待po所有进程执行完毕，必须放置在close之后
    print("-----end------")
if __name__ == "__main__":
    main()