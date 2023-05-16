"""旋转立方体, 作者：Al Sweigart al@inventwithpython.com
旋转立方体动画。按Ctrl-C停止。
此代码可在https://nostarch.com/big-book-small-python-programming获得
标签:大，艺术，数学"""

# 这个程序必须在终端/命令提示符窗口中运行。

import math, time, sys, os

# 建立常数:
PAUSE_AMOUNT = 0.1  # 暂停时间为十分之一秒。
WIDTH, HEIGHT = 80, 24
SCALEX = (WIDTH - 4) // 8
SCALEY = (HEIGHT - 4) // 8
# 文本单元格的高度是它们宽度的两倍，所以设置纵向缩放：
SCALEY *= 2
TRANSLATEX = (WIDTH - 4) // 2
TRANSLATEY = (HEIGHT - 4) // 2

# (!) 试着把这个改为'#'或'*'或其他字符:
LINE_CHAR = chr(9608)  # 字符9608是一个实体块。

# (!) 试着将其中两个值设置为0，使立方体只沿着一个轴旋转:
X_ROTATE_SPEED = 0.03
Y_ROTATE_SPEED = 0.08
Z_ROTATE_SPEED = 0.13

# 这个程序将XYZ坐标存储在列表中，X坐标位于下标0,Y坐标位于1,Z坐标位于2。
# 当访问这些列表中的坐标时，这些常量使我们的代码更具可读性。
X = 0
Y = 1
Z = 2


def line(x1, y1, x2, y2):
    """返回一行中给定点之间的点列表。

    使用Bresenham线性算法。更多信息在
    https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm获得"""
    points = []  # 包含直线上的点。
    # “陡峭”是指直线的斜率大于45度或小于-45度:

    # 检查起点和终点相邻的特殊情况，
    # 档次功能不能被正确处理，
    # 返回一个硬编码的列表:
    if (x1 == x2 and y1 == y2 + 1) or (y1 == y2 and x1 == x2 + 1):
        return [(x1, y1), (x2, y2)]

    isSteep = abs(y2 - y1) > abs(x2 - x1)
    if isSteep:
        # 这个算法只处理非陡度线，
        # 所以让我们把斜率改为非陡度线，然后再改回来。
        x1, y1 = y1, x1  # 交换x1和y1
        x2, y2 = y2, x2  # 交换x2和y2
    isReversed = x1 > x2  # 如果直线从右向左，则为True。

    if isReversed:  # 让直线上的点从右向左移动。
        x1, x2 = x2, x1  # 交换x1和x2
        y1, y2 = y2, y1  # 交换y1和y2

        deltax = x2 - x1
        deltay = abs(y2 - y1)
        extray = int(deltax / 2)
        currenty = y2
        if y1 < y2:
            ydirection = 1
        else:
            ydirection = -1
        # 计算这一行中每个x的y值:
        for currentx in range(x2, x1 - 1, -1):
            if isSteep:
                points.append((currenty, currentx))
            else:
                points.append((currentx, currenty))
            extray -= deltay
            if extray <= 0:  #只改变一次y的坐标extray <= 0.
                currenty -= ydirection
                extray += deltax
    else:  # 让直线上的点从左到右。
        deltax = x2 - x1
        deltay = abs(y2 - y1)
        extray = int(deltax / 2)
        currenty = y1
        if y1 < y2:
            ydirection = 1
        else:
            ydirection = -1
        # 计算这一行中每个x的y值:
        for currentx in range(x1, x2 + 1):
            if isSteep:
                points.append((currenty, currentx))
            else:
                points.append((currentx, currenty))
            extray -= deltay
            if extray < 0:  # 只改变一次y的坐标extray < 0.
                currenty += ydirection
                extray += deltax
    return points


