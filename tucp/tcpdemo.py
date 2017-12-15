#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu
 
@file: tcpdemo.py
 
@time: 2017/12/15 9:30
 
@desc:
 
'''
import socket
import threading
import time


#  tcp 三次握手 可靠  稍慢
# udp 快 不可靠


def dealClient(sock, addr):
    print("接受来自%s:%s.." % addr)

    sock.send("hello,i am a server")

    while True:
        data = sock.recv(1024)
        time.sleep(1)

        if not data or data.decode('utf-8') == 'exit':
            print('-->>%s' % data.decode('utf-8')).encode('utf-8')
    sock.close()
    print('from %s:%s connection' % addr)


if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 8888))

    s.listen(5)
    print('等待连接')

    while True:
        sock, addr = s.accept()
        t = threading.Thread(target=dealClient, args=(sock, addr))
        t.start()
