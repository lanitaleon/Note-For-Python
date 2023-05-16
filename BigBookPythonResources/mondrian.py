"""蒙德里安的艺术发电机, 作者：Al Sweigart al@inventwithpython.com
随机生成蒙德里安风格的艺术。
更多信息: https://en.wikipedia.org/wiki/Piet_Mondrian
此代码可在https://nostarch.com/big-book-small-python-programming获得
标签:大的，艺术的，文本"""

import sys, random

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# 建立常数:
MIN_X_INCREASE = 6
MAX_X_INCREASE = 16
MIN_Y_INCREASE = 3
MAX_Y_INCREASE = 6
WHITE = 'white'
BLACK = 'black'
RED = 'red'
YELLOW = 'yellow'
BLUE = 'blue'

# 设置屏幕:
width, height = bext.size()
# 在Windows上，如果不自动添加换行符，我们就无法打印到最后一列，所以将宽度减少1:
width -= 1

height -= 3

while True:  # 主程序循环。
    # 在画布上预填充空白:
    canvas = {}
    for x in range(width):
        for y in range(height):
            canvas[(x, y)] = WHITE

    # 产生垂直的线:
    numberOfSegmentsToDelete = 0
    x = random.randint(MIN_X_INCREASE, MAX_X_INCREASE)
    while x < width - MIN_X_INCREASE:
        numberOfSegmentsToDelete += 1
        for y in range(height):
            canvas[(x, y)] = BLACK
        x += random.randint(MIN_X_INCREASE, MAX_X_INCREASE)

    # 产生水平的线:
    y = random.randint(MIN_Y_INCREASE, MAX_Y_INCREASE)
    while y < height - MIN_Y_INCREASE:
        numberOfSegmentsToDelete += 1
        for x in range(width):
            canvas[(x, y)] = BLACK
        y += random.randint(MIN_Y_INCREASE, MAX_Y_INCREASE)

    numberOfRectanglesToPaint = numberOfSegmentsToDelete - 3
    numberOfSegmentsToDelete = int(numberOfSegmentsToDelete * 1.5)

    # 随机选择点并尝试移除它们。
    for i in range(numberOfSegmentsToDelete):
        while True:  # 继续选择要删除的段。
            # 在一个现有的片段上获得一个随机的起点:
            startx = random.randint(1, width - 2)
            starty = random.randint(1, height - 2)
            if canvas[(startx, starty)] == WHITE:
                continue

            # 看看我们是在垂直还是水平段上：
            if (canvas[(startx - 1, starty)] == WHITE and
                canvas[(startx + 1, starty)] == WHITE):
                orientation = 'vertical'
            elif (canvas[(startx, starty - 1)] == WHITE and
                canvas[(startx, starty + 1)] == WHITE):
                orientation = 'horizontal'
            else:
                # 起始点在一个交集上，所以得到一个新的随机起始点:
                continue

            pointsToDelete = [(startx, starty)]

            canDeleteSegment = True
            if orientation == 'vertical':
                # 从起点向上走一条路径，看看我们能否移除这段:
                for changey in (-1, 1):
                    y = starty
                    while 0 < y < height - 1:
                        y += changey
                        if (canvas[(startx - 1, y)] == BLACK and
                            canvas[(startx + 1, y)] == BLACK):
                            # 我们发现了一个十字路口。
                            break
                        elif ((canvas[(startx - 1, y)] == WHITE and
                               canvas[(startx + 1, y)] == BLACK) or
                              (canvas[(startx - 1, y)] == BLACK and
                               canvas[(startx + 1, y)] == WHITE)):
                            # 我们找到了一个T形路口;我们不能删除这个段:
                            canDeleteSegment = False
                            break
                        else:
                            pointsToDelete.append((startx, y))

            elif orientation == 'horizontal':
                # 从起点向上走一条路径，看看我们能否移除这段:
                for changex in (-1, 1):
                    x = startx
                    while 0 < x < width - 1:
                        x += changex
                        if (canvas[(x, starty - 1)] == BLACK and
                            canvas[(x, starty + 1)] == BLACK):
                            #我们发现了一个十字路口。
                            break
                        elif ((canvas[(x, starty - 1)] == WHITE and
                               canvas[(x, starty + 1)] == BLACK) or
                              (canvas[(x, starty - 1)] == BLACK and
                               canvas[(x, starty + 1)] == WHITE)):
                            # 我们找到了一个T形路口;我们不能删除这个段:
                            canDeleteSegment = False
                            break
                        else:
                            pointsToDelete.append((x, starty))
            if not canDeleteSegment:
                continue  # 获得一个新的随机起点。
            break  # 继续删除段。

        # 如果我们可以删除这段，将所有的点设置为白色:
        for x, y in pointsToDelete:
            canvas[(x, y)] = WHITE

    # 添加边框线:
    for x in range(width):
        canvas[(x, 0)] = BLACK  # 上边框
        canvas[(x, height - 1)] = BLACK  # 下边框
    for y in range(height):
        canvas[(0, y)] = BLACK  # 左侧边框
        canvas[(width - 1, y)] = BLACK  # 右侧边框

    # 画矩形:
    for i in range(numberOfRectanglesToPaint):
        while True:
            startx = random.randint(1, width - 2)
            starty = random.randint(1, height - 2)

            if canvas[(startx, starty)] != WHITE:
                continue  # 获得一个新的随机起点。
            else:
                break

        # 填充算法：
        colorToPaint = random.choice([RED, YELLOW, BLUE, BLACK])
        pointsToPaint = set([(startx, starty)])
        while len(pointsToPaint) > 0:
            x, y = pointsToPaint.pop()
            canvas[(x, y)] = colorToPaint
            if canvas[(x - 1, y)] == WHITE:
                pointsToPaint.add((x - 1, y))
            if canvas[(x + 1, y)] == WHITE:
                pointsToPaint.add((x + 1, y))
            if canvas[(x, y - 1)] == WHITE:
                pointsToPaint.add((x, y - 1))
            if canvas[(x, y + 1)] == WHITE:
                pointsToPaint.add((x, y + 1))

    # 绘制画布数据结构:
    for y in range(height):
        for x in range(width):
            bext.bg(canvas[(x, y)])
            print(' ', end='')

        print()

    # 提示用户创建一个新的艺术品:
    try:
        input('Press Enter for another work of art, or Ctrl-C to quit.')
    except KeyboardInterrupt:
        sys.exit()
