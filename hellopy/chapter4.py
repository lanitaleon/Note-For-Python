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

spam = [2, 5, 3.14, 1, -7]
spam.sort()
print(spam)

bacon = ['Alice', 'ants', 'Bob', 'badgers']
bacon.sort()
print(bacon)

bacon.sort(key=str.lower)
print(bacon)

bacon.reverse()
print(bacon)

"""
默认是ASCII排序，大写字母在前，字典序需要单独设置
"""
