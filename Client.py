# 客户端原型，已弃用

import socket
import threading
import select
import time
host="192.168.2.153"
port=60000
from constant import *

def sender(s):
    while True:
        msg = input("input: ")
        print(msg)

        # 退出
        if msg == 'exit':
            s.close()
            break
        else:
            try:
                msg = s.recv(1024)
                msg = str(msg, encoding="utf-8")
                print(msg)
            except:
                print("程序出现错误，终止程序。")
                exit()
def receiver(s):
    input, _, _ = select.select([s], [], [])
    if input[0] is s:
        try:
            msg = s.recv(1024)
            msg = str(msg, encoding='utf-8')
            print(msg)
        except socket.error:
            print("该用户已经退出了聊天室。")
            exit()


def main():

    # 和服务器建立初始连接
    print('sdsad')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    print('sdsssad')
    # 将你的名字发送到服务器端
    name = input("input your name: ")
    s.send(bytes(name,encoding='utf-8'))

    # # 接受服务器的消息
    # fd = s.recv(1024)
    # fd = int(str(fd, encoding="utf-8"))

    # 建立双线程，一个线程发送消息，一个线程接受消息
    t_receive = threading.Thread(target=receiver, args=(s,))
    t_receive.start()
    t_send = threading.Thread(target=sender, args=(s,))
    t_send.start()




    # s.send(b"hello!%d" % (i))
    # data = s.recv(1024)
    # print(data, i)
    # time.sleep(10)
    # s.send(b"hello!%d" % (i))
    # data = s.recv(1024)
    # print(data, i)
    # time.sleep(10)


if __name__ == "__main__":
    main()


