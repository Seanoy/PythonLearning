#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import re
import os
from urllib.request import urlopen
from fnmatch import fnmatch, fnmatchcase


# 使用多个界定符分割字符串
line = 'aab ccd; kkk, opp,qqq, foo'
sp = re.split(r'[;,\s]\s*', line)    # 分隔符可以是逗号，分号或者空格，并且后面紧跟着任意个空格
print(sp)

# 如果使用了捕获分组，那么被匹配的文本也将出现在结果列表中
sp2 = re.split(r'(;|,|\s)\s*', line)
print(sp2)

# 获取分割字符在某些情况下也是有用的。比如，你可能想保留分割字符串，用来在后面重新构造一个新的输出字符串
values = sp2[::2]
delimiters = sp2[1::2] + ['']
print(values)
print(delimiters)

# Reform the line using the same delimiters
sp3 = ''.join(v+d for v, d in zip(values, delimiters))
print(sp3)

# 如果你不想保留分割字符串到结果列表中去，但仍然需要使用到括号来分组正则表
# 达式的话，确保你的分组是非捕获分组，形如 (?:...) 。
print(re.split(r'(?:,|;|\s)\s*', line))

# 字符串开头或结尾匹配    str.startswith() or str.endswith()
filename = 'spam.txt'
fs = filename.startswith('file')
fe = filename.endswith('.txt')
print(fs, fe)

# 如果你想检查多种匹配可能，只需要将所有的匹配项放入到一个元组中去，然后传
# 给 startswith() 或者 endswith() 方法
filenames = os.listdir('.')
print(filenames)
result = [name for name in filenames if name.endswith(('.c', '.h'))]
print(result)

result = any(name.endswith('.py') for name in filenames)
print(result)


def read_data(name):
    if name.startswith(('http:', 'https:', 'ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()


choices = ['https:', 'ftp:']  # 要先转换为元组
url = 'https://github.com/Seanoy'
result = url.startswith(tuple(choices))
print(result)
# read_data(url)

# 用Shell通配符匹配字符串
result = fnmatch('foo.txt', '*.txt')
print(result)
result = fnmatch('foo.txt', '?oo.txt')
print(result)
result = fnmatch('Dat45.csv', 'Dat[0-9]*')
print(result)
names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
result = [name for name in names if fnmatch(name, 'Dat*.csv')]
print(result)

# 后者要完全匹配，前者根据系统不同结果不同
print(fnmatch('f.txt', '*.TXT'), fnmatchcase('f.txt', '*.TXT'))


addresses = [
 '5412 N CLARK ST',
 '1060 W ADDISON ST',
 '1039 W GRANVILLE AVE',
 '2122 N CLARK ST',
 '4802 N BROADWAY',
]

result = [addr for addr in addresses if fnmatchcase(addr, '*ST')]
print(result)

result = [addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')]
print(result)

# 字符串匹配和搜索
text = 'yeah, but no, but yeah, but no, but yeah'
result = text == 'yeah'
print(result)
# Match at start or end
print(text.startswith('yeah'))
print(text.endswith('no'))
# Search for the location of the first occurrence
print(text.find('no'))


# 对于复杂的匹配需要使用正则表达式和re模块
text1 = '11/27/2012'
text2 = 'Nov 27, 2012'
# Simple matching: \d+ means match one or more digits
if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')

if re.match(r'\d+/\d+/\d+', text2):
    print('yes')
else:
    print('no')


# 如果你想使用同一个模式去做多次匹配，你应该先将模式字符串预编译为模式对象。
datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(text1):
    print('yes')
else:
    print('no')

# match() 总是从字符串开始去匹配，如果你想查找字符串任意部分的模式出现位置，使用 findall() 方法去代替。
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(datepat.findall(text))

# 在定义正则式的时候，通常会利用括号去捕获分组
datepat2 = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat2.match('11/27/2012')
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))
print(m.group())

month, day, year = m.groups()
print(text)

result = datepat2.findall(text)
print(result)

for month, day, year in datepat2.findall(text):
    print('{}-{}-{}'.format(year, month, day))

for m in datepat2.finditer(text):
    print(m.groups())


m = datepat.match('11/27/2012abcdef')
print(m.group())

# 如果你想精确匹配，确保你的正则表达式以 $ 结尾
datepat3 = re.compile(r'(\d+)/(\d+)/(\d+)$')
result = datepat3.match('11/27/2012abcdef')
print(result)
result = datepat.match('11/27/2012')
print(result)

# 如果你仅仅是做一次简单的文本匹配/搜索操作的话，可以略过编译部分，直接使用 re 模块级别的函数。
result = re.findall(r'(\d+)/(\d+)/(\d+)', text)
print(result)

