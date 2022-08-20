# 装饰器

- [语法说明](#语法说明)
- [注册装饰器](#注册装饰器)
- [参数化装饰器](#参数化装饰器)
- [结尾](#结尾)

## 语法说明

装饰器是Python的一种特性比如，调用装饰器`func_zs`装饰`func`语法如下：

```python
@func_zs
def func():
    """
    Code
    """
    pass
```

相当于

```python
def func():
    """
    Code
    """
    pass

func_zs(func())
```

## 注册装饰器
我们将使用注册装饰器做个简单的计时器

```python
from time import time # 记录时间

def func_pref():
    def clock(func):
        # 装饰器一般都要嵌套
        # 装饰器主体
        t1 = time()
        # 运行被装饰函数
        func()
        t2 = time()
        print('函数{},运行所使用时间为{}'.format(func.__name__, t2 - t1))
        return func # 必须返回,否则会被覆盖
    return clock

@func_pref
def mul():
    print('10000 * 3810的结果是{}'.format(10000 * 3810))
```

以上代码作者没实际运行过，不过效果大概如下
```sh
~ $ python test.py
10000 * 3810的结果是38100000
函数mul，运行所使用时间为XXX
```
由此可见，注册装饰器会将函数作为参数

## 参数化装饰器
参数化装饰器在调用装饰器的过程中，必须要传参，这是之前实例的改进版

```python
from time import time # 记录时间

def func_pref(fmt_str="函数{},运行所使用时间为{}"):
    def clock(func):
        # 装饰器一般都要嵌套
        # 装饰器主体
        t1 = time()
        # 运行被装饰函数
        func()
        t2 = time()
        print(fmt_str.format(func.__name__, t2 - t1))
        return func # 必须返回,否则会被覆盖
    return clock

@func_pref() # 必须要加括号，因为是参数化装饰器
def mul():
    print('10000 * 3810的结果是{}'.format(10000 * 3810))

@func_pref(fmt_str="Function {}, func_time {}")
def add():
    print('54188 + 20结果是{}'.format(54188 + 20))
```

运行结果（模拟的）
```sh
~ $ python test.py
10000 * 3810的结果是38100000
函数mul，运行所使用时间为XXX
54188 + 20结果是54208
Function add, func_time XXX
```

## 结尾
关于装饰器的知识，还有很多，什么工厂化装饰器，还有闭包，`nonlocal`关键字，如果各位有兴趣，可以去了解一下

老师叫我去办公室了，不说了，拜拜。
