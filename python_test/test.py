'''name=input()
print (name)
a=10
if a>0:
    print(a)
else:
    print(-a)
b=0o55#octal_iteral
print('I\'m ok.')
print("\\\n\\")
print(r'\\\n\\')'''#默认不转义
print(
'''line1
line2
line3''')#多行内容
'''print(True and False)
print(not True)#!True
print(10/3)
print(10//3)#整除
print(ord("$"),chr(68))
x=b'Hi'#Bytes type. ABC->string type
print(x.decode('ascii'))
c='中国'.encode('utf-8')
print(c.decode('utf-8'))
print('Wow,%s,you have $%d'%('Sean',99999999))
print('%04d,%.2f%%'%(3,3.1415926))#%%->char '%'
fruits=['apple','banana','cherry']#a list
fruits.insert(3,'durian')#??没见过榴莲??辣么好次??
fruits.append('egg-fruit')
fruits.append('wrong fruit')
fruits.pop()#or use subscript
fruits[4]='elderberry'
print(fruits,fruits[0],fruits[-1]," The length of list is:",len(fruits))
anything=['emm',['xixi','haha'],250,'mdzz']#length==4
letter=('a','b','c')#a tuple(immutable)
OPai1=(1)#not a tuple,just (to be) number 1
OPai2=(1,)#a tuple, this way can avoid ambiguity
age=20
if age<18:
    print('XiLu')
elif age>=18:#else if
    print('DaLao')

birth=int(input('birth'))#input() return str
if birth < 2000:
    print('00前')
else:
    print('00后')
names=['A','B','C']
for name in names:
    print(name)
print(sum(list(range(2,6)),0))#start value of sum
sum1=0
n=10
while n>0:
    if n<=6:
        break
    sum1+=n
    n-=1
print(sum1)
dictionary={'A':'apple','B':'banana','C':'cherry'}#similar to map
print(dictionary['A'],'E'in dictionary,dictionary.get('E',-1),dictionary.pop('F',"don't exist"))
#throw error_runtime if key don't exist. So check key in this way
s=set([1,2,3])#set container
print(s)
s1=set([1,2,3])#take it as mathematics
s2=set([1,3])
print(s1&s2)
a=('ABC')#althought tuple is immutable,but invoke its copy is legitimate
b=a.replace('A','a')

def factorial(n):#递归函数
    if n==1:
        return 1
    return n * factorial(n - 1)
print(factorial(3))
def fact(n):#尾递归优化，可以防止栈溢出，但是python并没有做优化，所以和普通迭代一样会数据溢出
    return fact_iter(n, 1)
def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
print(fact(3))

def hanoi(n,x,y,z):#用递归函数解决汉诺塔问题
    if n == 1:
        print(x, '-->', z)
    else:
        hanoi(n - 1, x, z, y)  # 将前n-1个盘子从x移动到y上
        hanoi(1, x, y, z)  # 将最底下的最后一个盘子从x移动到z上
        hanoi(n - 1, y, x, z)  # 将y上的n-1个盘子移动到z上
hanoi(3,'A','B','C')
L=[]
n=1
while n<10:
    L.append(n)
    n=n+2
print(L)

r=[]
n=3
for i in range(n):#i:0->2
    r.append(L[i])
print(r)

#Slice切片
l1=list(range(100))
l1[:10]#取前10个元素
l1[-10:]#取后10个元素
l1[10:20]#取10-20范围元素
print(l1[:10:2])#取前十个元素  每两个取一个
l1[::5]#每5个取一个

#estimate whether the object is iterable or not
from collections import Iterable
print(isinstance('abc',Iterable))

for i,value in enumerate(['A','B','C']):#内置函数enumerate把list编程元素-索引对
    print(i,value)
for x,y in[(0,'A'),(1,'B'),(2,'C')]:
    print(x,y)#同上ditto

l2=[x*x for x in range(1,11)if x%2==0]#列表生成式
print(l2)

l3=[m+n for m in 'AB' for n in 'XY']#生成全排列 两层循环
print(l3)

import os
print([d for d in os.listdir('.')])#输出当前目录下所有的文件和目录名

d={'x':'A','y':'B','z':'C'}#dic的items()可以同时迭代key和value
for k,v in d.items():
    print(k,"=",v)
dd=[k+'='+v for k,v in d.items()]#用两个变量生成list
print(dd)

l4=['AdGd','FeKa']
l5='aa'
print([s.lower() for s in l4],isinstance(l5,str))
#把所有字符串变成小写lower只适用于字符串 后面是判断l5是否为字符串

g=(x*x for x in range(1))
print(next(g))
#print(next(g))#用next()函数容易出错,应该用for循环


def fib(max1):#Fibonacci
    n,a,b=0,0,1
    while n<max1:
        yield b  #yield 生成器 生成generator
        a,b=b,a+b
        n=n+1
    return 'done'

f=fib(6)
print(f)
for n in f:
    print(n)#发现没有返回值要捕获StopIteration错误

g=fib(6)
while True:
    try:
        x=next(g)
        print ('g:',x)
    except StopIteration as e:
        print('Generator return value:',e.value)
        break

#杨辉三角
def triangles():#基础版
    L = [1]
    while True:
        yield L
        L.append(0)
        L=[L[i-1]+L[i] for i in range(len(L))]

def triangles():#高级版
    a=[1]
    while True:
        yield a
        a=[sum(i) for i in zip([0]+a,a+[0])]
        # x=[x1,x2] y=[y1,y2]
        # zip(x,y)=[(x1,y1),(x2,y2)]“错位”
n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break

#检测是否为可迭代对象
from collections import Iterable
print(
isinstance([],Iterable),
isinstance((),Iterable),
isinstance({},Iterable),
isinstance("",Iterable),
isinstance((x for x in range(10)),Iterable),
isinstance(100,Iterable)
)
#list tuple dic str虽然Iterable,但不是iterator。但可以用iter来使他成为iterator
from collections import Iterator
print(
isinstance([],Iterator),
isinstance((),Iterator),
isinstance({},Iterator),
isinstance("",Iterator),
isinstance((x for x in range(10)),Iterator),
isinstance(100,Iterator),
isinstance(iter([]),Iterator)
)

for x in [1,2,3]:
    pass
#euqals to
it=[1,2,3]
while True:
    try:
        x=next(it)
    except StopIteration:
        break'''
