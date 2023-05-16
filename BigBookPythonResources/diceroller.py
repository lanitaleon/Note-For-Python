"""掷骰子，作者：Al Sweigart al@inventwithpython.com
使用 Dungeons & Dragons 掷骰符号模拟掷骰子。
此代码可在 https://nostarch.com/big-book-small-python-programming 获得
标签：短，模拟"""

import random, sys

print('''Dice Roller, by Al Sweigart al@inventwithpython.com

Enter what kind and how many dice to roll. The format is the number of
dice, followed by "d", followed by the number of sides the dice have.
You can also add a plus or minus adjustment.

Examples:
  3d6 rolls three 6-sided dice
  1d10+2 rolls one 10-sided die, and adds 2
  2d38-1 rolls two 38-sided die, and subtracts 1
  QUIT quits the program
''')

while True:  # 主程序循环：
    try:
        diceStr = input('> ')  # 输入骰子串的提示。
        if diceStr.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        # 清理骰子串：
        diceStr = diceStr.lower().replace(' ', '')

        # 在骰子字符串输入中找到“d”：
        dIndex = diceStr.find('d')
        if dIndex == -1:
            raise Exception('Missing the "d" character.')

        # 获取骰子的数量。 （“3d6+1”中的“3”）：
        numberOfDice = diceStr[:dIndex]
        if not numberOfDice.isdecimal():
            raise Exception('Missing the number of dice.')
        numberOfDice = int(numberOfDice)

        # 查找修饰符是否有加号或减号：
        modIndex = diceStr.find('+')
        if modIndex == -1:
            modIndex = diceStr.find('-')

        # 求面数。 （“3d6+1”中的“6”）：
        if modIndex == -1:
            numberOfSides = diceStr[dIndex + 1 :]
        else:
            numberOfSides = diceStr[dIndex + 1 : modIndex]
        if not numberOfSides.isdecimal():
            raise Exception('Missing the number of sides.')
        numberOfSides = int(numberOfSides)

        # 找到修改量。 （“3d6+1”中的“1”）：
        if modIndex == -1:
            modAmount = 0
        else:
            modAmount = int(diceStr[modIndex + 1 :])
            if diceStr[modIndex] == '-':
                # 将修改量改为负数：
                modAmount = -modAmount

        # 模拟掷骰子：
        rolls = []
        for i in range(numberOfDice):
            rollResult = random.randint(1, numberOfSides)
            rolls.append(rollResult)

        # 显示总数：
        print('Total:', sum(rolls) + modAmount, '(Each die:', end='')

        # 显示单个点数：
        for i, roll in enumerate(rolls):
            rolls[i] = str(roll)
        print(', '.join(rolls), end='')

        # 显示修改量：
        if modAmount != 0:
            modSign = diceStr[modIndex]
            print(', {}{}'.format(modSign, abs(modAmount)), end='')
        print(')')

    except Exception as exc:
        # 捕获任何异常并向用户显示消息：
        print('Invalid input. Enter something like "3d6" or "1d10+2".')
        print('Input was invalid because: ' + str(exc))
        continue  # 返回骰子串提示。
