#!/usr/bin/env python3
# -*- coding:utf-8 -*-

text = "hello world"
r = text.ljust(20)
print(r)
r = text.rjust(20)
print(r)
r = text.rjust(20, "=")
print(r)
r = text.ljust(20, "=")
print(r)
r = text.center(20, "*")
print(r)
r = format(text, '>20')
print(r)
r = '{:>10s}{:>10s}'.format('Hello', 'world')
print(r)
r = format(1.234, '>10')
print(r)
r = format(1.234, '^10.2f')
print(r)