#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 数据类型：int/float/str/bool/dict/list/turple/none

# and or not
print(True and False)
print(not False)
print(None)


# 类型转换：int() float() str() bool() list() tuple() dict() set()
# age = input()
# if int(age) >= 18:
#   print('adult')
# else:
#   print('teenager')

print('---\n')

x = 2
x = x + 2
print(x)

print('---\n')

# 格式化
## %s %d %f %x
print('%s %d %f %x' % ('hello', 1, 2.3, 4))

print('Hi, %s, you have $%d.' % ('Michael', 1000000))

# %s永远起作用，它会把任何数据类型转换为字符串
# 用 %% 来表示一个 %

# f-string
r = 2.5
s = 3.14 * r ** 2
print(f'the area of a circle with radius {r} is {s:.2f}')

s1 = 72
s2 = 85
r = (s2 - s1) / s1 * 100
print(f'the raise rate is {r:.1f}%')


print('---\n')

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Bob']
]

print(L[0][0])
print(L[1][1])
print(L[2][2])

s = ()
print(f"s type: {type(s)}")

t = ('a', 'b', ['A', 'B'])
print(t)
# t[1] = 'Y'
# print(t)
t[2][0] = 'X'
print(t)

p = (1, 2, (3, 4))
# p[2][0] = 5
print(p)

class User:
    def __init__(self, name):
        self.name = name

obj = {'name': 'bf'}

print(f"t type: {type(t)}")
print(f"L type: {type(L)}")
print(f"t[2] type: {type(t[2])}")
print(f"t[2][0] type: {type(t[2][0])}")
print(f"1 type: {type(1)}")
print(f"1.0 type: {type(1.0)}")
print(f"True type: {type(True)}")
print(f"User type: {type(User)}")
print(f"None type: {type(None)}")
print(f"User('bf') type: {type(User('bf'))}")
print(f"obj type: {type(obj)}")

print('---\n')

age = 1
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

if age:
    print(f"age is: {age}")

height = 1.75
weight = 80.5
bmi = weight / (height * height)
print(f"bmi is: {bmi}")
if bmi >= 32:
    print('严重肥胖')
elif bmi >= 28:
    print('肥胖')
elif bmi >= 25:
    print('过重')
elif bmi >= 18.5:
    print('正常')
elif bmi >= 18:
    print('偏瘦')
else:
    print('瘦')

match bmi:
    case _ if bmi >= 32:
        print('严重肥胖')
    case _ if bmi >= 28:
        print('肥胖')
    case _ if bmi >= 25:
        print('过重')
    case _ if bmi >= 18.5:
        print('正常')
    case _ if bmi >= 18:
        print('偏瘦')
    case _: # 任意值，default
        print('瘦')

age = 12
match age:
    case x if x >= 18:
        print('adult')
    case 10:
        print('ten')
    case 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18:
        print('11~18 years old.')
    case _:
        print(f"age is: {age}")

# args = ['gcc']
# args = ['gcc', 'hello.c']
# args = ['gcc', 'hello.c', 'world.c']
# args = ['gcc', 'hello.c', 'world.c', 'test.c']
args = ['clean']
match args:
  case ['gcc', file1, file2]:
    print(f"compiling {file1} and {file2}")
  case ['gcc', file1, *files]:
    print(f"compiling {file1} and {files}")
  case ['gcc']:
    print("usage: gcc [file1] [file2]")
  case ['clean']:
    print("cleaning...")
  case _:
    print("usage: gcc [file1] [file2]")

print('---\n')

names = ['bf', 'bf2', 'bf3']
for name in names:
    print(name)

sum = 0
for x in range(10):
    sum = sum + x
print(sum)

n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d.get('Michael'))

d['bf'] = 100
print(d)
d.pop('Bob')
print(d)
d.popitem()
print(d)
print(type(d))

s = set([1, 2, 3])
print(s)
print(type(s))
s.add(4)
print(s)
s.remove(1)
print(s)

s1 = set([1, 2, 3])
s2 = set([3, 4, 5])
print(s1 & s2)
print(s1 | s2)
print(s1 - s2)
print(s1 ^ s2)

a = ['c', 'b', 'a']
a.sort()
print(a)

x = (1, 2, 3)
print(type(x), x)
y = {x[0]: 1, x[1]: 2, x[2]: 3}
print(type(y), y)

def double(x):
    return x * 2

a = map(double, [1, 2, 3])
print(list(a))
