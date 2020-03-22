#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : threadOne.py
# @Author: akexiu
# @Date  : 2020/3/22
# @Desc  :

import  time
import  threading

#唱歌
def sing():
   for i in range(5):
       print("正在唱【我是一只羊】")
       time.sleep(1)

#唱歌
def dance():
   for i in range(5):
       print("跳舞中")
       time.sleep(1)


def main():
     t1=threading.Thread(target=sing)
     t2=threading.Thread(target=dance)
     t1.start()
     t2.start()

     time.sleep(5)
     print(threading.enumerate())


if __name__ =='''__main__''':
    main()