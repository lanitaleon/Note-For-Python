"""
百吉饼，作者：Al Sweigart al@inventwithpython.com
一个演绎逻辑游戏，您必须根据线索猜测一个数字。
此代码可在https://nostarch.com/big-book-small-python-programming获得
这个游戏的一个版本在书中有特色，“发明你自己的使用 Python 的电脑游戏” https://nostarch.com/inventwithpython
标签：短，游戏，拼图
"""

import random

NUM_DIGITS = 3  # (!) 尝试将其设置为 1 或 10。
MAX_GUESSES = 10  # (!) 尝试将其设置为 1 或 100。


def main():
    print('''Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com

I am thinking of a {}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
When I say:    That means:
  Pico         One digit is correct but in the wrong position.
  Fermi        One digit is correct and in the right position.
  Bagels       No digit is correct.

For example, if the secret number was 248 and your guess was 843, the
clues would be Fermi Pico.'''.format(NUM_DIGITS))

    while True:  # 主游戏循环。
        # 这存储了玩家需要猜测的秘密数字：
        secretNum = getSecretNum()
        print('I have thought up a number.')
        print(' You have {} guesses to get it.'.format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            # 继续循环直到他们输入一个有效的猜测：
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}: '.format(numGuesses))
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break  # 他们是对的，所以跳出这个循环。
            if numGuesses > MAX_GUESSES:
                print('You ran out of guesses.')
                print('The answer was {}.'.format(secretNum))

        # 询问玩家是否想再玩一次。
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')


def getSecretNum():
    """返回由 NUM_DIGITS 个唯一随机数字组成的字符串。"""
    numbers = list('0123456789')  # 创建数字 0 到 9 的列表。
    random.shuffle(numbers)  # 将它们随机排列。

    # 获取秘密号码列表中的前 NUM_DIGITS 位数字：
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


def getClues(guess, secretNum):
    """返回一个带有 pico、fermi、百吉饼线索的字符串，用于猜测秘密数字对。"""
    if guess == secretNum:
        return 'You got it!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # 正确的数字位于正确的位置。
            clues.append('Fermi')
        elif guess[i] in secretNum:
            # 正确的数字在不正确的地方。
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'  # 根本没有正确的数字。
    else:
        # 将线索按字母顺序排序，使其原始顺序
        # 不会泄露信息。
        clues.sort()
        # 从字符串线索列表中生成单个字符串。
        return ' '.join(clues)


# 如果程序运行（而不是导入），运行游戏：
if __name__ == '__main__':
    main()
