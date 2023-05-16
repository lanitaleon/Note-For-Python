"""蒙提霍尔问题， 作者：Al Sweigart al@inventwithpython.com
一个模拟蒙提霍尔游戏秀的问题。
更多信息在https://en.wikipedia.org/wiki/Monty_Hall_problem获得
此代码可在https://nostarch.com/big-book-small-python-programming获得
标签:大型，游戏，数学，模拟"""

import random, sys

ALL_CLOSED = """
+------+  +------+  +------+
|      |  |      |  |      |
|   1  |  |   2  |  |   3  |
|      |  |      |  |      |
|      |  |      |  |      |
|      |  |      |  |      |
+------+  +------+  +------+"""

FIRST_GOAT = """
+------+  +------+  +------+
|  ((  |  |      |  |      |
|  oo  |  |   2  |  |   3  |
| /_/|_|  |      |  |      |
|    | |  |      |  |      |
|GOAT|||  |      |  |      |
+------+  +------+  +------+"""

SECOND_GOAT = """
+------+  +------+  +------+
|      |  |  ((  |  |      |
|   1  |  |  oo  |  |   3  |
|      |  | /_/|_|  |      |
|      |  |    | |  |      |
|      |  |GOAT|||  |      |
+------+  +------+  +------+"""

THIRD_GOAT = """
+------+  +------+  +------+
|      |  |      |  |  ((  |
|   1  |  |   2  |  |  oo  |
|      |  |      |  | /_/|_|
|      |  |      |  |    | |
|      |  |      |  |GOAT|||
+------+  +------+  +------+"""

FIRST_CAR_OTHERS_GOAT = """
+------+  +------+  +------+
| CAR! |  |  ((  |  |  ((  |
|    __|  |  oo  |  |  oo  |
|  _/  |  | /_/|_|  | /_/|_|
| /_ __|  |    | |  |    | |
|   O  |  |GOAT|||  |GOAT|||
+------+  +------+  +------+"""

SECOND_CAR_OTHERS_GOAT = """
+------+  +------+  +------+
|  ((  |  | CAR! |  |  ((  |
|  oo  |  |    __|  |  oo  |
| /_/|_|  |  _/  |  | /_/|_|
|    | |  | /_ __|  |    | |
|GOAT|||  |   O  |  |GOAT|||
+------+  +------+  +------+"""

THIRD_CAR_OTHERS_GOAT = """
+------+  +------+  +------+
|  ((  |  |  ((  |  | CAR! |
|  oo  |  |  oo  |  |    __|
| /_/|_|  | /_/|_|  |  _/  |
|    | |  |    | |  | /_ __|
|GOAT|||  |GOAT|||  |   O  |
+------+  +------+  +------+"""

print('''The Monty Hall Problem, by Al Sweigart al@inventwithpython.com

In the Monty Hall game show, you can pick one of three doors. One door
has a new car for a prize. The other two doors have worthless goats:
{}
Say you pick Door #1.
Before the door you choose is opened, another door with a goat is opened:
{}
You can choose to either open the door you originally picked or swap
to the other unopened door.

It may seem like it doesn't matter if you swap or not, but your odds
do improve if you swap doors! This program demonstrates the Monty Hall
problem by letting you do repeated experiments.

You can read an explanation of why swapping is better at
https://en.wikipedia.org/wiki/Monty_Hall_problem
'''.format(ALL_CLOSED, THIRD_GOAT))

input('Press Enter to start...')


swapWins = 0
swapLosses = 0
stayWins = 0
stayLosses = 0
while True:  # 主程序循环。
    # 电脑选择哪一扇门有汽车:
    doorThatHasCar = random.randint(1, 3)

    # 让玩家选择一扇门：
    print(ALL_CLOSED)
    while True:  # 不断询问玩家，直到他们进入一个有效的门。
        print('Pick a door 1, 2, or 3 (or "quit" to stop):')
        response = input('> ').upper()
        if response == 'QUIT':
            # 结束游戏。
            print('Thanks for playing!')
            sys.exit()

        if response == '1' or response == '2' or response == '3':
            break
    doorPick = int(response)

    # 找出该向玩家呈现的山羊门:
    while True:
        # 选择一扇未被玩家选中的山羊门:
        showGoatDoor = random.randint(1, 3)
        if showGoatDoor != doorPick and showGoatDoor != doorThatHasCar:
            break

    # 向玩家展示山羊门:
    if showGoatDoor == 1:
        print(FIRST_GOAT)
    elif showGoatDoor == 2:
        print(SECOND_GOAT)
    elif showGoatDoor == 3:
        print(THIRD_GOAT)

    print('Door {} contains a goat!'.format(showGoatDoor))

    # 询问玩家是否想要交换:
    while True:  # 一直问下去，直到玩家选择Y或N。
        print('Do you want to swap doors? Y/N')
        swap = input('> ').upper()
        if swap == 'Y' or swap == 'N':
            break

    # 如果他们想交换，交换玩家的门:
    if swap == 'Y':
        if doorPick == 1 and showGoatDoor == 2:
            doorPick = 3
        elif doorPick == 1 and showGoatDoor == 3:
            doorPick = 2
        elif doorPick == 2 and showGoatDoor == 1:
            doorPick = 3
        elif doorPick == 2 and showGoatDoor == 3:
            doorPick = 1
        elif doorPick == 3 and showGoatDoor == 1:
            doorPick = 2
        elif doorPick == 3 and showGoatDoor == 2:
            doorPick = 1

    # 打开所有的门:
    if doorThatHasCar == 1:
        print(FIRST_CAR_OTHERS_GOAT)
    elif doorThatHasCar == 2:
        print(SECOND_CAR_OTHERS_GOAT)
    elif doorThatHasCar == 3:
        print(THIRD_CAR_OTHERS_GOAT)

    print('Door {} has the car!'.format(doorThatHasCar))

    # 交换和不交换的胜与负记录:
    if doorPick == doorThatHasCar:
        print('You won!')
        if swap == 'Y':
            swapWins += 1
        elif swap == 'N':
            stayWins += 1
    else:
        print('Sorry, you lost.')
        if swap == 'Y':
            swapLosses += 1
        elif swap == 'N':
            stayLosses += 1

    # 计算交换和不交换的成功率:
    totalSwaps = swapWins + swapLosses
    if totalSwaps != 0:  #防止零分割错误。
        swapSuccess = round(swapWins / totalSwaps * 100, 1)
    else:
        swapSuccess = 0.0

    totalStays = stayWins + stayLosses
    if (stayWins + stayLosses) != 0:  # 防止除数为0.
        staySuccess = round(stayWins / totalStays * 100, 1)
    else:
        staySuccess = 0.0

    print()
    print('Swapping:     ', end='')
    print('{} wins, {} losses, '.format(swapWins, swapLosses), end='')
    print('success rate {}%'.format(swapSuccess))
    print('Not swapping: ', end='')
    print('{} wins, {} losses, '.format(stayWins, stayLosses), end='')
    print('success rate {}%'.format(staySuccess))
    print()
    input('Press Enter repeat the experiment...')
