"""Flooder，作者：Al Sweigart al@inventwithpython.com
一款色彩缤纷的游戏，您可以尝试用单一颜色填充棋盘。 有
色盲玩家的模式。
灵感来自“淹没它！” 游戏。
此代码可在 https://nostarch.com/big-book-small-python-programming 获得
标签：大，Bext，游戏"""

import random, sys

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# 设置常量：
BOARD_WIDTH = 16  # (!) 尝试将其更改为 4 或 40。
BOARD_HEIGHT = 14  # (!) 尝试将其更改为 4 或 20。
MOVES_PER_GAME = 20  # (!) 尝试将其更改为 3 或 300。

# 色盲模式下使用的不同形状的常量：
HEART     = chr(9829)  # 字符 9829 是“♥”。
DIAMOND   = chr(9830)  # 字符 9830 是“♦”。
SPADE     = chr(9824)  # 字符 9824 是“♠”。
CLUB      = chr(9827)  # 字符 9827 是“♣”。
BALL      = chr(9679)  # 字符 9679 是“●”。
TRIANGLE  = chr(9650)  # 字符 9650 是“▲”。

BLOCK     = chr(9608)  # 字符 9608 是 “█”
LEFTRIGHT = chr(9472)  # 字符 9472 是 “─”
UPDOWN    = chr(9474)  # 字符 9474 是 “│”
DOWNRIGHT = chr(9484)  # 字符 9484 是 “┌”
DOWNLEFT  = chr(9488)  # 字符 9488 是 “┐”
UPRIGHT   = chr(9492)  # 字符 9492 是 ”└“
UPLEFT    = chr(9496)  # 字符 9496 是 “┘”
# chr() 代码列表位于 https://inventwithpython.com/chr

# 板上使用的所有颜色/形状瓷砖：
TILE_TYPES = (0, 1, 2, 3, 4, 5)
COLORS_MAP = {0: 'red', 1: 'green', 2:'blue',
              3:'yellow', 4:'cyan', 5:'purple'}
COLOR_MODE = 'color mode'
SHAPES_MAP = {0: HEART, 1: TRIANGLE, 2: DIAMOND,
              3: BALL, 4: CLUB, 5: SPADE}
SHAPE_MODE = 'shape mode'


def main():
    bext.bg('black')
    bext.fg('white')
    bext.clear()
    print('''Flooder, by Al Sweigart al@inventwithpython.com

Set the upper left color/shape, which fills in all the
adjacent squares of that color/shape. Try to make the
entire board the same color/shape.''')

    print('Do you want to play in colorblind mode? Y/N')
    response = input('> ')
    if response.upper().startswith('Y'):
        displayMode = SHAPE_MODE
    else:
        displayMode = COLOR_MODE

    gameBoard = getNewBoard()
    movesLeft = MOVES_PER_GAME

    while True:  # 主游戏循环。
        displayBoard(gameBoard, displayMode)

        print('Moves left:', movesLeft)
        playerMove = askForPlayerMove(displayMode)
        changeTile(playerMove, gameBoard, 0, 0)
        movesLeft -= 1

        if hasWon(gameBoard):
            displayBoard(gameBoard, displayMode)
            print('You have won!')
            break
        elif movesLeft == 0:
            displayBoard(gameBoard, displayMode)
            print('You have run out of moves!')
            break


def getNewBoard():
    """返回一个新的 Flood It 板的字典。"""

    # 键是 (x, y) 元组，值是该位置的图块。
    board = {}

    # 为板创建随机颜色。
    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT):
            board[(x, y)] = random.choice(TILE_TYPES)

    # 制作几个与其邻居相同的瓷砖。 这会创建相同颜色/形状的组。
    for i in range(BOARD_WIDTH * BOARD_HEIGHT):
        x = random.randint(0, BOARD_WIDTH - 2)
        y = random.randint(0, BOARD_HEIGHT - 1)
        board[(x + 1, y)] = board[(x, y)]
    return board


