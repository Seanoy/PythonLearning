#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from collections import deque

print("hello,seanOY!")


# 解压序列赋值给多个变量
p = (4, 5)
x, y = p
print(x, y)

data = ['ABC', 50, 91.1, (2018, 12, 12)]
name, shares, price, date = data
print(name, shares, price, date)

name, shares, price, (year, month, day) = data
print(name, shares, price, year, month, day)

s = 'Hello'
a, b, c, d, e = s
print(a, b, c, d, e)

# unzip parts of the sequence
_, shares1, price1, _ = data
print(shares1, price1)

# 解压可迭代对象赋值给多个变量 星号表达式
record = ('seanOY', 'oyzeyuan@163.com', '18022615295', '18888888888', 123)
name, email, *phone_number, num = record
# 解压出的 phone numbers 变量永远都是列表类型
print(name, email, phone_number, num)


def average(data8):
    *data7, data1 = data8
    data_avg = sum(data7) / len(data7)
    return data_avg


print(average([1, 2, 3, 4, 5, 6, 7, 9]))


# 星号表达式在迭代元素为可变长元组的序列时是很有用的
records = [('apple', 1, 2),
           ('banana', 'hey'),
           ('apple', 3, 4)]


def eat_apple(x1, y1):
    print('apple', x1, y1)


def eat_banana(s1):
    print('banana', s1)


# 通过星号表达式取标签，然后输出列表args里的数据
for tag, *args in records:
    if tag == 'apple':
        eat_apple(*args)
    elif tag == 'banana':
        eat_banana(*args)

# 星号解压语法在字符串操作的时候也会很有用，比如字符串的分割
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
usr_name, *field, home_dir, sh = line.split(':')
print(usr_name, home_dir, sh)
print(field)

# 有时候，你想解压一些元素后丢弃它们，你不能简单就使用 * ，但是你可以使用一个普通的废弃名称，比如 _或者 ign
record = ('seanOY', 22, 'Male', (3, 1997))
my_name, *_, (*_, year) = record
print(my_name, year)


def sum1(nums):
    head, tail = nums
    return head + sum1(tail) if tail else head


print(sum([1, 2, 3, 4, 5]), '\n')


# 保留最后 N 个元素


def search(lines, pattern, history=1):
    previous_lines = deque(maxlen=history)
    for li in lines:
        if pattern in li:
            yield li, previous_lines
        previous_lines.append(li)


# print deque separately
f = open(r'./data.txt')
for line, p_lines in search(f, 'born', 1):  # history指保留多少条上文的数据
    print(line, p_lines, '\n')
    for p_line in p_lines:
        print(p_line, end='')   # 上文的数据
    print(line, end='')
    print('-' * 20, '\n')









