"""强力球彩票,作者：Al Sweigart al@inventwithpython.com
一个模拟彩票的游戏，这样你就可以体验到输了彩票而又不浪费钱的兴奋感。
此代码可在https://nostarch.com/big-book-small-python-programming获得
标签:简短，幽默，模拟"""

import random

print('''Powerball Lottery, by Al Sweigart al@inventwithpython.com

Each powerball lottery ticket costs $2. The jackpot for this game
is $1.586 billion! It doesn't matter what the jackpot is, though,
because the odds are 1 in 292,201,338, so you won't win.

This simulation gives you the thrill of playing without wasting money.
''')

# 让玩家在1到69中选5个数输入：
while True:
    print('Enter 5 different numbers from 1 to 69, with spaces between')
    print('each number. (For example: 5 17 23 42 50)')
    response = input('> ')

    # 检查玩家是否输入了5个内容:
    numbers = response.split()
    if len(numbers) != 5:
        print('Please enter 5 numbers, separated by spaces.')
        continue

    # 将字符串转换为整数:
    try:
        for i in range(5):
            numbers[i] = int(numbers[i])
    except ValueError:
        print('Please enter numbers, like 27, 35, or 62.')
        continue

    # 检查数字是否在1到69之间:
    for i in range(5):
        if not (1 <= numbers[i] <= 69):
            print('The numbers must all be between 1 and 69.')
            continue

    # 检查数字是否唯一:
    # (从数字中创建一个集合，删除重复数字。)
    if len(set(numbers)) != 5:
        print('You must enter 5 different numbers.')
        continue

    break

# 让玩家在1到26中选择强力球:
while True:
    print('Enter the powerball number from 1 to 26.')
    response = input('> ')

    # 将字符串转换为整数:
    try:
        powerball = int(response)
    except ValueError:
        print('Please enter a number, like 3, 15, or 22.')
        continue

    # 检查数字是否在1到26之间:
    if not (1 <= powerball <= 26):
        print('The powerball number must be between 1 and 26.')
        continue

    break

# 输入你想玩游戏的次数:
while True:
    print('How many times do you want to play? (Max: 1000000)')
    response = input('> ')

    # 将字符串转换为整数:
    try:
        numPlays = int(response)
    except ValueError:
        print('Please enter a number, like 3, 15, or 22000.')
        continue

    # 检查数字是否在1到1000000之间:
    if not (1 <= numPlays <= 1000000):
        print('You can play between 1 and 1000000 times.')
        continue

    break

# 运行模拟彩票:
price = '$' + str(2 * numPlays)
print('It costs', price, 'to play', numPlays, 'times, but don\'t')
print('worry. I\'m sure you\'ll win it all back.')
input('Press Enter to start...')

possibleNumbers = list(range(1, 70))
for i in range(numPlays):
    # 想出彩票号码:
    random.shuffle(possibleNumbers)
    winningNumbers = possibleNumbers[0:5]
    winningPowerball = random.randint(1, 26)

    # 显示中奖号码:
    print('The winning numbers are: ', end='')
    allWinningNums = ''
    for i in range(5):
        allWinningNums += str(winningNumbers[i]) + ' '
    allWinningNums += 'and ' + str(winningPowerball)
    print(allWinningNums.ljust(21), end='')

    # 注意:集合是没有顺序的，
    # 所以set(numbers)和set(winningNumbers)中的整数的顺序无关紧要。
    if (set(numbers) == set(winningNumbers)
        and powerball == winningPowerball):
            print()
            print('You have won the Powerball Lottery! Congratulations,')
            print('you would be a billionaire if this was real!')
            break
    else:
        print(' You lost.')  # 这里需要前导空间。

print('You have wasted', price)
print('Thanks for playing!')
