"""幸运星, 作者：Al Sweigart al@inventwithpython.com
这是一款“碰运气”游戏，你可以通过掷骰子来收集尽可能多的星星。
你想掷多少次都可以，但如果你掷了三个头骨，你就失去了所有的星星。

灵感来自史蒂夫杰克逊游戏的僵尸骰子游戏。
此代码可在https://nostarch.com/big-book-small-python-programming获得
标签:大型，游戏，多人游戏"""

import random

# 建立常数:
GOLD = 'GOLD'
SILVER = 'SILVER'
BRONZE = 'BRONZE'

STAR_FACE = ["+-----------+",
             "|     .     |",
             "|    ,O,    |",
             "| 'ooOOOoo' |",
             "|   `OOO`   |",
             "|   O' 'O   |",
             "+-----------+"]
SKULL_FACE = ['+-----------+',
              '|    ___    |',
              '|   /   \\   |',
              '|  |() ()|  |',
              '|   \\ ^ /   |',
              '|    VVV    |',
              '+-----------+']
QUESTION_FACE = ['+-----------+',
                 '|           |',
                 '|           |',
                 '|     ?     |',
                 '|           |',
                 '|           |',
                 '+-----------+']
FACE_WIDTH = 13
FACE_HEIGHT = 7

print("""Lucky Stars, by Al Sweigart al@inventwithpython.com

A "press your luck" game where you roll dice with Stars, Skulls, and
Question Marks.

On your turn, you pull three random dice from the dice cup and roll
them. You can roll Stars, Skulls, and Question Marks. You can end your
turn and get one point per Star. If you choose to roll again, you keep
the Question Marks and pull new dice to replace the Stars and Skulls.
If you collect three Skulls, you lose all your Stars and end your turn.

When a player gets 13 points, everyone else gets one more turn before
the game ends. Whoever has the most points wins.

There are 6 Gold dice, 4 Silver dice, and 3 Bronze dice in the cup.
Gold dice have more Stars, Bronze dice have more Skulls, and Silver is
even.
""")

print('How many players are there?')
while True:  # 循环，直到用户输入一个数字。
    response = input('> ')
    if response.isdecimal() and int(response) > 1:
        numPlayers = int(response)
        break
    print('Please enter a number larger than 1.')

playerNames = []  # 球员名字的字符串列表。
playerScores = {}  # 键是玩家的名字，值是整数分数。
for i in range(numPlayers):
    while True:  # 继续循环，直到输入一个名称。
        print('What is player #' + str(i + 1) + '\'s name?')
        response = input('> ')
        if response != '' and response not in playerNames:
            playerNames.append(response)
            playerScores[response] = 0
            break
        print('Please enter a name.')
print()

