#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : TcpCli.py
# @Author: akexiu
# @Date  : 2020/3/22
# @Desc  :
from socket import *
from time import ctime


def main():
    HOST = ''
    PORT = 21567
    BUFSIZE = 1024
    ADDR =(HOST,PORT)
    #创建服务器套接字
    tcpSock = socket(AF_INET6,SOCK_STREAM)
    # 套接字和端口绑定
    tcpSock.bind(ADDR)
    # 监听连接
    tcpSock.listen(5)

    while True:
        print("等待连接")
        cliSock,addr = tcpSock.accept()
        print("连接成功，地址为：",addr)
        while True:
            print("等待客户端发送消息")
            data = cliSock.recv(BUFSIZE)
            if not data:
                break
            print(data)
            cliSock.send(data)
        cliSock.close()



if __name__ =="__main__":
    main()