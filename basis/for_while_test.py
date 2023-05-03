# -*- coding: utf-8 -*-
# for 循环
names = ['Mickle', 'Bob', 'Tracy']
for name in names:
    print('hell,' + name)

# 计算1-100整数之和
sum = 0
for x in range(101):
    sum = sum + x
print(sum)

# while 循环
# break提前结束循环
# continue跳过当次循环，直接开始下一次循环
# break、continue语句容易造成死循环，如遇到死循环可以直接control+C停止

# 计算100以内所有奇数之和
sum2 = 0
n = 99
while n > 0:
    sum2 = sum2 + n
    n = n - 2
print(sum2)

# break 使用
m = 1
while m <= 100:
    print(m)
    m = m + 1
    if m > 10: # 当m=11时，满足条件，执行break语句
        break # break语句会结束当前循环
print('END')

# continue 使用
z = 1
while z < 10:
    z = z + 1
    if z % 2 == 0: # 如果z是奇数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的语句不会执行
    print(z)
print('End')