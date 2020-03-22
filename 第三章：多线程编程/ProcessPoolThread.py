#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : ProcessPoolThread.py
# @Author: akexiu
# @Date  : 2020/3/22
# @Desc  :
import multiprocessing
import os
from multiprocessing.dummy import Pool


def copyFile(q, file_Name, old_file_name, new_file_name):
    # print("文件%s，从到%s复制到%s" % (file_Name, old_file_name, new_file_name))
    # 读取老文件夹中需要copy的文件
    old_f = open(old_file_name + "/" + file_Name, "rb")
    connect = old_f.read()
    old_f.close()

    # 把文件夹下的文件写入
    new_f = open(new_file_name + "/" + file_Name, "wb")
    new_f.write(connect)
    new_f.close()
    # 添加到队列
    q.put(file_Name)


def main():
    pass
    # 1,获取需要copy的文件夹
    old_file_name = input("请输入文件:")
    # 2，创建新的文件夹
    try:
        new_file_name = old_file_name + "[copy]"
        os.mkdir(new_file_name)
    except:
        pass
    # 3，获取需要copy的文件名字
    file_names = os.listdir(old_file_name)

    # 4，创建进程池
    po = Pool(5)
    # ,5，创建队列
    q = multiprocessing.Manager().Queue()
    # ,6，向进程池中添加copy任务
    for file_Name in file_names:
        po.apply_async(copyFile, args=(q, file_Name, old_file_name, new_file_name))

    po.close()  # ,7关闭进程池，不在接收信息
    # po.join()  # 等待po所有进程执行完毕，必须放置在close之后
    file_num = len(file_names)
    copy_num = 0
    # 显示进度条
    while True:
        copy_num += 1;
        # end = "" 换行
        print("\r文件copy完成%s,进度%.2f %%" % (q.get(), (copy_num / file_num) * 100), end="")
        if copy_num >= file_num:
            break


if __name__ == '__main__':
    main()