turn = 0  # 在playerNames[0]的玩家将首先出场。
# (!) 取消注释，让名为“Al”的玩家以3分开始:
#playerScores['Al'] = 3
endGameWith = None
while True:  # Main game loop.
    # 显示每个人的分数:
    print()
    print('SCORES: ', end='')
    for i, name in enumerate(playerNames):
        print(name + ' = ' + str(playerScores[name]), end='')
        if i != len(playerNames) - 1:
            # 除了最后一个选手，所有选手的名字之间都用逗号隔开。
            print(', ', end='')
    print('\n')

    # 从0开始收集星星和头骨。
    stars = 0
    skulls = 0
    # 一个杯子有6个金的，4个银的，3个铜骰子:
    cup = ([GOLD] * 6) + ([SILVER] * 4) + ([BRONZE] * 3)
    hand = []  # 你的手一开始没有骰子。
    print('It is ' + playerNames[turn] + '\'s turn.')
    while True:  # 这个循环的每次迭代都是在掷骰子。
        print()

        # 检查是否有足够的骰子留在杯子里:
        if (3 - len(hand)) > len(cup):
            # 因为没有足够的骰子，结束这一回合:
            print('There aren\'t enough dice left in the cup to '
                + 'continue ' + playerNames[turn] + '\'s turn.')
            break

        # 从杯子中取骰子，直到有3在你的手:
        random.shuffle(cup)  # 在杯子中摇骰子
        while len(hand) < 3:
            hand.append(cup.pop())

        # 掷骰子:
        rollResults = []
        for dice in hand:
            roll = random.randint(1, 6)
            if dice == GOLD:
                # 掷出一个金骰子(3颗星，2个问题，1个骷髅)
                if 1 <= roll <= 3:
                    rollResults.append(STAR_FACE)
                    stars += 1
                elif 4 <= roll <= 5:
                    rollResults.append(QUESTION_FACE)
                else:
                    rollResults.append(SKULL_FACE)
                    skulls += 1
            if dice == SILVER:
                # 掷一个银骰子(2颗星，2个问题，2个头骨):
                if 1 <= roll <= 2:
                    rollResults.append(STAR_FACE)
                    stars += 1
                elif 3 <= roll <= 4:
                    rollResults.append(QUESTION_FACE)
                else:
                    rollResults.append(SKULL_FACE)
                    skulls += 1
            if dice == BRONZE:
                # 掷一个铜骰子(1颗星，2个问题，3个头骨)
                if roll == 1:
                    rollResults.append(STAR_FACE)
                    stars += 1
                elif 2 <= roll <= 4:
                    rollResults.append(QUESTION_FACE)
                else:
                    rollResults.append(SKULL_FACE)
                    skulls += 1

        # 显示掷出的骰子：
        for lineNum in range(FACE_HEIGHT):
            for diceNum in range(3):
                print(rollResults[diceNum][lineNum] + ' ', end='')
            print()  # 输出一个换行符。

        # 展示每个骰子的类型(金，银，铜):
        for diceType in hand:
            print(diceType.center(FACE_WIDTH) + ' ', end='')
        print()  # 输出一个换行符。

        print('Stars collected:', stars, '  Skulls collected:', skulls)

        # 检查他们是否收集了3个或更多的头骨:
        if skulls >= 3:
            print('3 or more skulls means you\'ve lost your stars!')
            input('Press Enter to continue...')
            break

        print(playerNames[turn] + ', do you want to roll again? Y/N')
        while True:  # 一直问玩家，直到他们进入Y或N:
            response = input('> ').upper()
            if response != '' and response[0] in ('Y', 'N'):
                break
            print('Please enter Yes or No.')

        if response.startswith('N'):
            print(playerNames[turn], 'got', stars, 'stars!')
            # 将星星添加到这个玩家的积分总数
            playerScores[playerNames[turn]] += stars

            # 如果他们已经达到13分或更多:
            # (!) 试着把它改成5点或50点。
            if (endGameWith == None
                and playerScores[playerNames[turn]] >= 13):
                # 由于这名球员达到13分，再玩一轮的所有其他球员:
                print('\n\n' + ('!' * 60))
                print(playerNames[turn] + ' has reached 13 points!!!')
                print('Everyone else will get one more turn!')
                print(('!' * 60) + '\n\n')
                endGameWith = playerNames[turn]
            input('Press Enter to continue...')
            break

        # 去掉星星和头骨，但保留问号:
        nextHand = []
        for i in range(3):
            if rollResults[i] == QUESTION_FACE:
                nextHand.append(hand[i])  # Keep the question marks.
        hand = nextHand

    # 继续下一个玩家的回合:
    turn = (turn + 1) % numPlayers

    # 如果游戏已经结束，打破这个循环:
    if endGameWith == playerNames[turn]:
        break  # 结束游戏。

print('The game has ended...')

# 显示每个玩家的分数：
print()
print('SCORES: ', end='')
for i, name in enumerate(playerNames):
    print(name + ' = ' + str(playerScores[name]), end='')
    if i != len(playerNames) - 1:
        # 除了最后一个选手，所有选手的名字之间都用逗号隔开。
        print(', ', end='')
print('\n')

# 看看谁是赢家:
highestScore = 0
winners = []
for name, score in playerScores.items():
    if score > highestScore:
        # 此玩家得分最高:
        highestScore = score
        winners = [name]  # 覆盖以前所有的赢家。
    elif score == highestScore:
        # 这名选手与最高分持平。
        winners.append(name)

if len(winners) == 1:
    # 只有一个赢家:
    print('The winner is ' + winners[0] + '!!!')
else:
    # 有多个并列的获胜者:
    print('The winners are: ' + ', '.join(winners))

print('Thanks for playing!')
