#!/usr/bin/env python3
# -*- coding:utf-8 -*-

print('你好')

result = 1 and 2
print(result)

exec("print('hello')")

d = eval("x+y", {"x": 1, "y": 2})
print(d)
'''
s = """              #一大段代码
for x in range(10):
    print(x, end='')  
print()
"""
name = ""
code_exec = compile(s, '<string>', 'exec')
code_eval = compile('10+20', '<string>', 'eval')
code_single = compile('name = input("Input Your Name: ")', '<string>', 'single')   #交互式
a = exec(code_exec)   # 使用的exec，因此没有返回值
b = eval(code_eval)

c = exec(code_single)  # 交互
d = eval(code_single)
print('a: ', a)
print('b: ', b)
print('c: ', c)
print('name: ', name)
print('d: ', d)
print('name; ', name)
print(not 1)

a = ["1"]
b = a
print(a is b)

for letter in 'Python':
    if letter == 'h':
        break
    print('当前字母 :', letter)'''

for letter in 'Python':
    if letter == 'h':
        pass
        print('这是 pass 块')
    print('当前字母 :', letter)
print("Good bye!")
assert True
print("Good bye!")

try:
    print(1)
finally:
    print(2)

a = 1
b = a
del a
print(b)#1


def foo():
    print("starting...")
    while True: res = yield 4
    print("res:",res)


g = foo()
print(next(g))
print("*"*20)
print(next(g))

sum1 = 1 + \
        2

'''
123
456
789
'''





