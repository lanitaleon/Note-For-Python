"""九九乘法表, 作者：Al Sweigart al@inventwithpython.com
打印乘法表。
此代码可在https://nostarch.com/big-book-small-python-programming获得
标签:小，初学，数学"""

print('Multiplication Table, by Al Sweigart al@inventwithpython.com')

# 打印水平数字标签:
print('  |  0   1   2   3   4   5   6   7   8   9  10  11  12')
print('--+---------------------------------------------------')

# 展示每一行结果:
for number1 in range(0, 13):

    # 打印垂直数字标签:
    print(str(number1).rjust(2), end='')

    # P打印一个分隔条:
    print('|', end='')

    for number2 in range(0, 13):
        # 打印结果后跟一个空格:
        print(str(number1 * number2).rjust(3), end=' ')

    print()  # 打印一个换行符来完成这一行。
