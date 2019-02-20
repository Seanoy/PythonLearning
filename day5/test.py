#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import re
from calendar import month_abbr
# 字符串搜索和替换
text = 'oh, boy next door ♂'
r = text.replace('boy', 'girl')
print(r)

text = 'Today is 2/20/2019. SeanOY python starts at 2/15/2018'
r = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
print(r)
# sub() 函数中的第一个参数是被匹配的模式，第二个参数是替换模式。反斜杠数字 比如 \3 指向前面模式的捕获组号。


# re编译
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
r = datepat.sub(r'\3-\1-\2', text)
print(r)

# 对于更加复杂的替换，可以传递一个替换回调函数来代替


def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{}{}{}'.format(m.group(2), mon_name, m.group(3))


r = datepat.sub(change_date, text)
print(r)

newtext, n = datepat.subn(r'\3-\1-\2', text)
print(newtext, n)


# 字符串忽略大小写的搜索替换
text = 'UPPER PYTHON, lower python, Mixed Python'
r = re.findall('python', text, flags=re.IGNORECASE)
print(r)
r = re.sub('python', 'snake', text, flags=re.IGNORECASE)
print(r)


# 替换字符串并不会自动跟被匹配字符串的大小写保持一致。
def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace


r = re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE)
print(r)


# 最短匹配模式
str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no."'
r = str_pat.findall(text1)
print(r)

text2 = 'Computer says "no." Phone says "yes."'
r = str_pat.findall(text2)
print(r)
# 模式 r'\"(.*)\"' 的意图是匹配被双引号包含的文本。但是在正
# 则表达式中 * 操作符是贪婪的，因此匹配操作会查找最长的可能匹配。

# 为了修正这个问题，可以在模式中的 * 操作符后面加上? 修饰符
str_pat = re.compile(r'\"(.*?)\"')
r = str_pat.findall(text2)
print(r)

# 多行匹配模式
comment = re.compile(r'/\*(.*?)\*')
text1 = '/* this is a comment */'
text2 = '''/* this is a
 multiline comment */
 '''
r = comment.findall(text1)
print(r)
r = comment.findall(text2)
print(r)

# 为了修正这个问题，你可以修改模式字符串，增加对换行的支持
comment = re.compile(r'/\*((?:.|\n)*?)\*/')
r = comment.findall(text2)
print(r)

# 在这个模式中， (?:.|\n) 指定了一个非捕获组 (也就是它定义了一个仅仅用来做
# 匹配，而不能通过单独捕获或者编号的组)。

# 对于简单的情况使用 re.DOTALL 标记参数工作的很好，但是如果模式非常复杂
# 或者是为了构造字符串令牌而将多个模式合并起来
# ，这时候使用这个标记参数就可能出现一些问题。如果让你选择的话，最好还是定义自己的正则表达
# 式模式，这样它可以在不需要额外的标记参数下也能工作的很好。
comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
r = comment.findall(text2)
print(r)




