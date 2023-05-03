# -*- coding: utf-8 -*-

# dict
# 键-值（key-value）存储
# 一个key只能对应一个value，所以，当多次对一个key放入value，后面的值会把前面的值冲掉
# 与list相比，dict优缺点：
#   1、查找和插入的速度极快，不会随着key的增加而变慢；
#   2、需要占用大量的内存，内存浪费多。
# dict的key必须是不可变对象

d = {'Mickle' : 96, 'Bob' : '80', 'Lisa' : '90'}
print(d['Mickle'])

# 判断某一个key在不在dict里面
print('tomes' in d) # 通过in判断
print(d.get('tomes', -1)) # 通过get方法，也可自己指定value，默认不存在返回none

# 删除key
d.pop('Bob')
print(d)

# set
# 是一组key的集合，但不存储value
# 无重复key，重复元素在set中会自动过滤

s = set([1, 2, 3])
print(s)

# set添加元素
s.add(4)
print(s)
s.add(3) # 可以重复添加，但无效果
print(s)

# 删除元素
s.remove(4)
print(s)

# set可看成数学意义上无序和无重复元素的集合，可以做数学意义上的交集、并集
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)

# str为不可变对象
a = 'abc'
a.replace('a', 'A')
print(a.replace('a', 'A'))
print(a)

# list为可变对象,内容是会变的
l = ['c', 'b', 'a']
l.sort()
print(l)

# 练习
dict = {(1, 2, 3): 96, (2, 3): 100}
print(dict)

s3 = set((1, [2, 3])) # key应同时满足内容不变和指向不变，这里的tuple指向虽然没变，但内容变了，所以会报错
print(s3)
