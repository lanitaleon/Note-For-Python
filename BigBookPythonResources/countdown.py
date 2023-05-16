"""倒计时，作者：Al Sweigart al@inventwithpython.com
使用七段显示器显示倒数计时器动画。
按 Ctrl-C 停止。
更多信息请访问 https://en.wikipedia.org/wiki/Seven-segment_display
要求 sevseg.py 位于同一文件夹中。
此代码可在 https://nostarch.com/big-book-small-python-programming 获得
标签： 小，艺术"""

import sys, time
import sevseg  # Imports our sevseg.py program.

# (!) 将其更改为任意秒数：
secondsLeft = 30

try:
    while True:  # 主程序循环。
        # 通过打印几个换行符来清除屏幕：
        print('\n' * 60)

        # 从 secondsLeft 获取小时/分钟/秒：
        # 例如：7265 是 2 小时 1 分 5 秒。
        # 所以 7265 // 3600 是 2 小时：
        hours = str(secondsLeft // 3600)
        # 7265 % 3600 是 65，而 65 // 60 是 1 分钟：
        minutes = str((secondsLeft % 3600) // 60)
        # 7265 % 60 是 5 秒：
        seconds = str(secondsLeft % 60)

        # 从 sevseg 模块中获取数字字符串：
        hDigits = sevseg.getSevSegStr(hours, 2)
        hTopRow, hMiddleRow, hBottomRow = hDigits.splitlines()

        mDigits = sevseg.getSevSegStr(minutes, 2)
        mTopRow, mMiddleRow, mBottomRow = mDigits.splitlines()

        sDigits = sevseg.getSevSegStr(seconds, 2)
        sTopRow, sMiddleRow, sBottomRow = sDigits.splitlines()

        # 显示数字：
        print(hTopRow    + '     ' + mTopRow    + '     ' + sTopRow)
        print(hMiddleRow + '  *  ' + mMiddleRow + '  *  ' + sMiddleRow)
        print(hBottomRow + '  *  ' + mBottomRow + '  *  ' + sBottomRow)

        if secondsLeft == 0:
            print()
            print('    * * * * BOOM * * * *')
            break

        print()
        print('Press Ctrl-C to quit.')

        time.sleep(1)  # 插入一秒钟的停顿。
        secondsLeft -= 1
except KeyboardInterrupt:
    print('Countdown, by Al Sweigart al@inventwithpython.com')
    sys.exit()  # 当按下 Ctrl-C 时，结束程序。
