# spam = ['cat', 'bat', 'rat', 'elephant']
# print(spam[-1])
# print(spam[0:4])
# print(spam[1:3])
# print(spam[0:-1])
# print(spam[:2])
# print(spam[1:])
# print(spam[:])

# print(len(spam))
# spam[1] = 'hello'
# spam[-1] = 12345

"""
又到了花里胡哨的切片时间 
切片是前闭后开的 [i, j)
负数是从结尾往前找
省略就是从0或者从末尾开始
"""

# bacon = ['A', 'B', 'C']
# print(spam + bacon)
# bacon = bacon * 3
# print(bacon)

"""
像string一样可以复制
"""

# spam = ['cat', 'dog', 'rat', 'elephant']
# del spam[2]
# print(spam)

"""
del 也可以删除变量
"""

# myPets = ['Zophie', 'Pooka', 'Fat-tail']
# print('Enter a pet name:')
# name = input()
# if name not in myPets:
#     print('I do not have a pet named ' + name)
# else:
#     print(name + ' is my pet.')    

"""
not in 和 in
"""

# cat = ['fat', 'black', 'loud']
# size, color, disposition = cat
# print(size)
# print(color)
# print(disposition)

"""
多重赋值，数量需要严格一一对应
"""

# supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
# for index, item in enumerate(supplies):
#     print('index: ' + str(index) + ', item: ' + item)

# import random
# print(random.choice(supplies))
# random.shuffle(supplies)
# print(supplies)

# bacon = supplies + ['pens']
# print(bacon)
# print(bacon.index('pens'))
# bacon.remove('pens')
# print(bacon)

# supplies.append('moose')
# supplies.insert(1, 'chicken')
# print(supplies)

"""
enumerate index+value
"""

# spam = [2, 5, 3.14, 1, -7]
# spam.sort()
# print(spam)

# bacon = ['Alice', 'ants', 'Bob', 'badgers']
# bacon.sort()
# print(bacon)

# bacon.sort(key=str.lower)
# print(bacon)

# bacon.reverse()
# print(bacon)

"""
默认是ASCII排序，大写字母在前，字典序需要单独设置
"""

# name = 'Zophie'
# print(name[0])
# print(name[-2])
# print(name[0:4])
# print('Zo' in name)
# print('p' not in name)
# for i in name:
#     print('value: ' + i)

# name[2] = 't' # Error

"""
字符串是char set 跟Java还算相似
赋值是不可以的
"""    

# eggs = ('hello', 42, 0.5)
# print(eggs[0])
# print(eggs[1:3])
# print(len(eggs))
# eggs[1] = 99 # Error

"""
tuple 元组，不可变序列，因为不可变底层会优化效率更好
"""

# print(type(('hello',)))
# print(type(('hello')))

# print(tuple(['cat', 'dog', 5]))
# print(list(('cat', 'dog', 5)))
# print(list('hello'))

"""
tuple list 转换
"""

# bacon = 'Hello'
# print(id(bacon))
# bacon += ' World'
# print(id(bacon))

# eggs = ['cat', 'dog']
# print(id(eggs))
# eggs.append('moose')
# print(id(eggs))
# eggs = ['bat', 'rat']
# print(id(eggs))

"""
python中的所有值都有一个唯一标识，内存地址
"""

# import copy
# spam = ['A', 'B', 'C']
# print(id(spam))
# bacon = copy.copy(spam)
# print(id(bacon))
# bacon[1] = 42
# print(bacon)
# print(id(bacon))

"""
浅拷贝 深拷贝是copy.deepcopy()
下一节的生命游戏就不cv了 在 conwaysgameoflibe.py
"""


