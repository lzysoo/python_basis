# -*- coding: utf-8 -*-
import math

def my_abs(x):
    if not isinstance(x, (int, float)): # 先判断输入类型是否为int、float，不是抛出具体错误，否则报错信息不会判断数据类型
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-9))

# 定义空函数
# pass当作占位符，如果还没想好怎么写代码，可以先让程序运行起来，否则会报错
def nop():
    pass

# 练习
def quadtice(a, b, c):
    x1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
    x2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
    return x1, x2

print('quadtice(2, 3, 1)= ', quadtice(2, 3, 1))
print('quadtice(1, 3, -4)= ', quadtice(1, 3, -4))

'''
  位置参数
'''
# 定义多参数函数，计算X的n次方
def power(x, n):
    s = 1
    while(n > 0):
        n = n - 1
        s = s * x
    return s
print(power(5, 3))
print(power(5, 2))

'''
   默认参数：可以降低函数调用的难度
'''
# 必选参数在前，默认参数在后
# 当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
# 默认参数必须指向不变对象！！！！！！
def enroll(name, gender, age = 6, city = 'beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

enroll('Bob', 'F') # age、city默认
enroll('Lisa', 'M', 7) # city默认
enroll('Mary', 'F', city='shanghai') # 参数可以不按照顺序写，但需要把参数名写上，这里 age默认

# def add_end(L = []):
#     L.append('End')
#     return L
# print(add_end()) # 输出 【'End】
# print(add_end()) # 输出 【'End', 'End'】，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。

def add_end(L = None):
    if L is None:
        L = []
    L.append('End')
    return L

'''
    可变参数
'''
# 计算 a^2 + b^2 + c^2 + ……
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
# 调用时先组装出一个list或者tuple
print(calc([1, 2, 3]))
print(calc((1, 2, 3, 4)))

# 若利用可变参数，调用函数的方式可简化成 calc(1, 2, 3)
# 把函数参数改为可变参数，仅需在参数前面加个 * ，可变参数在函数调用时自动组装成一个tuple，如下：
# 在调用函数时，可以传入任意个参数，包括0个
def calc2(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc2(1, 2, 3))

# 如果已有一个list或者tuple，想调用可变参数，只需在list或者tuple前加一个 * ，如下：
# *nums 把 nums 这个list的所有元素作为可变参数传进去
nums = [1, 2, 3]
print(calc2(*nums))

'''
    关键字参数
'''
# 关键字参数允许传入0个或者任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
# 关键字参数可以扩展函数的功能
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('Mike', 30)
person('Lisa', 25, city = 'beijing')
person('Bob', 35, gender = 'M', city = 'shanghai')

# 如果已有一个dict，可以在dict前面加 ** 传进去
extra = {'city': 'beijing', 'job': 'Engineer'}
# 普通传入
person('Jack', 24, city = extra['city'], job = extra['job'])
# 简洁传入
# **extra 把 extra 这个dict的所有key-value用关键字参数传入到函数的 **kw 参数，kw将获得一个dict
# 注意：kw 获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra
person('Jack', 24, **extra)

'''
    命名关键字参数
'''
# 可以限制关键字参数的名字
# 需要使用特殊分隔符 * ，* 后面的参数被视为关键字参数
# 命名关键字参数必须传入 参数名，否则会报错
def person2(name, age, *, city, job):
    print(name, age, city, job)

# 如果函数定义中已经有了一个可变参数，后面的命名关键字参数就不需要再加一个特殊分隔符 * 了
def person(name, age, *args, city, job):
    print(name, age, args, city, job)

# 命名关键字可以有缺省值，从而简化调用
def person3(name, age, *, city = 'beijing', job):
    print(name, age, city, job)

person3('Aisa', 23, job = 'woker')

'''
    参数组合
'''
# 可组合使用以上5种参数，但参数定义顺序必须是：必须参数、默认参数、可变参数、命名关键字参数、关键字参数
def f1(a, b, c = 0, *args, **kw):
    print('a=', a, 'b=', b, 'c=', c, 'args=', args, 'kw=', kw)
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw) # a= 1 b= 2 c= 3 args= (4,) kw= {'d': 99, 'x': '#'} ,为什么 a b c分别为1 2 3
