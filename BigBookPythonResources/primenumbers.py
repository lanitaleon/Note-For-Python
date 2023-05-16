"""质数, 作者：Al Sweigart al@inventwithpython.com
计算质数，质数是只能被1和质数整除的数。 它们被用于各种实际应用中。
更多信息在https://en.wikipedia.org/wiki/Prime_number获得
此代码可在 https://nostarch.com/big-book-small-python-programming获得
标签:微小，数学，滚动"""

import math, sys

def main():
    print('Prime Numbers, by Al Sweigart al@inventwithpython.com')
    print('Prime numbers are numbers that are only evenly divisible by')
    print('one and themselves. They are used in a variety of practical')
    print('applications, but cannot be predicted. They must be')
    print('calculated one at a time.')
    print()
    while True:
        print('Enter a number to start searching for primes from:')
        print('(Try 0 or 1000000000000 (12 zeros) or another number.)')
        response = input('> ')
        if response.isdecimal():
            num = int(response)
            break

    input('Press Ctrl-C at any time to quit. Press Enter to begin...')

    while True:
        # 打印任何质数:
        if isPrime(num):
            print(str(num) + ', ', end='', flush=True)
        num = num + 1  # 看下一个数字。


def isPrime(number):
    """如果数字是质数则返回True，否则返回False。"""
    # 处理特殊情况:
    if number < 2:
        return False
    elif number == 2:
        return True

    #试着把数除以从2到数的平方根的所有数。
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


# 如果程序运行(而不是导入)，运行游戏:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # 按下Ctrl-C后，结束程序。
