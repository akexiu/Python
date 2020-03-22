#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : TcpCli.py
# @Author: akexiu
# @Date  : 2020/3/22
# @Desc  :
from socket import *

from past.builtins import raw_input


def main():
    HOST = 'localhost'
    PORT = 21567
    BUFSIZE = 1024
    ADDR =(HOST,PORT)
    #创建服务器套接字
    cliSock = socket(AF_INET6,SOCK_STREAM)
    # 套接字和端口绑定
    cliSock.connect(ADDR)
    while True:
        data = raw_input('>')
        if not data:
            break
        cliSock.send(data.encode("utf-8"))
        data=cliSock.recvfrom(BUFSIZE)
        if not data:
            break
        print(data)
    cliSock.close()

if __name__ == "__main__":
    main()