#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import heapq
from collections import deque
# 使用 deque(maxlen=N) 构造函数会新建一个固定大小的队列。
# 当新的元素加入并且这个队列已满的时候，最老的元素会自动被移除掉。

q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q)
q.append(4)
print(q)
q.append(5)
print(q)

# 不设置最大队列大小，那么就会得到一个无限大小队列
q1 = deque()
q1.append(1)
q1.appendleft(2)
print(q1)
q1.pop()
print(q1)
q1.popleft()
print(q1)

# 查找最大或最小的 N 个元素
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))
portfolio = [
 {'name': 'IBM', 'shares': 100, 'price': 91.1},
 {'name': 'AAPL', 'shares': 50, 'price': 543.22},
 {'name': 'FB', 'shares': 200, 'price': 21.09},
 {'name': 'HPQ', 'shares': 35, 'price': 31.75},
 {'name': 'YHOO', 'shares': 45, 'price': 16.35},
 {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap = heapq.nsmallest(2, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(2, portfolio, key=lambda s: s['price'])
print(cheap, '\n', expensive)

# heap[0]始终是最小数 （小根堆）
heapq.heapify(nums)
print(nums)
# 弹出第一个数
print(heapq.heappop(nums))
print(nums)





