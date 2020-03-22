from socket import *

from past.builtins import raw_input


# 创建客户端
def main():
    HOST = 'localhost'
    PORT = 21567
    BUFSIZE = 1024
    ADDR = (HOST, PORT)
    #还有一种TCP方式发送，只需把AF_INET改成AF_INET6 SOCK_DGRAM，改成SOCK_STREAM即可
    udpCliSock = socket(AF_INET, SOCK_DGRAM)
    while True:
        data = raw_input('>')
        if not data:
            break
        # 发送信息
        udpCliSock.sendto(data.encode("utf-8"), ADDR)
        data, addr = udpCliSock.recvfrom(BUFSIZE)
        if not data:
            break
        print(data)
    # 关闭连接
    udpCliSock.close()


if __name__ == '__main__':
    main()
