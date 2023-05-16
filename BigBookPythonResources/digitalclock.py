"""数码时钟，作者：Al Sweigart al@inventwithpython.com
显示一个数字时钟的当前时间与7段
显示。按Ctrl-C停止。
更多信息请访问 https://en.wikipedia.org/wiki/Seven-segment_display
要求 sevseg.py 位于同一文件夹中。
此代码可在 https://nostarch.com/big-book-small-python-programming 获得
标签： 小，艺术"""

import sys, time
import sevseg  # Imports our sevseg.py program.

try:
    while True:  # 主程序循环。
        # 通过打印几个换行符来清除屏幕：
        print('\n' * 60)

        # 从计算机的时钟获取当前时间：
        currentTime = time.localtime()
        # % 12 所以我们使用 12 小时制，而不是 24：
        hours = str(currentTime.tm_hour % 12)
        if hours == '0':
            hours = '12'  # 12 小时制显示的是 12:00，而不是 00:00。
        minutes = str(currentTime.tm_min)
        seconds = str(currentTime.tm_sec)

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
        print()
        print('Press Ctrl-C to quit.')

        # 继续循环直到第二个变化：
        while True:
            time.sleep(0.01)
            if time.localtime().tm_sec != currentTime.tm_sec:
                break
except KeyboardInterrupt:
    print('Digital Clock, by Al Sweigart al@inventwithpython.com')
    sys.exit()  # 当按下 Ctrl-C 时，结束程序。
