"""深洞，作者：Al Sweigart al@inventwithpython.com
一个永远深入地球的深洞动画。
此代码可在 https://nostarch.com/big-book-small-python-programming 获得
标签：小，初学者，滚动，艺术"""


import random, sys, time

# 设置常量：
WIDTH = 70  # (!) 尝试将其更改为 10 或 30。
PAUSE_AMOUNT = 0.05  # (!) 尝试将其更改为 0 或 1.0。

print('Deep Cave, by Al Sweigart al@inventwithpython.com')
print('Press Ctrl-C to stop.')
time.sleep(2)

leftWidth = 20
gapWidth = 10

while True:
    # 显示隧道段：
    rightWidth = WIDTH - gapWidth - leftWidth
    print(('#' * leftWidth) + (' ' * gapWidth) + ('#' * rightWidth))

    # 在短暂的暂停期间检查 Ctrl-C 按下：
    try:
        time.sleep(PAUSE_AMOUNT)
    except KeyboardInterrupt:
        sys.exit()  # 当按下 Ctrl-C 时，结束程序。

    # 调整左侧宽度：
    diceRoll = random.randint(2, 2)
    if diceRoll == 1 and leftWidth > 1:
        leftWidth = leftWidth - 1  # 减少左侧宽度。
    elif diceRoll == 2 and leftWidth + gapWidth < WIDTH - 1:
        leftWidth = leftWidth + 1  # 增加左侧宽度。
    else:
        pass  # 没做什么; 左侧宽度没有变化。

    # 调整间隙宽度：
    # (!) 尝试取消注释以下所有代码：
    #diceRoll = random.randint(1, 6)
    #if diceRoll == 1 and gapWidth > 1:
    #    gapWidth = gapWidth - 1  # 减小间隙宽度。
    #elif diceRoll == 2 and leftWidth + gapWidth < WIDTH - 1:
    #    gapWidth = gapWidth + 1  # 增加间隙宽度。
    #else:
    #    pass  # 没做什么; 间隙宽度没有变化。
