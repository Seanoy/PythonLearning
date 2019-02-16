#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import heapq
import json
from collections import deque
from collections import OrderedDict
from collections import defaultdict
from collections import Counter
from operator import itemgetter
from operator import attrgetter
from itertools import groupby
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

# 实现一个按优先级排序的队列
# 并且在这个队列上面每次 pop 操作总是返回优先级最高的那个元素


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1
    # 优先级为负数的目的是使得元素按照优先级从高到低排序。
    # 这个跟普通的按优先级从低到高排序的堆排序恰巧相反。因为他最先弹出的数据要最高优先级
    # index变量的作用是保证同等优先级元素的正确排序

    def pop(self):
        return heapq.heappop(self._queue)[-1]  # [-1]最后一个元素


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):  # 返回一个可以用来表示对象的可打印字符串
        return 'Item({!r})'.format(self.name)


q = PriorityQueue()
q.push(Item('apple'), 1)
q.push(Item('banana'), 5)
q.push(Item('carrot'), 4)
q.push(Item('doge'), 1)
# 第一个 pop() 操作返回优先级最高的元素。
# 两个有着相同优先级的元素，pop 操作按照它们被插入到队列的顺序返回。
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())

# Item don't support compare operation
'''a = Item('foo')
b = Item('bar')
print(a < b)'''

# same priority can't compare
'''a = (1, Item('foo'))
b = (2, Item('bar'))
print(a < b)
c = (1, Item('god'))
print(a < c)'''

# 第一个比较完就比较第二个，所以index在比较相同优先级元素时很有效
a = (1, 0, Item('foo'))
b = (5, 1, Item('bar'))
c = (1, 2, Item('god'))
print(a < b)
print(a < c)

# 字典中的键映射多个值
'''d = {
    'a': [2, 3],
    'b': [4, 5]
}'''

d = defaultdict(list)  # 放置值的容器为列表
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
print(d)

d = defaultdict(set)   # 放置值的容器为集合
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)
print(d)

'''d = {}
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(4)
print(d)'''


# 在迭代操作的时候它会保持元素被插入时的顺序  保持Key的顺序
def ordered_dict():
    d = OrderedDict()

    d['foo'] = 1
    d['bar'] = 2
    d['spam'] = 3
    json.dumps(d)
    print(d)


ordered_dict()

prices = {
    'Apple': 12,
    'orange': 20,
    'banana': 11
}
# 为了对字典值执行计算操作，通常需要使用 zip() 函数先将键和值反转过来
min_price = min(zip(prices.values(), prices.keys()))
print(min_price)
# 可以使用 zip() 和 sorted() 函数来排列字典数据
prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)

# zip() 函数创建的是一个只能访问一次的迭代器
prices_and_names = zip(prices.values(), prices.keys())
print(max(prices_and_names))
'print(min(prices_and_names))'

# 想知道value最小（大）的key是什么
price_min = min(prices, key=lambda k: prices[k])
price_max = max(prices, key=lambda k: prices[k])
print(price_min, price_max)

# （值，键）对   值相同时会比较键 ^^
prices = {'A': 12, 'B': 12}
m1 = min(zip(prices.values(), prices.keys()))
m2 = max(zip(prices.values(), prices.keys()))
print(m1, m2)

# find the equal part of the dict
a = {
    'x': 1,
    'y': 2,
    'z': 3,
    'w': 4
}
b = {
    'i': 5,
    'x': 6,
    'y': 2
}
print(a.keys() & b.keys())  # find keys in common
print(a.keys() - b.keys())  # find keys in dict'a' that are not in dict'b'
print(a.items() & b.items())    # find(key, value) pairs in common

# 上述操作可用于修改或者过滤字典元素
c = {key: a[key] for key in a.keys() - {'z', 'w'}}
print(c)


# 如果想要在一个序列上面保持元素顺序的同时消除重复的值
# 如果序列上的值都是 hashable 类型，那么可以很简单的利用集合或者生成器来解决这个问题


def dedupe(items):
    seen = set()    # 创建一个辅助空间存放不重复的数据
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


a = [1, 5, 2, 1, 9, 5, 10]
print(list(dedupe(a)))


