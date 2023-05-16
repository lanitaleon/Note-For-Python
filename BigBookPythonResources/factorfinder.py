"""因数查找器，Al Sweigart al@inventwithpython.com
求一个数的所有因数。
此代码可在https://nostarch.com/big-book-small-python-programming上找到
标签:小，初学，数学"""

import math, sys

print('''Factor Finder, by Al Sweigart al@inventwithpython.com

A number's factors are two numbers that, when multiplied with each
other, produce the number. For example, 2 x 13 = 26, so 2 and 13 are
factors of 26. 1 x 26 = 26, so 1 and 26 are also factors of 26. We
say that 26 has four factors: 1, 2, 13, and 26.

If a number only has two factors (1 and itself), we call that a prime
number. Otherwise, we call it a composite number.

Can you discover some prime numbers?
''')

while True:  # 主程序循环。
    print('Enter a positive whole number to factor (or QUIT):')
    response = input('> ')
    if response.upper() == 'QUIT':
        sys.exit()

    if not (response.isdecimal() and int(response) > 0):
        continue
    number = int(response)

    factors = ['hello']

    # 求number的因数:
    for i in range(1, int(math.sqrt(number)) + 1):
        if number % i == 0:  # 如果没有余数，它就是因数。
            factors.append(i)
            factors.append(number // i)

    # 转换为集合以去除重复因子：
    factors = list(set(factors))
    # factors.sort()

    # 显示结果：
    for i, factor in enumerate(factors):
        factors[i] = str(factor)
    print(', '.join(factors))
