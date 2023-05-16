"""沙漏,作者：Al Sweigart al@inventwithpython.com
一个关于沙漏中下落的沙子的动画 按 Ctrl-C 停止。
此代码可在 https://nostarch.com/big-book-small-python-programming获得
标签：大, 艺术, bext, 模拟"""

import random, sys, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# 建立常数：
PAUSE_LENGTH = 0.2  # (!) 尝试将其更改为0.0或1.0。
# (!) 试着把它改成0到100之间的任何数字:
WIDE_FALL_CHANCE = 50

SCREEN_WIDTH = 79
SCREEN_HEIGHT = 25
X = 0  # (X, y)元组中X值的下标为0。
Y = 1  # (x, Y)元组中Y值的下标为1。
SAND = chr(9617)
WALL = chr(9608)

#设置沙漏墙
HOURGLASS = set()  # 有(x, y)的元组用于沙漏墙所在的位置。
# (!) 尝试注释一些HOURGLASS.add()行来擦除墙壁:
for i in range(18, 37):
    HOURGLASS.add((i, 1))  # 为沙漏的顶盖添加墙壁。
    HOURGLASS.add((i, 23))  # 为底盖添加墙壁。
for i in range(1, 5):
    HOURGLASS.add((18, i))  # 为左上方的直墙添加墙壁。
    HOURGLASS.add((36, i))  # 为右上方的直墙添加墙壁。
    HOURGLASS.add((18, i + 19))  # 在左下角添加墙壁。
    HOURGLASS.add((36, i + 19))  # 在右下角添加墙壁。
for i in range(8):
    HOURGLASS.add((19 + i, 5 + i))  #添加左上角斜墙。
    HOURGLASS.add((35 - i, 5 + i))  # 添加右上角斜墙。
    HOURGLASS.add((25 - i, 13 + i))  # 添加左下角斜墙。
    HOURGLASS.add((29 + i, 13 + i))  # 添加右下角斜墙。

# 一开始把沙子放在沙漏的顶端。
INITIAL_SAND = set()
for y in range(8):
    for x in range(19 + y, 36 - y):
        INITIAL_SAND.add((x, y + 4))


def main():
    bext.fg('yellow')
    bext.clear()

    #绘制推出消息：
    bext.goto(0, 0)
    print('Ctrl-C to quit.', end='')

    # 显示沙漏的墙壁：
    for wall in HOURGLASS:
        bext.goto(wall[X], wall[Y])
        print(WALL, end='')

    while True:  # 主程序循环
        allSand = list(INITIAL_SAND)

        # 绘制出最初的沙子
        for sand in allSand:
            bext.goto(sand[X], sand[Y])
            print(SAND, end='')

        runHourglassSimulation(allSand)