def displayBoard(board, displayMode):
    """在屏幕上显示板。"""
    bext.fg('white')
    # 显示板的顶部边缘：
    print(DOWNRIGHT + (LEFTRIGHT * BOARD_WIDTH) + DOWNLEFT)

    # 显示每一行：
    for y in range(BOARD_HEIGHT):
        bext.fg('white')
        if y == 0:  # 第一行以“>”开头。
            print('>', end='')
        else:  # 后面的行以白色垂直线开始。
            print(UPDOWN, end='')

        # 显示此行中的每个图块：
        for x in range(BOARD_WIDTH):
            bext.fg(COLORS_MAP[board[(x, y)]])
            if displayMode == COLOR_MODE:
                print(BLOCK, end='')
            elif displayMode == SHAPE_MODE:
                print(SHAPES_MAP[board[(x, y)]], end='')

        bext.fg('white')
        print(UPDOWN)  # 行以白色垂直线结束。
    # 显示板的底部边缘：
    print(UPRIGHT + (LEFTRIGHT * BOARD_WIDTH) + UPLEFT)


def askForPlayerMove(displayMode):
    """让玩家选择一种颜色来绘制左上角的瓷砖。"""
    while True:
        bext.fg('white')
        print('Choose one of ', end='')

        if displayMode == COLOR_MODE:
            bext.fg('red')
            print('(R)ed ', end='')
            bext.fg('green')
            print('(G)reen ', end='')
            bext.fg('blue')
            print('(B)lue ', end='')
            bext.fg('yellow')
            print('(Y)ellow ', end='')
            bext.fg('cyan')
            print('(C)yan ', end='')
            bext.fg('purple')
            print('(P)urple ', end='')
        elif displayMode == SHAPE_MODE:
            bext.fg('red')
            print('(H)eart, ', end='')
            bext.fg('green')
            print('(T)riangle, ', end='')
            bext.fg('blue')
            print('(D)iamond, ', end='')
            bext.fg('yellow')
            print('(B)all, ', end='')
            bext.fg('cyan')
            print('(C)lub, ', end='')
            bext.fg('purple')
            print('(S)pade, ', end='')
        bext.fg('white')
        print('or QUIT:')
        response = input('> ').upper()
        if response == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        if displayMode == COLOR_MODE and response in tuple('RGBYCP'):
            # 根据响应返回图块类型编号：
            return {'R': 0, 'G': 1, 'B': 2,
                'Y': 3, 'C': 4, 'P': 5}[response]
        if displayMode == SHAPE_MODE and response in tuple('HTDBCS'):
            # 根据响应返回图块类型编号：
            return {'H': 0, 'T': 1, 'D':2,
                'B': 3, 'C': 4, 'S': 5}[response]


def changeTile(tileType, board, x, y, charToChange=None):
    """使用递归洪水填充更改图块的颜色/形状算法。"""
    if x == 0 and y == 0:
        charToChange = board[(x, y)]
        if tileType == charToChange:
            return  # 基本情况：已经是同一个图块。

    board[(x, y)] = tileType

    if x > 0 and board[(x - 1, y)] == charToChange:
        # 递归案例：更改左邻居的瓦片：
        changeTile(tileType, board, x - 1, y, charToChange)
    if y > 0 and board[(x, y - 1)] == charToChange:
        # 递归案例：更改顶部邻居的瓦片：
        changeTile(tileType, board, x, y - 1, charToChange)
    if x < BOARD_WIDTH - 1 and board[(x + 1, y)] == charToChange:
        # 递归案例：更改右邻居的瓦片：
        changeTile(tileType, board, x + 1, y, charToChange)
    if y < BOARD_HEIGHT - 1 and board[(x, y + 1)] == charToChange:
        # 递归案例：更改底部邻居的瓦片：
        changeTile(tileType, board, x, y + 1, charToChange)


def hasWon(board):
    """如果整个板子是一种颜色/形状，则返回 True。"""
    tile = board[(0, 0)]

    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT):
            if board[(x, y)] != tile:
                return False
    return True


# 如果此程序已运行（而不是导入），请运行游戏：
if __name__ == '__main__':
    main()
