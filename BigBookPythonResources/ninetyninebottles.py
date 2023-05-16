"""在墙上的九十九瓶牛奶 ，作者:Al Sweigart al@inventwithpython.com
打印最长的完整的歌词之一的歌曲! 按Ctrl-C停止。
此代码可在https://nostarch.com/big-book-small-python-programming获得
标签:微小，初学者，滚动"""

import sys, time

print('Ninety-Nine Bottles, by Al Sweigart al@inventwithpython.com')
print()
print('(Press Ctrl-C to quit.)')

time.sleep(2)

bottles = 99  # 这是起始瓶数。
PAUSE = 2  # (!) 试着将其更改为0，以便立即看到完整的歌曲。

try:
    while bottles > 1:  # Keep looping and display the lyrics.
        print(bottles, 'bottles of milk on the wall,')
        time.sleep(PAUSE)  # 因为为暂停数秒暂停
        print(bottles, 'bottles of milk,')
        time.sleep(PAUSE)
        print('Take one down, pass it around,')
        time.sleep(PAUSE)
        bottles = bottles - 1  # 减少一瓶的数量。
        print(bottles, 'bottles of milk on the wall!')
        time.sleep(PAUSE)
        print()  # 打印一个换行符。

    # 显示最后一节:
    print('1 bottle of milk on the wall,')
    time.sleep(PAUSE)
    print('1 bottle of milk,')
    time.sleep(PAUSE)
    print('Take it down, pass it around,')
    time.sleep(PAUSE)
    print('No more bottles of milk on the wall!')
except KeyboardInterrupt:
    sys.exit()  # 按下Ctrl-C后，结束程序。
