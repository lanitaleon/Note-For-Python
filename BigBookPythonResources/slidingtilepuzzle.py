"""滑块拼图, 作者：Al Sweigart al@inventwithpython.com
将有编号的瓷砖按正确顺序滑动。
此代码可在https://nostarch.com/big-book-small-python-programming获得
标签:大型，游戏，谜题"""

import random, sys

BLANK = '  '  # 注意:这个字符串是两个空格，而不是一个。


def main():
    print('''Sliding Tile Puzzle, by Al Sweigart al@inventwithpython.com

    Use the WASD keys to move the tiles
    back into their original order:
           1  2  3  4
           5  6  7  8
           9 10 11 12
          13 14 15   ''')
    input('Press Enter to begin...')

    gameBoard = getNewPuzzle()

    while True:
        displayBoard(gameBoard)
        playerMove = askForPlayerMove(gameBoard)
        makeMove(gameBoard, playerMove)

        if gameBoard == getNewBoard():
            print('You won!')
            sys.exit()


def getNewBoard():
    """返回一个代表着新拼图列表的列表。"""
    return [['1 ', '5 ', '9 ', '13'], ['2 ', '6 ', '10', '14'],
            ['3 ', '7 ', '11', '15'], ['4 ', '8 ', '12', BLANK]]


def displayBoard(board):
    """在屏幕上显示给定的board。"""
    labels = [board[0][0], board[1][0], board[2][0], board[3][0],
              board[0][1], board[1][1], board[2][1], board[3][1],
              board[0][2], board[1][2], board[2][2], board[3][2],
              board[0][3], board[1][3], board[2][3], board[3][3]]
    boardToDraw = """
+------+------+------+------+
|      |      |      |      |
|  {}  |  {}  |  {}  |  {}  |
|      |      |      |      |
+------+------+------+------+
|      |      |      |      |
|  {}  |  {}  |  {}  |  {}  |
|      |      |      |      |
+------+------+------+------+
|      |      |      |      |
|  {}  |  {}  |  {}  |  {}  |
|      |      |      |      |
+------+------+------+------+
|      |      |      |      |
|  {}  |  {}  |  {}  |  {}  |
|      |      |      |      |
+------+------+------+------+
""".format(*labels)
    print(boardToDraw)


def findBlankSpace(board):
    """返回空白空间位置的(x, y)元组。"""
    for x in range(4):
        for y in range(4):
            if board[x][y] == '  ':
                return (x, y)


def askForPlayerMove(board):
    """让玩家选择要滑动的砖块。"""
    blankx, blanky = findBlankSpace(board)

    w = 'W' if blanky != 3 else ' '
    a = 'A' if blankx != 3 else ' '
    s = 'S' if blanky != 0 else ' '
    d = 'D' if blankx != 0 else ' '

    while True:
        print('                          ({})'.format(w))
        print('Enter WASD (or QUIT): ({}) ({}) ({})'.format(a, s, d))

        response = input('> ').upper()
        if response == 'QUIT':
            sys.exit()
        if response in (w + a + s + d).replace(' ', ''):
            return response


def makeMove(board, move):
    """在给定的棋盘上执行给定的走法。"""
    # 注意:这个函数假设移动是有效的。
    bx, by = findBlankSpace(board)

    if move == 'W':
        board[bx][by], board[bx][by+1] = board[bx][by+1], board[bx][by]
    elif move == 'A':
        board[bx][by], board[bx+1][by] = board[bx+1][by], board[bx][by]
    elif move == 'S':
        board[bx][by], board[bx][by-1] = board[bx][by-1], board[bx][by]
    elif move == 'D':
        board[bx][by], board[bx-1][by] = board[bx-1][by], board[bx][by]


def makeRandomMove(board):
    """在一个随机的方向上做一个滑动。"""
    blankx, blanky = findBlankSpace(board)
    validMoves = []
    if blanky != 3:
        validMoves.append('W')
    if blankx != 3:
        validMoves.append('A')
    if blanky != 0:
        validMoves.append('S')
    if blankx != 0:
        validMoves.append('D')

    makeMove(board, random.choice(validMoves))


def getNewPuzzle(moves=200):
    """通过从一个已解决的状态制作随机幻灯片来获得一个新拼图。"""
    board = getNewBoard()

    for i in range(moves):
        makeRandomMove(board)
    return board


# 如果程序运行(而不是导入)，运行游戏:
if __name__ == '__main__':
    main()
