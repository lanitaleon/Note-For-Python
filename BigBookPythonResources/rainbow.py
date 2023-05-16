"""彩虹, 作者：Al Sweigart al@inventwithpython.com
显示一个简单的彩虹动画。按Ctrl-C停止。
此代码可在https://nostarch.com/big-book-small-python-programming获得
标签:微小，艺术，bext，初学者，滚动"""

import time, sys

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

print('Rainbow, by Al Sweigart al@inventwithpython.com')
print('Press Ctrl-C to stop.')
time.sleep(3)

indent = 0  # 要缩进多少个空格。
indentIncreasing = True  # 压痕是否增大。

try:
    while True:  # 主程序循环。
        print(' ' * indent, end='')
        bext.fg('red')
        print('##', end='')
        bext.fg('yellow')
        print('##', end='')
        bext.fg('green')
        print('##', end='')
        bext.fg('blue')
        print('##', end='')
        bext.fg('cyan')
        print('##', end='')
        bext.fg('purple')
        print('##')

        if indentIncreasing:
            # 增加空间数量:
            indent = indent + 1
            if indent == 60:  # (!) 把这个改为10或30。
                # 改变方向:
                indentIncreasing = False
        else:
            # 减少空间的数量:
            indent = indent - 1
            if indent == 0:
                # 改变方向:
                indentIncreasing = True

        time.sleep(0.02)  # 添加一个轻微的停顿。
except KeyboardInterrupt:
    sys.exit()  # 按下Ctrl-C后，结束程序
