"""闪亮的地毯, 作者：Al Sweigart al@inventwithpython.com
展示了《闪灵》中地毯图案的镶嵌。
此代码可在https://nostarch.com/big-book-small-python-programming获得
标签:小，初学者，艺术"""

# 建立常数:
X_REPEAT = 6  # 水平镶嵌多少次。
Y_REPEAT = 4  # 垂直镶嵌多少次。

for i in range(Y_REPEAT):
    print(r'_ \ \ \_/ __' * X_REPEAT)
    print(r' \ \ \___/ _' * X_REPEAT)
    print(r'\ \ \_____/ ' * X_REPEAT)
    print(r'/ / / ___ \_' * X_REPEAT)
    print(r'_/ / / _ \__' * X_REPEAT)
    print(r'__/ / / \___' * X_REPEAT)
