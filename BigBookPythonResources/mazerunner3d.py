"""3D迷宫, 作者：Al Sweigart al@inventwithpython.com
在迷宫中移动并尝试逃跑…在3D模式下!
此代码可在https://nostarch.com/big-book-small-python-programming获得
标签:超大，艺术，迷宫，游戏"""

import copy, sys, os

#建立常数:
WALL = '#'
EMPTY = ' '
START = 'S'
EXIT = 'E'
BLOCK = chr(9617)  # 字符9617是'░'
NORTH = 'NORTH'
SOUTH = 'SOUTH'
EAST = 'EAST'
WEST = 'WEST'


def wallStrToWallDict(wallStr):
    """取走表示墙画的字符串（像ALL_OPEN或CLOSED中的那些），并返回字典中
    代表作为键的（x，y）元组和在该x, y位置绘制的字符的单字符字符串。"""
    wallDict = {}
    height = 0
    width = 0
    for y, line in enumerate(wallStr.splitlines()):
        if y > height:
            height = y
        for x, character in enumerate(line):
            if x > width:
                width = x
            wallDict[(x, y)] = character
    wallDict['height'] = height + 1
    wallDict['width'] = width + 1
    return wallDict

EXIT_DICT = {(0, 0): 'E', (1, 0): 'X', (2, 0): 'I',
             (3, 0): 'T', 'height': 1, 'width': 4}

# 创建显示出来的字符串的方法是使用wallStrToWallDict()将这些多行字符串中的图片转换为字典。
# 然后我们根据玩家的位置和方向，将CLOSED中的墙壁字典“粘贴”在ALL_OPEN中的墙壁字典之上，从而组成墙壁。


ALL_OPEN = wallStrToWallDict(r'''
.................
____.........____
...|\......./|...
...||.......||...
...||__...__||...
...||.|\./|.||...
...||.|.X.|.||...
...||.|/.\|.||...
...||_/...\_||...
...||.......||...
___|/.......\|___
.................
.................'''.strip())
# strip()调用用于删除换行符
# 在这个多行字符串的开头。

CLOSED = {}
CLOSED['A'] = wallStrToWallDict(r'''
_____
.....
.....
.....
_____'''.strip()) # 粘贴到6,4。

CLOSED['B'] = wallStrToWallDict(r'''
.\.
..\
...
...
...
../
./.'''.strip()) # 粘贴到4,3。

CLOSED['C'] = wallStrToWallDict(r'''
___________
...........
...........
...........
...........
...........
...........
...........
...........
___________'''.strip()) # 粘贴到3，1。

CLOSED['D'] = wallStrToWallDict(r'''
./.
/..
...
...
...
\..
.\.'''.strip()) # 粘贴到10, 3。

CLOSED['E'] = wallStrToWallDict(r'''
..\..
...\_
....|
....|
....|
....|
....|
....|
....|
....|
....|
.../.
../..'''.strip()) # 粘贴到0, 0。

CLOSED['F'] = wallStrToWallDict(r'''
../..
_/...
|....
|....
|....
|....
|....
|....
|....
|....
|....
.\...
..\..'''.strip()) # 粘贴到12, 0.

def displayWallDict(wallDict):
    """在屏幕上显示由wallStrToWallDict()返回的wall字典。  """
    print(BLOCK * (wallDict['width'] + 2))
    for y in range(wallDict['height']):
        print(BLOCK, end='')
        for x in range(wallDict['width']):
            wall = wallDict[(x, y)]
            if wall == '.':
                wall = ' '
            print(wall, end='')
        print(BLOCK)  # 换行符打印block。
    print(BLOCK * (wallDict['width'] + 2))


def pasteWallDict(srcWallDict, dstWallDict, left, top):
    """将srcWallDict中的wall字典复制到dstWallDict中的wall字典之上，偏移到由左上方给出的位置。"""
    dstWallDict = copy.copy(dstWallDict)
    for x in range(srcWallDict['width']):
        for y in range(srcWallDict['height']):
            dstWallDict[(x + left, y + top)] = srcWallDict[(x, y)]
    return dstWallDict