'''
def add(x,y,f):#高阶函数
    return f(x)+f(y)
print(add(-3,1,abs))
def square(x):
    return x*x
r=map(square,[1,2,3,4,5,6])
print(list(r))#Iterator是惰性序列，要用list()函数把它整个序列都计算出来并返回一个list
print(list(map(str,[1,2,3,4,5])))

from functools import reduce
#这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，当然可以用sum()函数
#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
def add2(x,y):
    return x+y
a=reduce(add2,[1,2,3,4])
print(a)

def fn(x,y):
    return 10*x+y
f1=reduce(fn,[5,2,0])
print(f1)
'''
'''def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
f2=reduce(fn,map(char2num,'520'))
print(f2)

#还可以用lambda来简化程序
def char2int(s):
    return reduce(lambda x,y:x*10+y,map(char2num,'520'))

def normalize(name):
    first=name[0].upper()
    name=name.lower()[1:]
    return first+name
L1=['aadD','DER']
L2=list(map(normalize,L1))
print(L2)

def prod(L):
    return reduce(lambda x,y:x*y,L)
print('3*5*7*9=',prod([3,5,7,9]))
print(float('123.456'))

def is_odd(n):
    return n%2==1
l3=list(filter(is_odd,[1,2,3,4,8,10,13]))
print(l3)
def not_empty(s):
    return s and s.strip()
l4=list(filter(not_empty,['A','',' dd',' ']))
print(l4)

def _odd_iter():
    n1=1
    while True:
        n1=n1+2
        yield n1#构造一个无限序列生成器
def _not_divisible(n2):
    return lambda x:x%n2>0#筛选函数
def primes():#定义一个生成器，不断返回素数
    yield 2
    it=_odd_iter()
    while True:
        n3=next(it)
        yield n3
        it=filter(_not_divisible(n3),it)
for n in primes():
    if n < 50:
        print(n)
    else:
        break

def is_palindrome(n):
    return str(n)==str(n)[::-1]
output = filter(is_palindrome, range(1, 100))
print(list(output))

l=sorted(['apple','Cherry','durian','Banana'],key=str.lower,reverse=True)#按照字母小写排序，并按照倒序排列
print(l)

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0]
def by_score(t):
    return t[1]
l1=sorted(L,key=by_name)
l2=sorted(L,key=by_score)
print(l1,'  ',l2)

def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1,f2,f3= count()
print(f1())

def count1():
    def f(j):
        def g():
            return j*j
        return g
    fs=[]
    for i in range(1,4):
        fs.append(f(i))
    return fs
f1,f2,f3= count1()
print(f1(),f2(),f3())

i=2**38
print(i)

str1="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj map."
str2=str1.split(' ')
str3=''
for word in str2:
    w = ''
    for char in word:
        if char.isalpha() and char not in 'yz':
            w += chr(ord(char) + 2)
        if char == 'y':
            w += 'a'
        if char == 'z':
            w += 'b'
    str3+=w+' '
    #print (w)
    w = ''
print(str3)


str1="}*"#搜索字符串单个字符出现次数
s1=set(['!', '#', '%', '$', '&', ')', '(', '+', '*', '@', '[', ']', '_', '^', 'a', 'e', 'i', 'l', 'q', 'u', 't', 'y', '{', '}'])
for i in str1:
    s1.add(i)
for i in s1:
    print (i,str1.count(i))

def now():
    print('2017-9-26')
f=now
print(now.__name__)'''

