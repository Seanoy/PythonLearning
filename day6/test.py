#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import unicodedata
import re
import sys

# 将 Unicode 文本标准化
s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'
print(s1, s2)
# 这里的文本”Spicy Jalapeño” 使用了两种形式来表示。第一种使用整体字符”ñ”
# (U+00F1)，第二种使用拉丁字母”n” 后面跟一个”˜” 的组合字符 (U+0303)。
print(s1 == s2, len(s1), len(s2))

# 在需要比较字符串的程序中使用字符的多种表示会产生问题。为了修正这个问题，
# 你可以使用 unicodedata 模块先将文本标准化

t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
print(t1 == t2, ascii(t1))

t3 = unicodedata.normalize('NFD', s1)
t4 = unicodedata.normalize('NFD', s2)
print(t1 == t2, ascii(t3))
# NFC 表示字符应该是整体组成 (比如可能的话就使用单一编码)，
# 而 NFD 表示字符应该分解为多个组合字符表示。

# Python 同样支持扩展的标准化形式 NFKC 和 NFKD，它们在处理某些字符的时候增加了额外的兼容特性。
s = '\ufb01'  # A single character
print(s)
# Notice how the combined letters are broken apart here
s3 = unicodedata.normalize('NFKD', s)
s4 = unicodedata.normalize('NFKC', s)
print(s3, s4)


# 在清理和过滤文本的时候字符的标准化也是很重要的。比如，假设你想清除掉一些
# 文本上面的变音符的时候 (可能是为了搜索和匹配)：
t1 = unicodedata.normalize('NFD', s1)
r = ''.join(c for c in t1 if not unicodedata.combining(c))
# combining() 函数可以测试一个字符是否为和音字符。
print(r)


# 在正则式中使用 Unicode
num = re.compile('\d+')
# ASCII digits
r = num.match('123')
print(r)
r1 = num.match('\u0661\u0662\u0663')
print(r1)

# 如果你想在模式中包含指定的 Unicode 字符，你可以使用 Unicode 字符对应的转
# 义序列 (比如 \uFFF 或者 \UFFFFFFF )。

arabic = re.compile('[\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff]+')

# 但是同样也应该注意一些特殊情况，比如在忽略大小写匹配和大小写转换时的行为。
pat = re.compile('stra\u00dfe', re.IGNORECASE)
s = 'straße'
r = pat.match(s)  # Matches
print(r)
r = pat.match(s.upper())  # Doesn't match
print(r)
r = s.upper()
print(r)


# 删除字符串中不需要的字符
# Whitespace stripping
s = ' hello world \n'
# lstrip() 和 rstrip() 分别从左和
# 从右执行删除操作。
r = s.strip()
print(r)
r = s.lstrip()
print(r)
r = s.rstrip()
print(r)

# Character stripping
t = '-----hello====='
r = t.lstrip('-')
print(r)
r = t.rstrip('=')
print(r)

# 这些 strip() 方法在读取和清理数据以备后续处理的时候是经常会被用到的。比
# 如，你可以用它们来去掉空格，引号和完成其他任务。
s = ' hello      world \n'
s = s.strip()
# 需要注意的是去除操作不会对字符串的中间的文本产生任何影响。
print(s)

# 如果你想处理中间的空格，那么你需要求助其他技术。比如使用 replace() 方法
# 或者是用正则表达式替换。
r = s.replace(' ', '')
print(r)
r = re.sub('\s+', ' ', s)
print(r)

# 通常情况下你想将字符串 strip 操作和其他迭代操作相结合，比如从文件中读取
# 多行数据。如果是这样的话，那么生成器表达式就可以大显身手了。
with open('D:\python_learn\day6\data.txt') as f:
    lines = (line.strip() for line in f)
    for line in lines:
        print(line)

# 在这里，表达式 lines = (line.strip() for line in f) 执行数据转换操作。这
# 种方式非常高效，因为它不需要预先读取所有数据放到一个临时的列表中去。它仅仅
# 只是创建一个生成器，并且每次返回行之前会先执行 strip 操作。


# 审查清理文本字符串
# 文本清理问题会涉及到包括文本解析与数据处理等一系列问题。

# str.upper() 和 str.lower()将文本转为标准格式。
# str.replace() 或者 re.sub() 简单替换操作能删除或者改变指定的字符序列。
# unicodedata.normalize() 函数将 unicode文本标准化。
# 更进一步，你可能想消除整个区间上的字符或者去除变音符。
# 为了这样做，你可以使用经常会被忽视的 str.translate()方法。

s = 'pýtĥöñ\fis\tawesome\r\n'
print(s)
# 第一步是清理空白字符。为了这样做，先创建一个小的转换表格然后使用translate() 方法
remap = {
    ord('\t'): ' ',
    ord('\f'): ' ',
    ord('\r'): None  # delete
}
a = s.translate(remap)
print(a)
# 空白字符 \t 和 \f 已经被重新映射到一个空格。回车字符 r 直接被删除。

# 你可以以这个表格为基础进一步构建更大的表格
cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
b = unicodedata.normalize('NFD', a)
print(b)
r = b.translate(cmb_chrs)
print(r)

# 通过使用 dict.fromkeys() 方法构造一个字典，每个 Unicode 和音符作为键，对于的值全部为 None 。
# 然后使用 unicodedata.normalize() 将原始输入标准化为分解形式字符。
# 然后再调用 translate 函数删除所有重音符。同样的技术也可以被用来删除其他类型的字符(比如控制字符等)。

# 这里构造一个将所有 Unicode 数字字符映射到对应的 ASCII 字符上的表格
digitmap = {c: ord('0') + unicodedata.digit(chr(c))
            for c in range(sys.maxunicode)
            if unicodedata.category(chr(c)) == 'Nd'}
r = len(digitmap)
print(r)
x = '\u0661\u0662\u0663'
r = x.translate(digitmap)
print(r)


# 另一种清理文本的技术涉及到 I/O 解码与编码函数。这里的思路是先对文本做一些初步的清理，
# 然后再结合 encode() 或者 decode() 操作来清除或修改它。
print(a)
b = unicodedata.normalize('NFD', a)
r = b.encode('ascii', 'ignore').decode('ascii')
print(r)
# 这里的标准化操作将原来的文本分解为单独的和音符。接下来的 ASCII 编码/解码
# 只是简单的一下子丢弃掉那些字符。当然，这种方法仅仅只在最后的目标就是获取到
# 文本对应ACSII表示的时候生效。

#  str.replace() 方法通常是最快的，甚至在你需要多次调用的时候。比如，为了清理空白字符，你可以这样做：
def clean_spaces(s):
    s = s.replace('\r', '')
    s = s.replace('\t', ' ')
    s = s.replace('\f', ' ')
    return s


print(s)
print(clean_spaces(s))


