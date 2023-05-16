"""猜数字，作者：Al Sweigart al@inventwithpython.com
尝试根据提示猜测秘密数字。
此代码可在 https://nostarch.com/big-book-small-python-programming 获得
标签：小，初学者，游戏"""

import random


def askForGuess():
    while True:
        guess = input('> ')  # 输入猜测。

        if guess.isdecimal():
            return int(guess)  # 将字符串猜测转换为整数。
        print('Please enter a number between 1 and 100.')


print('Guess the Number, by Al Sweigart al@inventwithpython.com')
print()
secretNumber = random.randint(1, 100)  # 选择一个随机数。
print('I am thinking of a number between 1 and 100.')

for i in range(10):  # 给玩家 10 次猜测。
    print('You have {} guesses left. Take a guess.'.format(10 - i))

    guess = askForGuess()
    if guess == secretNumber:
        break  # 如果猜测正确，则跳出 for 循环。

    # 提供一个提示：
    if guess < secretNumber:
        print('Your guess is too low.')
    if guess > secretNumber:
        print('Your guess is too high.')

# 显示结果：
if guess == secretNumber:
    print('Yay! You guessed my number!')
else:
    print('Game over. The number I was thinking of was', secretNumber)
