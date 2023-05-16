"""DNA，作者：Al Sweigart al@inventwithpython.com
DNA双螺旋的简单动画。 按 Ctrl-C 停止。
灵感来自 matoken https://asciinema.org/a/155441
此代码可在 https://nostarch.com/big-book-small-python-programming 获得
标签：短，艺术，滚动，科学"""

import random, sys, time

PAUSE = 0.15  # (!) 尝试将其更改为 0.5 或 0.0。

# 这些是 DNA 动画的各个行：
ROWS = [
    #123456789 <- 使用它来测量空格数：
    '         ##',  # 索引 0 没有 {}。
    '        #{}-{}#',
    '       #{}---{}#',
    '      #{}-----{}#',
    '     #{}------{}#',
    '    #{}------{}#',
    '    #{}-----{}#',
    '     #{}---{}#',
    '     #{}-{}#',
    '      ##',  # 索引 9 没有 {}。
    '     #{}-{}#',
    '     #{}---{}#',
    '    #{}-----{}#',
    '    #{}------{}#',
    '     #{}------{}#',
    '      #{}-----{}#',
    '       #{}---{}#',
    '        #{}-{}#']
    #123456789 <- 使用它来测量空格数：

try:
    print('DNA Animation, by Al Sweigart al@inventwithpython.com')
    print('Press Ctrl-C to quit...')
    time.sleep(2)
    rowIndex = 0

    while True:  # 主程序循环。
        # 增加 rowIndex 以绘制下一行：
        rowIndex = rowIndex + 1
        if rowIndex == len(ROWS):
            rowIndex = 0

        # 行索引 0 和 9 没有核苷酸：
        if rowIndex == 0 or rowIndex == 9:
            print(ROWS[rowIndex])
            continue

        # 选择随机核苷酸对，鸟嘌呤-胞嘧啶和
        # 腺嘌呤胸腺嘧啶：
        randomSelection = random.randint(1, 4)
        if randomSelection == 1:
            leftNucleotide, rightNucleotide = 'A', 'T'
        elif randomSelection == 2:
            leftNucleotide, rightNucleotide = 'T', 'A'
        elif randomSelection == 3:
            leftNucleotide, rightNucleotide = 'C', 'G'
        elif randomSelection == 4:
            leftNucleotide, rightNucleotide = 'G', 'C'

        # 打印行。
        print(ROWS[rowIndex].format(leftNucleotide, rightNucleotide))
        time.sleep(PAUSE)  # 添加一个轻微的停顿。
except KeyboardInterrupt:
    sys.exit()  # 当按下 Ctrl-C 时，结束程序。
