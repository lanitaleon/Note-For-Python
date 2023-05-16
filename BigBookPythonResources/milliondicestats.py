"""百万骰子滚动统计模拟器
作者：Al Sweigart al@inventwithpython.com
模拟掷一百万个骰子。
此代码可在https://nostarch.com/big-book-small-python-programming获得
标签:微小，初学者，数学，模拟"""

import random, time

print('''Million Dice Roll Statistics Simulator
By Al Sweigart al@inventwithpython.com

Enter how many six-sided dice you want to roll:''')
numberOfDice = int(input('> '))

# 设置一个字典来存储每次掷骰子的结果:
results = {}
for i in range(numberOfDice, (numberOfDice * 6) + 1):
    results[i] = 0

# 模拟掷骰子:
print('Simulating 1,000,000 rolls of {} dice...'.format(numberOfDice))
lastPrintTime = time.time()
for i in range(1000000):
    if time.time() > lastPrintTime + 1:
        print('{}% done...'.format(round(i / 10000, 1)))
        lastPrintTime = time.time()

    total = 0
    for j in range(numberOfDice):
        total = total + random.randint(1, 6)
    results[total] = results[total] + 1

# 显示结果：
print('TOTAL - ROLLS - PERCENTAGE')
for i in range(numberOfDice, (numberOfDice * 6) + 1):
    roll = results[i]
    percentage = round(results[i] / 10000, 1)
    print('  {} - {} rolls - {}%'.format(i, roll, percentage))
