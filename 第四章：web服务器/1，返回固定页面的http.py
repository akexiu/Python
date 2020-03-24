#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 1，返回固定页面的http.py
# @Author: akexiu
# @Date  : 2020/3/24
# @Desc  :
# 1. os.getcwd()
# 获取文件当前工作目录路径
# 2. sys.path[0]
# 获取文件当前工作目录路径（绝对路径）
# sys.argv[0]|获得模块所在的路径（由系统决定是否是全名）
# 若显示调用python指令，如python demo.py，会得到绝对路径;
# 若直接执行脚本，如./demo.py，会得到相对路径。
#
# 3. __ file __
# 获得文件所在的路径（由系统决定是否是全名）
# 若显示执行Python，会得到绝对路径;
# 若按相对路径来直接执行脚本./pyws/path_demo.py，会得到相对路径。
#
# 4. os.path.abspath(__ file __)
# 获得文件所在的路径（绝对路径）
#
# 5. os.path.realpath(__ file __)
# 获得文件所在的路径（绝对路径）
#
# 6. os.path.split(os.path.realpath(__ file __))
# 将文件路径名称分成头和尾一对，生成二元元组。（文件目录，文件名）


import socket
import os
import re


def main():
    # 创建套接字
    tcp_service_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定端口
    tcp_service_socket.bind(("", 8888))
    # 设置监听
    tcp_service_socket.listen(128)
    # 等待客户端响应
    while True:
        new_socket, client_addr = tcp_service_socket.accept()
        client_service(new_socket)
        # 关闭套接字
    tcp_service_socket.close()


def client_service(new_socket):
    # 接收浏览器返回的数据
    request = new_socket.recv(1024).decode("utf-8")
    requestsplit = request.splitlines()
    print(requestsplit)
    ret = re.match(r'[^/]+(/[^ ]*)', requestsplit[0])
    if ret:
        file_name = ret.group(1)
        print("**********" + file_name)
    else:
        file_name = "/"
        file_name = os.getcwd() + "\html\index.html"
    # 发送给数据给浏览器
    response = "HTTP/1.1 200 OK\r\n"
    response += "\r\n"
    # response += "aaa"
    # 获取用户信息
    f = open(os.getcwd() + "\html\index.html", "rb")
    html_content = f.read()
    f.close()
    new_socket.send(response.encode("utf-8"))
    new_socket.send(html_content)
    new_socket.close()


if __name__ == "__main__":
    main()
