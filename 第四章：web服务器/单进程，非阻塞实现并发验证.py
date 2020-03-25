#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 单进程，非阻塞实现并发验证.py
# @Author: akexiu
# @Date  : 2020/3/25
# @Desc  :

import socket
import time

# 创建套接字
socket_service = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_service.bind(('', 8888))
socket_service.listen(128)
# 设置套接字为非阻塞方式
socket_service.setblocking(False)

client_lists = list()

while True:
    time.sleep(1)
    try:
        new_socket, new_addr = socket_service.accept()
    except Exception as ret:
        print(ret)
        print("没有客户到来：")
    else:
        print("没有异常，证明有新客户到了")
        # 设置新的套接字为非阻塞方式
        new_socket.setblocking(False)
        client_lists.append(new_socket)

    for client_list in client_lists:
        try:
            recv_data = client_list.recv(1024)
            print(recv_data)
        except Exception as ret:
            print(ret)
            print("客户没有发来新信息：")
        else:
            if recv_data:
                print("客户发送了数据")
            else:
                client_list.close()
                client_lists.remove(client_list)
                print("关闭")
