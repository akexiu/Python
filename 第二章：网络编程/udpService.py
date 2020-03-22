


#创建套接字，使用socket 模块函数，语法：socket(socket_family,socket_type,prtocol=0)
from socket import *
from time import ctime

#创建服务端
def main():
    HOST = ''
    PORT = 21567
    BUFSIZE = 1024
    ADDR =(HOST,PORT)
    # 创建一个udp套接字
    udpSock = socket(AF_INET, SOCK_DGRAM);
    #绑定ip
    udpSock.bind(ADDR)
    # 使用套接字收发数据
    while True:
        print("开始等待信息")
        # 等待接收发送的数据 BUFSIZE表示最大的接收字节数
        data,addr=udpSock.recvfrom(BUFSIZE)
        udpSock.sendto(data,addr)
        print("返回地址:",addr,data)
    udpSock.close()

if __name__ == '__main__':
    main()
