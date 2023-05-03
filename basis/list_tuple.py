# -*- coding: utf-8 -*-

# list
# list为有序集合，可变
# 追加元素到末尾 append
# 指定位置插入元素 insert
# 删除元素 pop

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adma', 'Bart', 'Lisa']
]
# 获取元素长度
print(len(L))

# 打印Apple
print(L[0][0])

# 打印Python
print(L[1][1])

# 打印Lisa
print(L[-1][-1])

# 追加元素到末尾
L.append('lzy')
print(L)

# 指定位置插入元素
L.insert(1, ['l', 'z', 'y'])
print(L)

# 删除元素
L.pop()
print(L)
L.pop(0)
print(L)

# 某元素重新赋值（即替换元素）
L[0][1] = 'Huawei'
print(L)


# tuple
# tuple有序，但不可变
# 无append()、insert()类似方法
