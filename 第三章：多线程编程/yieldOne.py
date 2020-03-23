#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : yieldOne.py
# @Author: akexiu
# @Date  : 2020/3/23
# @Desc  : yield 生成器   生成器是一种特殊的迭代器
import time


def create_num(num):
    a, b = 0, 1
    current_num = 0
    while current_num < num:
        # 如果函数中有yield 那么这个函数就是生成器的模板
        ret = yield a
        print("yield:", ret)
        a, b = b, a + b
        current_num += 1
    return 'aaa'  # 如果yield 生成器有返回值，需要取异常信息中获取


# 如果函数中有yeild 那么就是创建一个生成器对象
obj = create_num(10)

# 第一种方式
# for o in obj:
# #     print(o)
# while True:
#     try:
#         ret = next(obj)
#         print(ret)
#     except Exception  as ret:
#         print(ret.value)  # 获取返回值
#         break

# 通过send启动生成器，第二中方式
ret = next(obj)  # 必须先调用next 或者send 传None
ret = obj.send('hello')  # 用于传值给yeild


# while True:
#     try:
#         ret = obj.send("hello")#用于传值给yeild
#         print("\t 第二种启动方式：", ret)
#     except Exception  as ret:
#         print(ret.value)  # 获取返回值
#         break


# yield 实现多任务

def task_1():
    while True:
        print(1)
        time.sleep(1)
        yield


def task_2():
    while True:
        print(2)
        time.sleep(1)
        yield


def main():
    t1 = task_1()
    t2 = task_2()
    while True:
        next(t1)
        next(t2)


if __name__ == '__main__':
    main()
