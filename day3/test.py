#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import math
from itertools import compress
from collections import namedtuple
import os
from collections import ChainMap
# 过滤序列元素
# 列表推导
my_list = [1, 4, -5, 10, -7, 2, 3, -1]
print([n for n in my_list if n > 0])
print([n for n in my_list if n < 0])
# 使用列表推导的一个潜在缺陷就是如果输入非常大的时候会产生一个非常大的结果集，占用大量内存。

# 使用生成器表达式迭代
pos = (n for n in my_list if n > 0)
for x in pos:
    print(x)
print(list(pos))    # 将迭代器数据转换为列表

# 使用filter函数
values = ['1', '2', '-3', '-', '4', 'N/A', '5']


def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False


ivals = list(filter(is_int, values))
print(ivals)

# 过滤数据时转换数据
data = [math.sqrt(n) for n in my_list if n > 0]
print(data)

# 过滤操作的一个变种就是将不符合条件的值用新的值代替，而不是丢弃它们。
clip_neg = [n if n > 0 else 0 for n in my_list]
print(clip_neg)

addresses = [
 '5412 N CLARK',
 '5148 N CLARK',
 '5800 E 58TH',
 '2122 N CLARK',
 '5645 N RAVENSWOOD',
 '1060 W ADDISON',
 '4801 N BROADWAY',
 '1039 W GRANVILLE',
]
counts = [0, 3, 10, 4, 1, 7, 6, 1]
more5 = [n > 5 for n in counts]
print(more5)
print(list(compress(addresses, more5)))
# 这里的关键点在于先创建一个 Boolean 序列，指示哪些元素复合条件。然后
# compress() 函数根据这个序列去选择输出对应位置为 True 的元素

#从字典中提取子集
prices = {
 'ACME': 45.23,
 'AAPL': 612.78,
 'IBM': 205.55,
 'HPQ': 37.20,
 'FB': 10.75
}
# make a dictionary of all prices over 200
p1 = {key: value for key, value in prices.items() if value > 200}
# make a dictionary of tech stocks
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = {key: value for key, value in prices.items() if key in tech_names}
print(p1, p2)

# 大多数情况下字典推导能做到的，通过创建一个元组序列然后把它传给 dict() 函数也能实现。
p3 = dict((key, value) for key, value in prices.items() if value > 200)
print(p3)
p4 = {key: prices[key] for key in prices.keys() & tech_names}
print(p4)
# value == prices[key]，但后者更慢，大概是要索引的原因

# 映射名称到序列元素
Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('oyzeyuan@163.com', '2019-2-17')
print(sub)
print(sub.addr, sub.joined)
print(len(sub))
addr1, joined1 = sub
print(addr1, joined1)
# 命名元组的一个主要用途是将你的代码从下标操作中解脱出来。

# aim to declare the difference between them
# 普通元组代码


def compute_cost(records):
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total
# 下标操作通常会让代码表意不清晰，并且非常依赖记录的结构。


# 命名元组代码
Stock = namedtuple('Stock', ['name', 'shares', 'price'])


def compute_cost2(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total


# 命名元组另一个用途就是作为字典的替代
s = Stock('ACME', 100, 123.45)
print(s)
# 但命名元组不可修改（和元组一样）
# s.shares = 75
# 如果真的要修改属性
s = s._replace(shares=75)
print(s)

# replace() 方法还有一个很有用的特性就是当你的命名元组拥有可选或者缺失字段时候，它是一个非常方便的填充数据的方法。
Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])

# create a prototype instance
stock_prototype = Stock('', 0, 0.0, None, None)
# function to convert a dictionary to a stock


def dict_to_stock(data1):
    return stock_prototype._replace(**data1)


a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
print(a)
print(dict_to_stock(a))
print(b)
print(dict_to_stock(b))
# 如果你的目标是定义一个需要更新很多实例属性的高效数据结构，
# 那么命名元组并不是你的最佳选择。这时候你应该考虑定义一个包含__slots__方法的类


# 转换并同时计算数据
num = [1, 2, 3, 4]
s = sum(x * x for x in num)
print(s)


files = os.listdir('D:\python_learn\day3')
if any(name.endswith('.py') for name in files):
    print('There be python!')
else:
    print('Sorry, no python.')

# Output a tuple as CSV
s = ('AC', 50, 1.1)
print(','.join(str(x) for x in s))


portfolio = [
 {'name': 'GOOG', 'shares': 50},
 {'name': 'YHOO', 'shares': 75},
 {'name': 'AOL', 'shares': 20},
 {'name': 'SCOX', 'shares': 65}
]

# Original: Returns 20
min_share = min(s['shares'] for s in portfolio)
print(min_share)

# Alternative: Returns {'name': 'AOL', 'shares': 20}
min_shares = min(portfolio, key=lambda s: s['shares'])
print(min_shares)

# 合并多个字典或映射
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
c = ChainMap(a, b)      # 如果在a中找不到就到b中找
print(c['x'])
print(c['y'])
print(c['z'])

print(len(c))
print(list(c.keys()))
print(list(c.values()))
print(list(c.items()))

# 对于字典的更新或删除操作总是影响的是列表中第一个字典。
c['z'] = 10
c['w'] = 40
del c['x']
print(a)

# ChainMap 对于编程语言中的作用范围变量 (比如 globals , locals 等) 是非常有用
values = ChainMap()
values['y'] = 1
# Add a new mapping
values = values.new_child()
values['x'] = 2
# Add a new mapping
values = values.new_child()
values['x'] = 3
print(values)

# discard last mapping
values = values.parents
print(values['x'])

# 作为 ChainMap 的替代，你可能会考虑使用 update() 方法将两个字典合并。
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
merged = dict(b)
merged.update(a)
print(merged.items())

# 如果原字典做了更新，这种改变不会反应到新的合并字典中去
a['x'] = 13
print(merged['x'])

# ChainMap 使用原来的字典，它自己不创建新的字典。所以它并不会产生上面所说的结果
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
merged = ChainMap(a, b)
print(merged['x'])
a['x'] = 40
print(merged['x'])  # Notice change to merged dicts

