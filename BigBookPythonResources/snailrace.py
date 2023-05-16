"""蜗牛赛跑, 作者：Al Sweigart al@inventwithpython.com
快节奏的蜗牛赛跑行动!
此代码可在https://nostarch.com/big-book-small-python-programming获得
标签:短，艺术，初学者，游戏，多人"""

import random, time, sys

# Set up the constants:
MAX_NUM_SNAILS = 8
MAX_NAME_LENGTH = 20
FINISH_LINE = 40  # (!) 试着修改这个数字。

print('''Snail Race, by Al Sweigart al@inventwithpython.com

    @v <-- snail

''')

# 询问多少蜗牛赛跑:
while True:  # 继续询问，直到玩家输入一个数字。
    print('How many snails will race? Max:', MAX_NUM_SNAILS)
    response = input('> ')
    if response.isdecimal():
        numSnailsRacing = int(response)
        if 1 < numSnailsRacing <= MAX_NUM_SNAILS:
            break
    print('Enter a number between 2 and', MAX_NUM_SNAILS)

# 输入每只蜗牛的名字:
snailNames = []  # 字符串蜗牛名的列表。
for i in range(1, numSnailsRacing + 1):
    while True:  # 继续询问，直到玩家输入有效的名称。
        print('Enter snail #' + str(i) + "'s name:")
        name = input('> ')
        if len(name) == 0:
            print('Please enter a name.')
        elif name in snailNames:
            print('Choose a name that has not already been used.')
        else:
            break  # 输入的名称是可以接受的。
    snailNames.append(name)

# 在起跑线上显示每只蜗牛。
print('\n' * 40)
print('START' + (' ' * (FINISH_LINE - len('START')) + 'FINISH'))
print('|' + (' ' * (FINISH_LINE - len('|')) + '|'))
snailProgress = {}
for snailName in snailNames:
    print(snailName[:MAX_NAME_LENGTH])
    print('@v')
    snailProgress[snailName] = 0

time.sleep(1.5)  # 比赛开始前的暂停。

while True:  # 主程序循环。
    # 随机挑选蜗牛向前移动:
    for i in range(random.randint(1, numSnailsRacing // 2)):
        randomSnailName = random.choice(snailNames)
        snailProgress[randomSnailName] += 1

        # 检查蜗牛是否已经到达终点线:
        if snailProgress[randomSnailName] == FINISH_LINE:
            print(randomSnailName, 'has won!')
            sys.exit()

    # (!) 实验:如果蜗牛有你的名字，在这里添加一个小窍门来增加它的进度。

    time.sleep(0.5)  # (!) 实验:尝试改变这个值。

    # (!) 实验:如果你把这行注释掉会发生什么?
    print('\n' * 40)

    # 显示开始和结束线:
    print('START' + (' ' * (FINISH_LINE - len('START')) + 'FINISH'))
    print('|' + (' ' * (FINISH_LINE - 1) + '|'))

    # 展览螺柱(附有姓名标签):
    for snailName in snailNames:
        spaces = snailProgress[snailName]
        print((' ' * spaces) + snailName[:MAX_NAME_LENGTH])
        print(('.' * snailProgress[snailName]) + '@v')
