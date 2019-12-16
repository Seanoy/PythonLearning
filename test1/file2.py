#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
integer = 10
float_num = 10.0
string = "seanOY"
print(integer)
print(float_num)
print(string)
num1 = num2 = num3 = 66  # 创建3个都为整型的变量
num4 = string2 = 66, "xxm"

var1 = 1
var2 = 11
var3 = 12
var4 = 15656
var5 = 1.1
var6 = 1e1
var7 = 1E1
var8 = 1+.2j
print(var8)
complex2 = complex(4, 5)
string1 = "_y1997"
print(string1[2:6])
print(string1[-1])

print(string1[0:5:2])

list1 = ['1', '2', '3', '4', ['4', '5'], "string"]
print(list1[4][1])
print(list1[5][0:6:2])
print(list1[:3])
print(list1[4:])
print(list1[1:3])
print(list1[1:6:2])

tuple1 = ('hello', "world", 1, [1, 2])
print(tuple1)
print(tuple1[3])
print(tuple1[2:4])

dict1 = {'fruit1': 'apple', 'fruit2': 'banana', 2: 'cherry'}
print(dict1['fruit1'])
print(dict1[2])
print(dict1.keys())
print(dict1.values())

print(complex('1+2j'))
s = 'abc'
print(str(s))
print(repr('abc'))
x = 10
y = 10
print(eval("x+y*2"))

arg1 = 6
eval("arg1+6")  # 12
dict3 = {"arg2": 2}
result = eval("arg2+4", dict3)  # 6

print(result)



a = 10
b = 20
c = 30
g = {'a': 1, 'b': 2}
k = {'b': 3, 'c': 4}
result = eval("a+b+c", g, k)
print(result)
result1 = set('hello,seanOY')
print(result1)
result2 = set("hello,sillym")
print(result2)
print(result1 & result2)
print(result1 | result2)
print(result1 - result2)
"""
result = dict(a=1, b=2)
print(result)

result = dict(zip(['sean', 'OY'], [123, 777]))
print(result)

result = dict([('apple', 1), ('banana', 2)])
print(result)

a = frozenset(range(0, 10))
print(a)
b = frozenset("seanOY")
print(b)

c = chr(23455)
print(c)

d = ord('d')
print(d)

e = oct(10)
print(e)
