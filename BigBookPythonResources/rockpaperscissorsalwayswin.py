"""剪刀、石头、布(总是赢的版本)
作者：Al Sweigart al@inventwithpython.com
经典的手游运气，不过你总是赢。
此代码可在https://nostarch.com/big-book-small-python-programming获得
标签:小，游戏，幽默"""

import time, sys

print('''Rock, Paper, Scissors, by Al Sweigart al@inventwithpython.com
- Rock beats scissors.
- Paper beats rocks.
- Scissors beats paper.
''')

# 这些变量记录了胜利的数量。
wins = 0

while True:  # 主游戏循环
    while True:  # 一直问，直到玩家进入R, P, S或Q。
        print('{} Wins, 0 Losses, 0 Ties'.format(wins))
        print('Enter your move: (R)ock (P)aper (S)cissors or (Q)uit')
        playerMove = input('> ').upper()
        if playerMove == 'Q':
            print('Thanks for playing!')
            sys.exit()

        if playerMove == 'R' or playerMove == 'P' or playerMove == 'S':
            break
        else:
            print('Type one of R, P, S, or Q.')

    # 显示玩家选择的内容:
    if playerMove == 'R':
        print('ROCK versus...')
    elif playerMove == 'P':
        print('PAPER versus...')
    elif playerMove == 'S':
        print('SCISSORS versus...')

    # 数到三，然后戏剧性地停顿一下:
    time.sleep(0.5)
    print('1...')
    time.sleep(0.25)
    print('2...')
    time.sleep(0.25)
    print('3...')
    time.sleep(0.25)

    # 显示什么计算机选择:
    if playerMove == 'R':
        print('SCISSORS')
    elif playerMove == 'P':
        print('ROCK')
    elif playerMove == 'S':
        print('PAPER')

    time.sleep(0.5)

    print('You win!')
    wins = wins + 1
