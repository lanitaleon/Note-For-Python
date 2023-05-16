"""弹跳DVD标志，作者：Al Sweigart al@inventwithpython.com
一个弹跳的 DVD 标志动画。 您必须“达到一定年龄”才能
欣赏这一点。 按 Ctrl-C 停止。

注意：不要在此程序运行时调整终端窗口的大小。
此代码可在 https://nostarch.com/big-book-small-python-programming 获得
标签:简短，美观，简洁"""

import sys, random, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# 设置常量：
WIDTH, HEIGHT = bext.size()
# 我们无法在 Windows 上打印到最后一列而不添加
# 自动换行，所以宽度减一：
WIDTH -= 1

NUMBER_OF_LOGOS = 5  # (!) 尝试将其更改为 1 或 100。
PAUSE_AMOUNT = 0.2  # (!) 尝试将其更改为 1.0 或 0.0。
# (!) 尝试将此列表更改为更少的颜色：
COLORS = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

UP_RIGHT   = 'ur'
UP_LEFT    = 'ul'
DOWN_RIGHT = 'dr'
DOWN_LEFT  = 'dl'
DIRECTIONS = (UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT)

# 标志字典的关键名称:
COLOR = 'color'
X = 'x'
Y = 'y'
DIR = 'direction'


def main():
    bext.clear()

    # 生成一些标志。
    logos = []
    for i in range(NUMBER_OF_LOGOS):
        logos.append({COLOR: random.choice(COLORS),
                      X: random.randint(1, WIDTH - 4),
                      Y: random.randint(1, HEIGHT - 4),
                      DIR: random.choice(DOWN_RIGHT)})
        if logos[-1][X] % 2 == 1:
            # 确保 X 是均匀的，以便它可以击中角落。
            logos[-1][X] -= 1

    cornerBounces = 0  # 数一数一个标志有多少次碰到角落。
    while True:  # 主程序循环。
        for logo in logos:  # 处理标志列表中的每个标志。
            # 擦除标志的当前位置：
            bext.goto(logo[X], logo[Y])
            print('   ', end='')  # (!) 尝试注释掉这一行。

            originalDirection = logo[DIR]

            # 查看标志是否从角落反弹：
            if logo[X] == 0 and logo[Y] == 0:
                logo[DIR] = DOWN_RIGHT
                cornerBounces += 1
            elif logo[X] == 0 and logo[Y] == HEIGHT - 1:
                logo[DIR] = UP_RIGHT
                cornerBounces += 1
            elif logo[X] == WIDTH - 3 and logo[Y] == 0:
                logo[DIR] = DOWN_LEFT
                cornerBounces += 1
            elif logo[X] == WIDTH - 3 and logo[Y] == HEIGHT - 1:
                logo[DIR] = UP_LEFT
                cornerBounces += 1

            # 查看标志是否从左边缘反弹：
            elif logo[X] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = UP_RIGHT
            elif logo[X] == 0 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = DOWN_RIGHT

            # 查看标志是否从右边缘反弹：
            # （WIDTH - 3 因为“DVD”有 3 个字母。）
            elif logo[X] == WIDTH - 3 and logo[DIR] == UP_RIGHT:
                logo[DIR] = UP_LEFT
            elif logo[X] == WIDTH - 3 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = DOWN_LEFT

            # 查看标志是否从顶部边缘反弹：
            elif logo[Y] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = DOWN_LEFT
            elif logo[Y] == 0 and logo[DIR] == UP_RIGHT:
                logo[DIR] = DOWN_RIGHT

            # 查看标志是否从底部边缘反弹：
            elif logo[Y] == HEIGHT - 1 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = UP_LEFT
            elif logo[Y] == HEIGHT - 1 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = UP_RIGHT

            if logo[DIR] != originalDirection:
                # 当标志反弹时更改颜色：
                logo[COLOR] = random.choice(COLORS)

            # 移动标志。 （X 移动 2 因为终端
            # 字符的高度是宽度的两倍。）
            if logo[DIR] == UP_RIGHT:
                logo[X] += 2
                logo[Y] -= 1
            elif logo[DIR] == UP_LEFT:
                logo[X] -= 2
                logo[Y] -= 1
            elif logo[DIR] == DOWN_RIGHT:
                logo[X] += 2
                logo[Y] += 1
            elif logo[DIR] == DOWN_LEFT:
                logo[X] -= 2
                logo[Y] += 1

        # 显示角落反弹次数：
        bext.goto(5, 0)
        bext.fg('white')
        print('Corner bounces:', cornerBounces, end='')

        for logo in logos:
            # 在新位置绘制标志：
            bext.goto(logo[X], logo[Y])
            bext.fg(logo[COLOR])
            print('DVD', end='')

        bext.goto(0, 0)

        sys.stdout.flush()  # （下次使用的程序需要。）
        time.sleep(PAUSE_AMOUNT)


# 如果此程序运行（而不是导入），运行游戏：
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print('Bouncing DVD Logo, by Al Sweigart')
        sys.exit()  # 当按下 Ctrl-C 时，结束程序。
