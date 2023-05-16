"""珠算日本算盘, 作者：Al Sweigart al@inventwithpython.com
A simulation of a Japanese abacus calculator tool.
更多信息可在https://en.wikipedia.org/wiki/Soroban获得
此代码可在https://nostarch.com/big-book-small-python-programming获得
标签:大型，艺术，数学，模拟"""

NUMBER_OF_DIGITS = 10


def main():
    print('Soroban - The Japanese Abacus')
    print('By Al Sweigart al@inventwithpython.com')
    print()

    abacusNumber = 0  # 这是算盘上的数字。

    while True:  # 主程序循环：
        displayAbacus(abacusNumber)
        displayControls()

        commands = input('> ')
        if commands == 'quit':
            # 退出这个程序：
            break
        elif commands.isdecimal():
            # 设置算盘数:
            abacusNumber = int(commands)
        else:
            # 处理递增/递减命令:
            for letter in commands:
                if letter == 'q':
                    abacusNumber += 1000000000
                elif letter == 'a':
                    abacusNumber -= 1000000000
                elif letter == 'w':
                    abacusNumber += 100000000
                elif letter == 's':
                    abacusNumber -= 100000000
                elif letter == 'e':
                    abacusNumber += 10000000
                elif letter == 'd':
                    abacusNumber -= 10000000
                elif letter == 'r':
                    abacusNumber += 1000000
                elif letter == 'f':
                    abacusNumber -= 1000000
                elif letter == 't':
                    abacusNumber += 100000
                elif letter == 'g':
                    abacusNumber -= 100000
                elif letter == 'y':
                    abacusNumber += 10000
                elif letter == 'h':
                    abacusNumber -= 10000
                elif letter == 'u':
                    abacusNumber += 1000
                elif letter == 'j':
                    abacusNumber -= 1000
                elif letter == 'i':
                    abacusNumber += 100
                elif letter == 'k':
                    abacusNumber -= 100
                elif letter == 'o':
                    abacusNumber += 10
                elif letter == 'l':
                    abacusNumber -= 10
                elif letter == 'p':
                    abacusNumber += 1
                elif letter == ';':
                    abacusNumber -= 1

        # 算盘不能显示负数:
        if abacusNumber < 0:
            abacusNumber = 0  # 将任何负数改为0。
        # 算盘不能显示大于9999999999的数字:
        if abacusNumber > 9999999999:
            abacusNumber = 9999999999


def displayAbacus(number):
    numberList = list(str(number).zfill(NUMBER_OF_DIGITS))

    hasBead = []  # ：每个珠子位置包含True或False。

    # 上面的天堂排有一颗珠子代表数字0、1、2、3和4。
    for i in range(NUMBER_OF_DIGITS):
        hasBead.append(numberList[i] in '01234')

    # 底部天堂排有珠子的数字5,6,7,8，和9。
    for i in range(NUMBER_OF_DIGITS):
        hasBead.append(numberList[i] in '56789')

    # 最上面的一行有一个珠子，表示除0以外的所有数字。
    for i in range(NUMBER_OF_DIGITS):
        hasBead.append(numberList[i] in '12346789')

    # 第二行有一个珠子代表数字2、3、4、7、8和9。
    for i in range(NUMBER_OF_DIGITS):
        hasBead.append(numberList[i] in '234789')

    # 第三行有一个珠子表示数字0、3、4、5、8和9。
    for i in range(NUMBER_OF_DIGITS):
        hasBead.append(numberList[i] in '034589')

    # 第4行有一个珠子，表示数字0、1、2、4、5、6和9。
    for i in range(NUMBER_OF_DIGITS):
        hasBead.append(numberList[i] in '014569')

    # 第5行有一个珠子，表示数字0, 1, 2, 5, 6,和7。
    for i in range(NUMBER_OF_DIGITS):
        hasBead.append(numberList[i] in '012567')

    # 第6行有一个珠子，表示数字0, 1, 2, 3, 5, 6, 7,和8。
    for i in range(NUMBER_OF_DIGITS):
        hasBead.append(numberList[i] in '01235678')

    # 将这些True或False值转换为O或|字符。
    abacusChar = []
    for i, beadPresent in enumerate(hasBead):
        if beadPresent:
            abacusChar.append('O')
        else:
            abacusChar.append('|')

    # 用O/|字符画算盘。
    chars = abacusChar + numberList
    print("""
+================================+
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
I  |  |  |  |  |  |  |  |  |  |  I
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
+================================+
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
+=={}=={}=={}=={}=={}=={}=={}=={}=={}=={}==+""".format(*chars))


def displayControls():
    print('  +q  w  e  r  t  y  u  i  o  p')
    print('  -a  s  d  f  g  h  j  k  l  ;')
    print('(Enter a number, "quit", or a stream of up/down letters.)')


if __name__ == '__main__':
    main()
