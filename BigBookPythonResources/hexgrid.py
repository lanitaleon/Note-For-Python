"""六边形网格, 作者：Al Sweigart al@inventwithpython.com
显示一个六边形网格的简单镶嵌
此代码可在https://nostarch.com/big-book-small-python-programming获得
标签:微小，初学者，艺术"""

# 设置常量:
# (!) 试着将这些值为改其他数字:
X_REPEAT = 19  # 水平镶嵌多少次。
Y_REPEAT = 12  # 垂直镶嵌的次数。

for y in range(Y_REPEAT):
    # 显示六边形的上半部分:
    for x in range(X_REPEAT):
        print(r'/ \_', end='')
    print()

    # 显示六边形的下半部分:
    for x in range(X_REPEAT):
        print(r'\_/ ', end='')
    print()
