"""石头，剪刀，布，作者：Al Sweigart al@inventwithpython.com
经典的关于幸运的手游。
此代码可在https://nostarch.com/big-book-small-python-programming获得
标签:短,游戏"""

import random, time, sys

print('''Rock, Paper, Scissors, by Al Sweigart al@inventwithpython.com
- Rock beats scissors.
- Paper beats rocks.
- Scissors beats paper.
''')

# 这些变量记录了胜利、失败和平局的数量。
wins = 0
losses = 0
ties = 0

while True:  # 主游戏循环。
    while True:  # 一直问，直到玩家进入R, P, S或Q。
        print('{} Wins, {} Losses, {} Ties'.format(wins, losses, ties))
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
        playerMove = 'ROCK'
    elif playerMove == 'P':
        print('PAPER versus...')
        playerMove = 'PAPER'
    elif playerMove == 'S':
        print('SCISSORS versus...')
        playerMove = 'SCISSORS'

    # 数到三，然后戏剧性地停顿一下:
    time.sleep(0.5)
    print('1...')
    time.sleep(0.25)
    print('2...')
    time.sleep(0.25)
    print('3...')
    time.sleep(0.25)

    # 显示什么计算机选择:
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'ROCK'
    elif randomNumber == 2:
        computerMove = 'PAPER'
    elif randomNumber == 3:
        computerMove = 'SCISSORS'
    print(computerMove)
    time.sleep(0.5)

    # 显示和记录赢/输/平:
    if playerMove == computerMove:
        print('It\'s a tie!')
        ties = ties + 1
    elif playerMove == 'ROCK' and computerMove == 'SCISSORS':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'PAPER' and computerMove == 'ROCK':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'SCISSORS' and computerMove == 'PAPER':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'ROCK' and computerMove == 'PAPER':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'PAPER' and computerMove == 'SCISSORS':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'SCISSORS' and computerMove == 'ROCK':
        print('You lose!')
        losses = losses + 1