# 如果元素非hashable，想要消除如dict类型的元素
# 这里的 key 参数指定了一个函数，将序列元素转换成 hashable 类型。
def dedupe_dict(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
'''list_dict = list(dedupe_dict(a, key=lambda k: (k['x'], k['y'])))  # 删除key为'x'和'y'且value都相同的元素
print(list_dict)'''
list_dict1 = list(dedupe_dict(a, key=lambda k: k['x']))  # 删除key为'x' value相同的元素
print(list_dict1)

# 如果你仅仅就是想消除重复元素，通常可以简单的构造一个集合。
f = [1, 5, 2, 1, 9, 1, 5, 10]
print(set(f),'\n')
# 然而，这种方法不能维护元素的顺序，生成的结果中的元素位置被打乱。而上面的方法可以避免这种情况。

# 删除文件中重复行
f1 = open('./data.txt', 'r+')
f1.write('hello\n')
for line in dedupe(f1):
    print(line)


def fun():
    for i in range(2):  # 逐个生成i
        yield i


for x in fun():
    print(x)


# 命名切片  避免硬编码下标
record = '....................100 .......513.25 ..........'
SHARES = slice(20, 23)
PRICE = slice(31,37)
cost = int(record[SHARES]) * float(record[PRICE])
print(cost)

items = [1, 2, 3, 4, 5]
a = slice(2, 4)
print(items[2:4], items[a])
items[a] = [10, 11]     # 替换掉对应部分
print(items)
del items[a]
print(items)

a = slice(5, 50, 2)
print(a.start, a.stop, a.step)

# 通过调用切片的 indices(size) 方法将它映射到一个确定大小的序列上，
# 这个方法返回一个三元组 (start, stop, step) ，所有值都会被合适的缩小以
# 满足边界限制，从而使用的时候避免出现 IndexError 异常。
s = 'HelloWorld'
print(a.indices(len(s)))
for i in range(*a.indices(len(s))):
    print(s[i])     # 起始5，步距2，终点10  输出第5 7 9号元素


# 序列中出现次数最多的元素  用collections.Counter
words = [
 'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
 'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
 'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
 'my', 'eyes', "you're", 'sexy'
]
word_count = Counter(words)
# 出现频率最高的三个数
top_three = word_count.most_common(3)
print(top_three)
print(word_count['eyes'])

more_words = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
for word in more_words:
    word_count[word] += 1
print(word_count['eyes'])
# 在底层实现上，一个Counter对象就是一个字典，将元素映射到它出现的次数上。
word_count.update(more_words)
print(word_count['eyes'])

# Counter 实例一个鲜为人知的特性是它们可以很容易的跟数学运算操作相结合。
a = Counter(words)
b = Counter(more_words)
print(a)
print(b)
c = a + b
print(c)
d = a - b
print(d)

# 通过某个关键字排序一个字典列表   通过operator模块的itemgetter函数
rows = [
 {'fn': 'Brian', 'ln': 'Jones', 'uid': 1003},
 {'fn': 'David', 'ln': 'Beazley', 'uid': 1002},
 {'fn': 'John', 'ln': 'Cleese', 'uid': 1001},
 {'fn': 'Big', 'ln': 'Jones', 'uid': 1004}
]

rows_by_fn = sorted(rows, key=itemgetter('fn'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))
print(rows_by_fn)
print(rows_by_uid)
# itemgetter() 函数也支持多个 keys
rows_by_fln = sorted(rows, key=itemgetter('fn', 'ln'))
print(rows_by_fln)
# itemgetter() 同样适用min max
print(min(rows, key=itemgetter('uid')))


# 排序不支持原生比较的对象
class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


def sort_not_compare():
    users = [User(23), User(3), User(99)]
    print(users)
    print(sorted(users, key=lambda u: u.user_id))


sort_not_compare()

# 或者使用operator.attrgetter()代替lambda
users1 = [User(33), User(63), User(19)]
print(sorted(users1, key=attrgetter('user_id')))


class User1:
    def __init__(self, user_id, fn, ln):
        self.user_id = user_id
        self.fn = fn
        self.ln = ln

    def __repr__(self):
        return 'User({!r})'.format(self.fn)


users2 = [User1(12, 'Sean', 'oy'), User1(3, 'Tom', 'cat')]
by_name = sorted(users2, key=attrgetter('ln', 'fn'))
print(by_name)
print(min(users2, key=attrgetter('user_id')))

# 通过某个字段将记录分组  such as 'date'
rows = [
 {'address': '5412 N CLARK', 'date': '07/01/2012'},
 {'address': '5148 N CLARK', 'date': '07/04/2012'},
 {'address': '5800 E 58TH', 'date': '07/02/2012'},
 {'address': '2122 N CLARK', 'date': '07/03/2012'},
 {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
 {'address': '1060 W ADDISON', 'date': '07/02/2012'},
 {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
 {'address': '1039 W GRANVILLE', 'date': '07/04/2012'}
]

# Sort by the desired field first
rows.sort(key=itemgetter('date'))
# Iterate in groups
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print(' ', i)
print('\n')

rows_by_date = defaultdict(list)
for row in rows:
    rows_by_date[row['date']].append(row)

for r in rows_by_date['07/01/2012']:
    print(r)

