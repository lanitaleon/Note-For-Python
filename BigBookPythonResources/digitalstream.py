"""数字流，作者：Al Sweigart al@inventwithpython.com
黑客帝国电影视觉风格的屏幕保护程序。
此代码可在 https://nostarch.com/big-book-small-python-programming 获得
标签：小，艺术，初学者，滚动"""

import random, shutil, sys, time

# 设置常量：
MIN_STREAM_LENGTH = 6  # (!) 尝试将其更改为 1 或 50。
MAX_STREAM_LENGTH = 14  # (!) 尝试将其更改为 100。
PAUSE = 0.1  # (!) 尝试将其更改为 0.0 或 2.0。
STREAM_CHARS = ['0', '1']  # (!) 尝试将其更改为其他字符。

# 密度范围从 0.0 到 1.0：
DENSITY = 0.02  # (!) 尝试将其更改为 0.10 或 0.30。

# 获取终端窗口的大小：
WIDTH = shutil.get_terminal_size()[0]
# 我们无法在 Windows 上打印到最后一列而不添加
# 自动换行，所以宽度减一：
WIDTH -= 1

print('Digital Stream, by Al Sweigart al@inventwithpython.com')
print('Press Ctrl-C to quit.')
time.sleep(2)

try:
    # 对于每一列，当计数器为0时，不显示流。
    # 否则，它将作为 1 或 0
    # 应该显示在该列中多少次的计数器。
    columns = [0] * WIDTH
    while True:
        # 为每一列设置计数器：
        for i in range(WIDTH):
            if columns[i] == 0:
                if random.random() <= DENSITY:
                    # 重新启动此列上的流。
                    columns[i] = random.randint(MIN_STREAM_LENGTH,
                                                MAX_STREAM_LENGTH)

            # 显示一个空格或一个 1/0 字符。
            if columns[i] > 0:
                print(random.choice(STREAM_CHARS), end='')
                columns[i] -= 1
            else:
                print(' ', end='')
        print()  # 在列行的末尾打印一个换行符。
        sys.stdout.flush()  # 确保文本出现在屏幕上。
        time.sleep(PAUSE)
except KeyboardInterrupt:
    sys.exit()  # 当按下 Ctrl-C 时，结束程序。
