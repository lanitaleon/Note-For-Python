"""森林火灾模拟，由 Al Sweigart al@inventwithpython.com
模拟在森林中蔓延的野火。 按 Ctrl-C 停止。
灵感来自 Nicky Case 的 Emoji Sim http://ncase.me/simulating/model/
此代码可在 https://nostarch.com/big-book-small-python-programming 获得
标签：短，bext，模拟"""

import random, sys, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# 设置常量：
WIDTH = 79
HEIGHT = 22

TREE = 'A'
FIRE = 'W'
EMPTY = ' '

# (!) 尝试将这些设置更改为 0.0 和 1.0 之间的任何设置：
INITIAL_TREE_DENSITY = 0.20  # 以树木开始的森林数量。
GROW_CHANCE = 0.01  # 一个空白空间变成一棵树的几率。
FIRE_CHANCE = 0.01  # 一棵树被闪电击中和烧伤的几率。

# (!) 尝试将暂停长度设置为 1.0 或 0.0：
PAUSE_LENGTH = 0.5


def main():
    forest = createNewForest()
    bext.clear()

    while True:  # 主程序循环。
        displayForest(forest)

        # 运行单个模拟步骤：
        nextForest = {'width': forest['width'],
                      'height': forest['height']}

        for x in range(forest['width']):
            for y in range(forest['height']):
                if (x, y) in nextForest:
                    # 如果我们已经在 a 上设置了 nextForest[(x, y)]
                    # 之前的迭代，这里什么都不做：
                    continue

                if ((forest[(x, y)] == EMPTY)
                    and (random.random() <= GROW_CHANCE)):
                    # 在这空旷的地方种一棵树。
                    nextForest[(x, y)] = TREE
                elif ((forest[(x, y)] == TREE)
                    and (random.random() <= FIRE_CHANCE)):
                    # 闪电点燃了这棵树。
                    nextForest[(x, y)] = FIRE
                elif forest[(x, y)] == FIRE:
                    # 这棵树目前正在燃烧。
                    # 遍历所有相邻的空间：
                    for ix in range(-1, 2):
                        for iy in range(-1, 2):
                            # 火蔓延到邻近的树木：
                            if forest.get((x + ix, y + iy)) == TREE:
                                nextForest[(x + ix, y + iy)] = FIRE
                    # 这棵树现在已经烧毁了，所以把它擦掉：
                    nextForest[(x, y)] = EMPTY
                else:
                    # 只需复制现有对象：
                    nextForest[(x, y)] = forest[(x, y)]
        forest = nextForest

        time.sleep(PAUSE_LENGTH)


def createNewForest():
    """返回新森林数据结构的字典。"""
    forest = {'width': WIDTH, 'height': HEIGHT}
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if (random.random() * 100) <= INITIAL_TREE_DENSITY:
                forest[(x, y)] = TREE  # 从一棵树开始。
            else:
                forest[(x, y)] = EMPTY  # 从一个空的空间开始。
    return forest


def displayForest(forest):
    """在屏幕上显示森林数据结构。"""
    bext.goto(0, 0)
    for y in range(forest['height']):
        for x in range(forest['width']):
            if forest[(x, y)] == TREE:
                bext.fg('green')
                print(TREE, end='')
            elif forest[(x, y)] == FIRE:
                bext.fg('red')
                print(FIRE, end='')
            elif forest[(x, y)] == EMPTY:
                print(EMPTY, end='')
        print()
    bext.fg('reset')  # 使用默认字体颜色。
    print('Grow chance: {}%  '.format(GROW_CHANCE * 100), end='')
    print('Lightning chance: {}%  '.format(FIRE_CHANCE * 100), end='')
    print('Press Ctrl-C to quit.')


# 如果此程序已运行（而不是导入），请运行游戏：
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # 当按下 Ctrl-C 时，结束程序。