def runHourglassSimulation(allSand):
    """只需运行落沙模拟，知道沙子停止移动。"""
    while True:  # 继续循环，知道沙子用完。
        random.shuffle(allSand)  # 颗粒模拟的随即顺序。

        sandMovedOnThisStep = False
        for i, sand in enumerate(allSand):
            if sand[Y] == SCREEN_HEIGHT - 1:
                # 沙子在最底部，所以它不会移动：
                continue

            # 如果沙子底下没有东西, 就把它移下去:
            noSandBelow = (sand[X], sand[Y] + 1) not in allSand
            noWallBelow = (sand[X], sand[Y] + 1) not in HOURGLASS
            canFallDown = noSandBelow and noWallBelow

            if canFallDown:
                # 在新位置向下一个空间绘制沙子:
                bext.goto(sand[X], sand[Y])
                print(' ', end='')  # 清除旧位置。
                bext.goto(sand[X], sand[Y] + 1)
                print(SAND, end='')

                # 把沙子放在新位置的下一个空间：
                allSand[i] = (sand[X], sand[Y] + 1)
                sandMovedOnThisStep = True
            else:
                # 检查沙子是否会向左掉落。
                belowLeft = (sand[X] - 1, sand[Y] + 1)
                noSandBelowLeft = belowLeft not in allSand
                noWallBelowLeft = belowLeft not in HOURGLASS
                left = (sand[X] - 1, sand[Y])
                noWallLeft = left not in HOURGLASS
                notOnLeftEdge = sand[X] > 0
                canFallLeft = (noSandBelowLeft and noWallBelowLeft
                    and noWallLeft and notOnLeftEdge)

                #检查沙子是否会向右掉落。
                belowRight = (sand[X] + 1, sand[Y] + 1)
                noSandBelowRight = belowRight not in allSand
                noWallBelowRight = belowRight not in HOURGLASS
                right = (sand[X] + 1, sand[Y])
                noWallRight = right not in HOURGLASS
                notOnRightEdge = sand[X] < SCREEN_WIDTH - 1
                canFallRight = (noSandBelowRight and noWallBelowRight
                    and noWallRight and notOnRightEdge)

                # 设置下降方向:
                fallingDirection = None
                if canFallLeft and not canFallRight:
                    fallingDirection = -1  #把沙子放在左边。
                elif not canFallLeft and canFallRight:
                    fallingDirection = 1  # 把沙子放在右边。
                elif canFallLeft and canFallRight:
                    #两者都是可能的，所以随机设置:
                    fallingDirection = random.choice((-1, 1))

                # 检查沙子是否可以向左或向右“远”落两个空格，而不是只落一个空格:
                if random.random() * 100 <= WIDE_FALL_CHANCE:
                    belowTwoLeft = (sand[X] - 2, sand[Y] + 1)
                    noSandBelowTwoLeft = belowTwoLeft not in allSand
                    noWallBelowTwoLeft = belowTwoLeft not in HOURGLASS
                    notOnSecondToLeftEdge = sand[X] > 1
                    canFallTwoLeft = (canFallLeft and noSandBelowTwoLeft
                        and noWallBelowTwoLeft and notOnSecondToLeftEdge)

                    belowTwoRight = (sand[X] + 2, sand[Y] + 1)
                    noSandBelowTwoRight = belowTwoRight not in allSand
                    noWallBelowTwoRight = belowTwoRight not in HOURGLASS
                    notOnSecondToRightEdge = sand[X] < SCREEN_WIDTH - 2
                    canFallTwoRight = (canFallRight
                        and noSandBelowTwoRight and noWallBelowTwoRight
                        and notOnSecondToRightEdge)

                    if canFallTwoLeft and not canFallTwoRight:
                        fallingDirection = -2
                    elif not canFallTwoLeft and canFallTwoRight:
                        fallingDirection = 2
                    elif canFallTwoLeft and canFallTwoRight:
                        fallingDirection = random.choice((-2, 2))

                if fallingDirection == None:
                    # 这里的沙子不会掉下来，所以继续前进。
                    continue

                # 把沙子拉到它的新位置:
                bext.goto(sand[X], sand[Y])
                print(' ', end='')  # 删除旧沙。
                bext.goto(sand[X] + fallingDirection, sand[Y] + 1)
                print(SAND, end='')  # 绘制出新沙。

                # 将沙粒移到新位置
                allSand[i] = (sand[X] + fallingDirection, sand[Y] + 1)
                sandMovedOnThisStep = True

        sys.stdout.flush()  # (需要bext-using程序)
        time.sleep(PAUSE_LENGTH)  # 暂停后。

        # 如果没有沙子在这步移动，重置沙漏:
        if not sandMovedOnThisStep:
            time.sleep(2)
            # Erase all of the sand:
            for sand in allSand:
                bext.goto(sand[X], sand[Y])
                print(' ', end='')
            break  # 中断主模拟循环。


# 如果程序运行(而不是导入)，运行游戏:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # 按下Ctrl-C后，结束程序。
