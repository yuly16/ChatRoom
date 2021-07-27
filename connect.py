# 该文件定义了客户端如何与服务端进行连接

import socket
import select
from constant import *
s = None
import time
import os

# 第一次连接
def first_connect(name, warning):
    global s
    try:
        print(host)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        # 和服务器建立第一次连接
        # 对服务器发送姓名
        s.send(bytes(name, encoding='utf-8'))
        return 0
    except socket.error:
        warning.emit("The server or you meets some error. The program ends.")
        return -1


# 消息接收器
def receiver(signal, warning, name):
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
                    if name == spk:
                        msg = '<font color=\'blue\'>' + 'Me（' + spk + '） ' + current_time + '</font>'
                    else:
                        msg = '<font color=\'green\'>'  + spk + ' ' + current_time + '</font>'
                    signal.emit(msg)
                    msg = utt + '\n'
                    signal.emit(msg)
                    # 发射信号
                else:
                    msg += '\n'
                    signal.emit(msg)
            except socket.error:
                warning.emit("The server or you meets some error. The program ends.")


# 消息发送器
def sender(msg, warning):
    if msg == 'exit':
        s.close()
    else:
        try:
            s.send(bytes(msg, encoding='utf-8'))
        except socket.error:
            warning.emit("The server or you meets some error. The program ends.")


# 调试函数
def print_():
    global s
    print(s)