def makeWallDict(maze, playerx, playery, playerDirection, exitx, exity):
    """根据玩家在迷宫中的位置和方向(在exitx和exity处有一个出口)，
    通过将wall字典粘贴到ALL_OPEN顶部，创建wall字典，然后返回它。  """

    # A-F“部分”(与玩家方向相关)决定了我们在迷宫中检查哪些墙壁，
    # 看看是否需要将它们粘贴到我们正在创建的wall字典上。

    if playerDirection == NORTH:
        # 各区域的地图, 与  A 相关
        # 取决于玩家 @:              BCD (玩家面向北方)
        #                               E@F
        offsets = (('A', 0, -2), ('B', -1, -1), ('C', 0, -1),
                   ('D', 1, -1), ('E', -1, 0), ('F', 1, 0))
    if playerDirection == SOUTH:
        # 各区域的地图, 与 F@E 相关
        # 取决于玩家 @:              DCB (玩家面向南方)
        #                                A
        offsets = (('A', 0, 2), ('B', 1, 1), ('C', 0, 1),
                   ('D', -1, 1), ('E', 1, 0), ('F', -1, 0))
    if playerDirection == EAST:
        # 各区域的地图, 与 EB 有关
        # 取决于玩家 @:              @CA (玩家面向东方)
        #                               FD
        offsets = (('A', 2, 0), ('B', 1, -1), ('C', 1, 0),
                   ('D', 1, 1), ('E', 0, -1), ('F', 0, 1))
    if playerDirection == WEST:
        # 各区域的地图, 与DF有关
        # 取决于玩家@:              AC@ (玩家面向西方)
        #                                BE
        offsets = (('A', -2, 0), ('B', -1, 1), ('C', -1, 0),
                   ('D', -1, -1), ('E', 0, 1), ('F', 0, -1))

    section = {}
    for sec, xOff, yOff in offsets:
        section[sec] = maze.get((playerx + xOff, playery + yOff), WALL)
        if (playerx + xOff, playery + yOff) == (exitx, exity):
            section[sec] = EXIT

    wallDict = copy.copy(ALL_OPEN)
    PASTE_CLOSED_TO = {'A': (6, 4), 'B': (4, 3), 'C': (3, 1),
                       'D': (10, 3), 'E': (0, 0), 'F': (12, 0)}
    for sec in 'ABDCEF':
        if section[sec] == WALL:
            wallDict = pasteWallDict(CLOSED[sec], wallDict,
                PASTE_CLOSED_TO[sec][0], PASTE_CLOSED_TO[sec][1])

    # 如果需要，画出退出标志:
    if section['C'] == EXIT:
        wallDict = pasteWallDict(EXIT_DICT, wallDict, 7, 9)
    if section['E'] == EXIT:
        wallDict = pasteWallDict(EXIT_DICT, wallDict, 0, 11)
    if section['F'] == EXIT:
        wallDict = pasteWallDict(EXIT_DICT, wallDict, 13, 11)

    return wallDict


print('Maze Runner 3D, by Al Sweigart al@inventwithpython.com')
print('(Maze files are generated by mazemakerrec.py)')

# 从用户处获取迷宫文件的文件名:
while True:
    print('Enter the filename of the maze (or LIST or QUIT):')
    filename = input('> ')

    #列出当前文件夹中的所有迷宫文件:
    if filename.upper() == 'LIST':
        print('Maze files found in', os.getcwd())
        for fileInCurrentFolder in os.listdir():
            if (fileInCurrentFolder.startswith('maze')
            and fileInCurrentFolder.endswith('.txt')):
                print('  ', fileInCurrentFolder)
        continue

    if filename.upper() == 'QUIT':
        sys.exit()

    if os.path.exists(filename):
        break
    print('There is no file named', filename)

# 从文件中加载迷宫:
mazeFile = open(filename)
maze = {}
lines = mazeFile.readlines()
px = None
py = None
exitx = None
exity = None
y = 0
for line in lines:
    WIDTH = len(line.rstrip())
    for x, character in enumerate(line.rstrip()):
        assert character in (WALL, EMPTY, START, EXIT), 'Invalid character at column {}, line {}'.format(x + 1, y + 1)
        if character in (WALL, EMPTY):
            maze[(x, y)] = character
        elif character == START:
            px, py = x, y
            maze[(x, y)] = EMPTY
        elif character == EXIT:
            exitx, exity = x, y
            maze[(x, y)] = EMPTY
    y += 1
HEIGHT = y

assert px != None and py != None, 'No start point in file.'
assert exitx != None and exity != None, 'No exit point in file.'
pDir = NORTH


while True:  #主游戏循环
    displayWallDict(makeWallDict(maze, px, py, pDir, exitx, exity))

    while True: # 获取用户移动。
        print('Location ({}, {})  Direction: {}'.format(px, py, pDir))
        print('                   (W)')
        print('Enter direction: (A) (D)  or QUIT.')
        move = input('> ').upper()

        if move == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        if (move not in ['F', 'L', 'R', 'W', 'A', 'D']
            and not move.startswith('T')):
            print('Please enter one of F, L, or R (or W, A, D).')
            continue

        # 根据玩家的意图移动他们:
        if move == 'F' or move == 'W':
            if pDir == NORTH and maze[(px, py - 1)] == EMPTY:
                py -= 1
                break
            if pDir == SOUTH and maze[(px, py + 1)] == EMPTY:
                py += 1
                break
            if pDir == EAST and maze[(px + 1, py)] == EMPTY:
                px += 1
                break
            if pDir == WEST and maze[(px - 1, py)] == EMPTY:
                px -= 1
                break
        elif move == 'L' or move == 'A':
            pDir = {NORTH: WEST, WEST: SOUTH,
                    SOUTH: EAST, EAST: NORTH}[pDir]
            break
        elif move == 'R' or move == 'D':
            pDir = {NORTH: EAST, EAST: SOUTH,
                    SOUTH: WEST, WEST: NORTH}[pDir]
            break
        elif move.startswith('T'):  # 作弊代码: 'T x,y'
            px, py = move.split()[1].split(',')
            px = int(px)
            py = int(py)
            break
        else:
            print('You cannot move in that direction.')

    if (px, py) == (exitx, exity):
        print('You have reached the exit! Good job!')
        print('Thanks for playing!')
        sys.exit()
