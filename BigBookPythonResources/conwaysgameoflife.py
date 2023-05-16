"""康威的生命游戏，作者：Al Sweigart al@inventwithpython.com
经典的元胞自动机模拟。 按 Ctrl-C 停止。
更多信息请访问：https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
此代码可在 https://nostarch.com/big-book-small-python-programming 获得
标签：短，艺术，模拟"""

import copy, random, sys, time

# 设置常量：
WIDTH = 79   # 单元格网格的宽度。
HEIGHT = 20  # 单元格网格的高度。

# (!) 尝试将 ALIVE 更改为 '#' 或其他字符：
ALIVE = 'O'  # 代表活细胞的字符。
# (!) 尝试将 DEAD 更改为 '.' 或其他字符：
DEAD = ' '   # 代表死细胞的字符。

# (!) 尝试将 ALIVE 更改为“|” 和死到'-'。

# cell 和 nextCells 是游戏状态的字典。
# 它们的键是 (x, y) 元组，它们的值是 ALIVE 之一
# 或 DEAD 值。
nextCells = {}
# 将随机死细胞和活细胞放入 nextCells 中：
for x in range(WIDTH):  # 循环遍历每个可能的列。
    for y in range(HEIGHT):  # 遍历每个可能的行。
        # 50/50 的机会使细胞开始存活或死亡。
        if random.randint(0, 1) == 0:
            nextCells[(x, y)] = ALIVE  # 添加一个活细胞。
        else:
            nextCells[(x, y)] = DEAD  # 添加一个死细胞。

while True:  # 主程序循环。
    # 该循环的每次迭代都是模拟的一个步骤。

    print('\n' * 50)  # 用换行符分隔每个步骤。
    cells = copy.deepcopy(nextCells)

    # 在屏幕上打印单元格：
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(cells[(x, y)], end='')  # 打印# 或空格。
        print()  # 在行尾打印换行符。
    print('Press Ctrl-C to quit.')

    # 根据当前步骤的单元格计算下一步的单元格：
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # 获取 (x, y) 的相邻坐标，即使它们
            # 环绕边缘：
            left  = (x - 1) % WIDTH
            right = (x + 1) % WIDTH
            above = (y - 1) % HEIGHT
            below = (y + 1) % HEIGHT

            # 计算活着的邻居的数量：
            numNeighbors = 0
            if cells[(left, above)] == ALIVE:
                numNeighbors += 1  # 左上角的邻居还活着。
            if cells[(x, above)] == ALIVE:
                numNeighbors += 1  # 上面的邻居还活着。
            if cells[(right, above)] == ALIVE:
                numNeighbors += 1  # 右上角的邻居还活着。
            if cells[(left, y)] == ALIVE:
                numNeighbors += 1  # 左邻居还活着。
            if cells[(right, y)] == ALIVE:
                numNeighbors += 1  # 右邻还活着。
            if cells[(left, below)] == ALIVE:
                numNeighbors += 1  # 左下角的邻居还活着。
            if cells[(x, below)] == ALIVE:
                numNeighbors += 1  # 最底层的邻居还活着。
            if cells[(right, below)] == ALIVE:
                numNeighbors += 1  # 右下角的邻居还活着。

            # 根据康威的生命游戏规则设置单元格：
            if cells[(x, y)] == ALIVE and (numNeighbors == 2
                or numNeighbors == 3):
                    # 有 2 或 3 个邻居的活细胞保持活力：
                    nextCells[(x, y)] = ALIVE
            elif cells[(x, y)] == DEAD and numNeighbors == 3:
                # 有 3 个邻居的死细胞变成活细胞：
                nextCells[(x, y)] = ALIVE
            else:
                # 其他一切都会死亡或保持死亡：
                nextCells[(x, y)] = DEAD

    try:
        time.sleep(1)  # 添加 1 秒暂停以减少闪烁。
    except KeyboardInterrupt:
        print("Conway's Game of Life")
        print('By Al Sweigart al@inventwithpython.com')
        sys.exit()  # 当按下 Ctrl-C 时，结束程序。
