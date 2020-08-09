# 该文件定义了客户端如何与服务端进行连接

import socket
import select
from constant import *
s = None
import time
import os

# 第一次连接
def first_connect(name):
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    # 和服务器建立第一次连接
    # 对服务器发送姓名
    s.send(bytes(name, encoding='utf-8'))


# 消息接收器
def receiver(signal):
    while True:
        inputs, _, _ = select.select([s], [], [])
        if inputs[0] is s:
            try:
                msg = s.recv(1024)
                msg = str(msg, encoding='utf-8')
                if len(msg.split(':')) > 1:
                    current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                    spk = msg.split(':')[0]
                    utt = msg.split(':')[1]
                    msg = spk + ' ' + current_time + '\n' + utt + '\n'
                    # 发射信号
                else:
                    msg += '\n'
                signal.emit(msg)
            except socket.error:
                print("服务端或您出现问题，终止程序。")
                os._exit(5)


# 消息发送器
def sender(msg):
    if msg == 'exit':
        s.close()
    else:
        try:
            s.send(bytes(msg, encoding='utf-8'))
        except socket.error:
            print("服务端或您出现问题，终止程序。")
            os._exit(5)


# 调试函数
def print_():
    global s
    print(s)
