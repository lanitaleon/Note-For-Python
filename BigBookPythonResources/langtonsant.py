"""兰顿的蚂蚁,作者：Al Sweigart al@inventwithpython.com
一个细胞自动机动画。按Ctrl-C停止。
更多信息可在https://en.wikipedia.org/wiki/Langton%27s_ant获得
此代码可在https://nostarch.com/big-book-small-python-programming获得
标签:大，艺术，bext，模拟"""

import copy, random, sys, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# 建立常数:
WIDTH, HEIGHT = bext.size()
# 在Windows上，如果不自动添加换行符，我们就无法打印到最后一列，所以将宽度减少1:
WIDTH -= 1
HEIGHT -= 1  # 调整在底部的退出消息。

NUMBER_OF_ANTS = 10  # (!) 试着把它改成1或50。
PAUSE_AMOUNT = 0.1  # (!) 尝试将其更改为1.0或0.0。

# (!) 试着改变这些，让蚂蚁看起来不一样:
ANT_UP = '^'
ANT_DOWN = 'v'
ANT_LEFT = '<'
ANT_RIGHT = '>'

# (!) 试着将这些颜色改变为“黑”、“红”、“绿”、“黄”、“蓝”、“紫”、“青”或“白”中的一种。 (这些是bext模块支持的唯一颜色。)
ANT_COLOR = 'red'
BLACK_TILE = 'black'
WHITE_TILE = 'white'

NORTH = 'north'
SOUTH = 'south'
EAST = 'east'
WEST = 'west'


def main():
    bext.fg(ANT_COLOR)  # 蚂蚁的颜色是最显著的颜色。
    bext.bg(WHITE_TILE)  # 设置背景为白色开始。
    bext.clear()

    # 创建新的板数据结构:
    board = {'width': WIDTH, 'height': HEIGHT}

    # 创建ant数据结构:
    ants = []
    for i in range(NUMBER_OF_ANTS):
        ant = {
            'x': random.randint(0, WIDTH - 1),
            'y': random.randint(0, HEIGHT - 1),
            'direction': random.choice([NORTH, SOUTH, EAST, WEST]),
        }
        ants.append(ant)

    # 记录已经改变了的瓦片并在屏幕上重新绘制：
    changedTiles = []

    while True:  #主程序的循环：
        displayBoard(board, ants, changedTiles)
        changedTiles = []

        #nextBoard是在模拟的下一个步骤中board的样子。 从当前步骤的board副本开始:
        nextBoard = copy.copy(board)

        # 为每只蚂蚁运行一个模拟步骤:
        for ant in ants:
            if board.get((ant['x'], ant['y']), False) == True:
                nextBoard[(ant['x'], ant['y'])] = False
                #顺时针方向旋转：
                if ant['direction'] == NORTH:
                    ant['direction'] = EAST
                elif ant['direction'] == EAST:
                    ant['direction'] = SOUTH
                elif ant['direction'] == SOUTH:
                    ant['direction'] = WEST
                elif ant['direction'] == WEST:
                    ant['direction'] = NORTH
            else:
                nextBoard[(ant['x'], ant['y'])] = True
                # 逆时针方向旋转
                if ant['direction'] == NORTH:
                    ant['direction'] = WEST
                elif ant['direction'] == WEST:
                    ant['direction'] = SOUTH
                elif ant['direction'] == SOUTH:
                    ant['direction'] = EAST
                elif ant['direction'] == EAST:
                    ant['direction'] = NORTH
            changedTiles.append((ant['x'], ant['y']))

            # 让蚂蚁朝它所面对的任何方向前进:
            if ant['direction'] == NORTH:
                ant['y'] -= 1
            if ant['direction'] == SOUTH:
                ant['y'] += 1
            if ant['direction'] == WEST:
                ant['x'] -= 1
            if ant['direction'] == EAST:
                ant['x'] += 1

            # 如果蚂蚁越过了屏幕的边缘，它应该绕到另一边。
            ant['x'] = ant['x'] % WIDTH
            ant['y'] = ant['y'] % HEIGHT

            changedTiles.append((ant['x'], ant['y']))

        board = nextBoard


def displayBoard(board, ants, changedTiles):
    """在屏幕上显示挡板和蚂蚁  改变的瓦片参数是一个(x, y)元组列表，用于显示屏幕上已更改且需要重新绘制的瓦片。  """

    # 绘制board的数据结构:
    for x, y in changedTiles:
        bext.goto(x, y)
        if board.get((x, y), False):
            bext.bg(BLACK_TILE)
        else:
            bext.bg(WHITE_TILE)

        antIsHere = False
        for ant in ants:
            if (x, y) == (ant['x'], ant['y']):
                antIsHere = True
                if ant['direction'] == NORTH:
                    print(ANT_UP, end='')
                elif ant['direction'] == SOUTH:
                    print(ANT_DOWN, end='')
                elif ant['direction'] == EAST:
                    print(ANT_LEFT, end='')
                elif ant['direction'] == WEST:
                    print(ANT_RIGHT, end='')
                break
        if not antIsHere:
            print(' ', end='')

    # 在屏幕底部显示退出信息
    bext.goto(0, HEIGHT)
    bext.bg(WHITE_TILE)
    print('Press Ctrl-C to quit.', end='')

    sys.stdout.flush()  # (用于文本使用程序。)
    time.sleep(PAUSE_AMOUNT)


# 如果程序运行(而不是导入)，运行游戏:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Langton's Ant, by Al Sweigart al@inventwithpython.com")
        sys.exit()  # 按下Ctrl-C后，结束程序。
