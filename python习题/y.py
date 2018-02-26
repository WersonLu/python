# !/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2018/1/8 10:17
 
'''
x = 10
while x:
    x = x - 1
    if x % 2 != 0: continue
    print(x, end=' ')

sum = 0
for i in [1, 2, 3, 4, 5]:
    sum = sum + i
print(sum)

s1 = {1, 3, 5, 7, 8}
for i in s1:
    print(i, end=" ")


# 裴波纳契数列
def f(n):
    if n < 2:
        return 1
    else:
        return f(n - 1) + f(n - 2)


print(f(19))


def f2(n):
    f1 = f2 = 1
    for k in range(1, n):
        f1, f2 = f2, f2 + f1
    return f2


print(f2(19))


def f3(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1


print(f3(5))

# def f4(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n = n + 1
#
#
# print(f4(2))

for i in range(1, 10):
    for j in range(1, i + 1):
        print('{}x{}={}\t'.format(i, j, i * j), end="")
    print()