'''
def log(func):
    def wrapper(*args,**kw):
        print("call %s()" % func.__name__)
        return func(*args,**kw)
    return wrapper

@log
def now():
    print('2017-9-26')
now()

def log(text):
    def decorator(func):
        def wrapper(*args,**kw):
            print('%s %s()'%(text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print('2017-9-26')
now()

#now=log('execute')(now)#3层嵌套
#print(now.__name__)

import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def future():
    print('2017-9-27')
future()

i1=int('1111',2)
print(i1)

def int2(x,base=2):
    return int(x,base)
i3=int2('100011')
print(i3)

import functools
int2=functools.partial(int,base=2)#偏函数
# 简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），
# 返回一个新的函数，调用这个新函数会更简单。
i4=int2("10001")
print(i4)

max2 = functools.partial(max, 10)#实际上会把10作为*args的一部分自动加到左边
m1=max2(5,2,3)
print(m1)

from PIL import Image
im = Image.open('test.png')
print(im.format, im.size, im.mode)
#PNG (400, 300) RGB
im.thumbnail((200, 100))
im.save('thumb.jpg', 'JPEG')

std1={'name':'A','score':99}
std2={'name':'B','score':89}
def print_score(std):
    print('%s:%s' %(std['name'],std['score']))
print_score(std1)

class Student(object):
    def __init__(self,name,score):
        self.__name=name#在属性前加两条下划线'__'可以使其变为private，外部不可访问
        self.__score=score

    def print_score(self):
        print('%s:%s' %(self.__name,self.__score))

    def get_grade(self):#封装
        if self.__score >=90:
            return 'A'
        elif self.__score >=60:
            return 'A'
        else:
            return 'C'

    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score

    def set_score(self,score):
        if 0<=score<=100:
            self.__score = score
        else:
            raise ValueError('bad score')

bar=Student('Bar',57)
bar.print_score()
print(bar.get_name())
print(bar.get_score())
print(bar.get_grade())

bar.set_score(60)
print(bar.get_score())
print(bar._Student__name)#（虽然可从外部直接访问private，但）不要这么干！编译器可能会把__name改成不同的变量名'''

class Animal(object):
    def run(self):
        print('Animal is running...')
class Dog(Animal):
    def run(self):
        print('Dog is running...')

dog=Dog()
dog.run()

i=isinstance(dog,Dog)
ii=isinstance(dog,Animal)
print(i,ii)


def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())
run_twice(Dog())

class tortoise(Animal):
    def run(self):
        print('Tortoise is running...')
run_twice(tortoise())#新增一个Animal的子类，不必对run_twice()做任何修改