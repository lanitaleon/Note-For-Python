"""斐波那契数列，作者：Al Sweigart al@inventwithpython.com
计算斐波那契数列的数字：0, 1, 1, 2, 3, 5, 8, 13...
此代码可在 https://nostarch.com/big-book-small-python-programming 获得
标签：短，数学"""

import sys

print('''Fibonacci Sequence, by Al Sweigart al@inventwithpython.com

The Fibonacci sequence begins with 0 and 1, and the next number is the
sum of the previous two numbers. The sequence continues forever:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987...
''')

while True:  # 主程序循环。
    while True:  # 一直询问直到用户输入有效的输入。
        print('Enter the Nth Fibonacci number you wish to')
        print('calculate (such as 5, 50, 1000, 9999), or QUIT to quit:')
        response = input('> ').upper()

        if response == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        if response.isdecimal() and int(response) != 0:
            nth = int(response)
            break  # 当用户输入有效数字时退出循环。

        print('Please enter a number greater than 0, or QUIT.')
    print()

    # 如果用户输入 1 或 2，则处理特殊情况：
    if nth == 1:
        print('0')
        print()
        print('The #1 Fibonacci number is 0.')
        continue
    elif nth == 2:
        print('0, 1')
        print()
        print('The #2 Fibonacci number is 1.')
        continue

    # 如果用户输入了大量数字，则显示警告：
    if nth >= 10000:
        print('WARNING: This will take a while to display on the')
        print('screen. If you want to quit this program before it is')
        print('done, press Ctrl-C.')
        input('Press Enter to begin...')

    # 计算第 N 个斐波那契数：
    secondToLastNumber = 0
    lastNumber = 1
    fibNumbersCalculated = 2
    print('0, 1, ', end='')  # 显示前两个斐波那契数。

    # 显示斐波那契数列后面的所有数字：
    while True:
        nextNumber = secondToLastNumber + lastNumber
        fibNumbersCalculated += 1

        # 显示序列中的下一个数字：
        print(nextNumber, end='')

        # 检查我们是否找到了用户想要的第 N 个数字：
        if fibNumbersCalculated == nth:
            print()
            print()
            print('The #', fibNumbersCalculated, ' Fibonacci ',
                  'number is ', nextNumber, sep='')
            break

        # 在序列号之间打印一个逗号：
        print(', ', end='')

        # 移动最后两个数字：
        secondToLastNumber = lastNumber
        lastNumber = nextNumber