def rotatePoint(x, y, z, ax, ay, az):
    """返回由x, y, z参数旋转的(x, y, z)元组。

    旋转发生在角ax, ay, az(弧度)的原点0,0,0
       各轴方向:
         -y
          |
          +-- +x
         /
        +z
    """

    # 绕x轴旋转:
    rotatedX = x
    rotatedY = (y * math.cos(ax)) - (z * math.sin(ax))
    rotatedZ = (y * math.sin(ax)) + (z * math.cos(ax))
    x, y, z = rotatedX, rotatedY, rotatedZ

    # 绕y轴旋转:
    rotatedX = (z * math.sin(ay)) + (x * math.cos(ay))
    rotatedY = y
    rotatedZ = (z * math.cos(ay)) - (x * math.sin(ay))
    x, y, z = rotatedX, rotatedY, rotatedZ

    # 绕Z轴旋转
    rotatedX = (x * math.cos(az)) - (y * math.sin(az))
    rotatedY = (x * math.sin(az)) + (y * math.cos(az))
    rotatedZ = z

    return (rotatedX, rotatedY, rotatedZ)


def adjustPoint(point):
    """调整空间中XYZ点到适合的平面XY点在屏幕上显示。
    通过SCALEX和SCALEY缩放这个平面上的点，
    然后通过TRANSLATEX和TRANSLATEY移动点。"""
    return (int(point[X] * SCALEX + TRANSLATEX),
            int(point[Y] * SCALEY + TRANSLATEY))


"""CUBE_CORNERS stores the XYZ coordinates of the corners of a cube.
The indexes for each corner in CUBE_CORNERS are marked in this diagram:
      0---1
     /|  /|
    2---3 |
    | 4-|-5
    |/  |/
    6---7"""
CUBE_CORNERS = [[-1, -1, -1], # 点0
                [ 1, -1, -1], # 点1
                [-1, -1,  1], # 点2
                [ 1, -1,  1], # 点3
                [-1,  1, -1], # 点4
                [ 1,  1, -1], # 点5
                [-1,  1,  1], # 点6
                [ 1,  1,  1]] # 点7
# 在它们被rx, ry和rz数量旋转后，
# rotatedCorners存储CUBE_CORNERS中的XYZ坐标，:
rotatedCorners = [None, None, None, None, None, None, None, None]
# 每个轴的旋转量:
xRotation = 0.0
yRotation = 0.0
zRotation = 0.0

try:
    while True:  # 主程序循环。
        # 沿着不同的轴旋转立方体:
        xRotation += X_ROTATE_SPEED
        yRotation += Y_ROTATE_SPEED
        zRotation += Z_ROTATE_SPEED
        for i in range(len(CUBE_CORNERS)):
            x = CUBE_CORNERS[i][X]
            y = CUBE_CORNERS[i][Y]
            z = CUBE_CORNERS[i][Z]
            rotatedCorners[i] = rotatePoint(x, y, z, xRotation,
                yRotation, zRotation)

        # 得到立方体中的点
        cubePoints = []
        for fromCornerIndex, toCornerIndex in ((0, 1), (1, 3), (3, 2), (2, 0), (0, 4), (1, 5), (2, 6), (3, 7), (4, 5), (5, 7), (7, 6), (6, 4)):
            fromX, fromY = adjustPoint(rotatedCorners[fromCornerIndex])
            toX, toY = adjustPoint(rotatedCorners[toCornerIndex])
            pointsOnLine = line(fromX, fromY, toX, toY)
            cubePoints.extend(pointsOnLine)

        # 消除重复点:
        cubePoints = tuple(frozenset(cubePoints))

        # 在屏幕上显示立方体:
        for y in range(HEIGHT):
            for x in range(WIDTH):
                if (x, y) in cubePoints:
                    # 显示完整的块:
                    print(LINE_CHAR, end='', flush=False)
                else:
                    # 显示空的空间:
                    print(' ', end='', flush=False)
            print(flush=False)
        print('Press Ctrl-C to quit.', end='', flush=True)

        time.sleep(PAUSE_AMOUNT)  # 暂停一下。

        # 清屏：
        if sys.platform == 'win32':
            os.system('cls')  # Windows使用cls命令。
        else:
            os.system('clear')  # macOS和Linux使用clear命令。

except KeyboardInterrupt:
    print('Rotating Cube, by Al Sweigart al@inventwithpython.com')
    sys.exit()  # 按下Ctrl-C后，结束程序。
