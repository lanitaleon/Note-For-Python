"""曹韩，作者：Al Sweigart al@inventwithpython.com
日本传统的奇偶骰子游戏。
在 https://nostarch.com/big-book-small-python-projects 查看此代码
标签：简短，初学者，游戏"""

import random, sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                    4: 'SHI', 5: 'GO', 6: 'ROKU'}

print('''Cho-Han, by Al Sweigart al@inventwithpython.com

In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.
''')

purse = 5000
while True:  # 主游戏循环。
    # 请下注：
    print('You have', purse, 'mon. How much do you bet? (or QUIT)')
    while True:
        pot = input('> ')
        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > purse:
            print('You do not have enough to make that bet.')
        else:
            # 这是一个有效的赌注。
            pot = int(pot)  # 将pot转换为整数。
            break  # 下注有效后退出循环。

    # 掷骰子。
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the')
    print('dice and asks for your bet.')
    print()
    print('    CHO (even) or HAN (odd)?')

    # 让玩家下注 cho 或 han：
    while True:
        bet = input('> ').upper()
        if bet != 'CHO' and bet != 'HAN':
            print('Please enter either "CHO" or "HAN".')
            continue
        else:
            break

    # 显示骰子结果：
    print('The dealer lifts the cup to reveal:')
    print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print('    ', dice1, '-', dice2)

    # 确定玩家是否获胜：
    rollIsEven = (dice1 + dice2) % 2 == 0
    if rollIsEven:
        correctBet = 'CHO'
    else:
        correctBet = 'HAN'

    playerWon = bet == correctBet

    # 显示投注结果：
    if playerWon:
        print('You won! You take', pot, 'mon.')
        purse = purse + pot  # 从玩家的钱包中添加pot。
        print('The house collects a', pot // 10, 'mon fee.')
        purse = purse - (pot // 10)  # 房屋费为10%。
    else:
        purse = purse - pot  # 从玩家的钱包中减去pot。
        print('You lost!')

    # 检查玩家是否已经用完钱：
    if purse == 0:
        print('You have run out of money!')
        print('Thanks for playing!')
        sys.exit()
