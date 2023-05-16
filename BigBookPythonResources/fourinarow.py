"""连续四个，作者：Al Sweigart al@inventwithpython.com
一个图块掉落游戏，连续获得四个，类似于连接四个。
此代码可在 https://nostarch.com/big-book-small-python-programming 获得
标签: 大型, 游戏, 棋盘游戏, 两人"""

import sys

# 用于显示板的常量：
EMPTY_SPACE = '.'  # 句号比空格更容易计数。
PLAYER_X = 'X'
PLAYER_O = 'O'

# 注意：如果 BOARD_WIDTH 更改，则更新 displayBoard() & COLUMN_LABELS。
BOARD_WIDTH = 7
BOARD_HEIGHT = 6
COLUMN_LABELS = ('1', '2', '3', '4', '5', '6', '7')
assert len(COLUMN_LABELS) == BOARD_WIDTH


def main():
    print("""Four in a Row, by Al Sweigart al@inventwithpython.com

Two players take turns dropping tiles into one of seven columns, trying
to make four in a row horizontally, vertically, or diagonally.
""")

    # 设置新游戏：
    gameBoard = getNewBoard()
    playerTurn = PLAYER_X

    while True:  # 运行玩家的回合。
        # 显示棋盘并获取玩家的移动：
        displayBoard(gameBoard)
        playerMove = askForPlayerMove(playerTurn, gameBoard)
        gameBoard[playerMove] = playerTurn

        # 检查获胜或平局：
        if isWinner(playerTurn, gameBoard):
            displayBoard(gameBoard)  # 最后一次显示该棋盘。
            print('Player ' + playerTurn + ' has won!')
            sys.exit()
        elif isFull(gameBoard):
            displayBoard(gameBoard)  # 最后一次显示该棋盘。
            print('There is a tie!')
            sys.exit()

        # 切换到其他玩家：
        if playerTurn == PLAYER_X:
            playerTurn = PLAYER_O
        elif playerTurn == PLAYER_O:
            playerTurn = PLAYER_X


def getNewBoard():
    """返回一个代表一行有四个棋子的字典。

    键是两个整数的 (columnIndex, rowIndex) 元组，并且
     值是“X”、“O”或“.”之一。 （空白）字符串。"""
    board = {}
    for columnIndex in range(BOARD_WIDTH):
        for rowIndex in range(BOARD_HEIGHT):
            board[(columnIndex, rowIndex)] = EMPTY_SPACE
    return board


def displayBoard(board):
    """在屏幕上显示棋盘及其图块。"""

    '''Prepare a list to pass to the format() string method for the
    board template. The list holds all of the board's tiles (and empty
    spaces) going left to right, top to bottom:'''
    tileChars = []
    for rowIndex in range(BOARD_HEIGHT):
        for columnIndex in range(BOARD_WIDTH):
            tileChars.append(board[(columnIndex, rowIndex)])

    # 显示棋盘：
    print("""
     1234567
    +-------+
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    +-------+""".format(*tileChars))


def askForPlayerMove(playerTile, board):
    """让玩家选择棋盘上的一列将图块放入其中。

    返回图块所在的 (column, row) 的元组。"""
    while True:  # 不断询问玩家，直到他们输入有效的移动。
        print('Player {}, enter a column or QUIT:'.format(playerTile))
        response = input('> ').upper().strip()

        if response == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        if response not in COLUMN_LABELS:
            print('Enter a number from 1 to {}.'.format(BOARD_WIDTH))
            continue  # 再次询问玩家他们的举动。

        columnIndex = int(response) - 1  # -1 表示基于 0 的索引。

        # 如果列已满，请再次请求移动：
        if board[(columnIndex, 0)] != EMPTY_SPACE:
            print('That column is full, select another one.')
            continue  # 再次询问玩家他们的举动。

        # 从底部开始，找到第一个空白区域。
        for rowIndex in range(BOARD_HEIGHT - 1, -1, -1):
            if board[(columnIndex, rowIndex)] == EMPTY_SPACE:
                return (columnIndex, rowIndex)


def isFull(board):
    """如果 `board` 没有空格，则返回真，否则返回
     返回假。"""
    for rowIndex in range(BOARD_HEIGHT):
        for columnIndex in range(BOARD_WIDTH):
            if board[(columnIndex, rowIndex)] == EMPTY_SPACE:
                return False  # 找到一个空的空间，所以返回 False。
    return True  # 所有空间都已满。


def isWinner(playerTile, board):
    """如果 `playerTile` 在 `board` 上连续有四个图块，则返回 True，
     否则返回 False。"""

    # 浏览整个棋盘，检查是否有四个在一排：
    for columnIndex in range(BOARD_WIDTH - 3):
        for rowIndex in range(BOARD_HEIGHT):
            # Check for horizontal four-in-a-row going right:   检查水平向右的四个棋子：
            tile1 = board[(columnIndex, rowIndex)]
            tile2 = board[(columnIndex + 1, rowIndex)]
            tile3 = board[(columnIndex + 2, rowIndex)]
            tile4 = board[(columnIndex + 3, rowIndex)]
            if tile1 == tile2 == tile3 == tile4 == playerTile:
                return True

    for columnIndex in range(BOARD_WIDTH):
        for rowIndex in range(BOARD_HEIGHT - 3):
            # 检查垂直向下在的四个棋子：
            tile1 = board[(columnIndex, rowIndex)]
            tile2 = board[(columnIndex, rowIndex + 1)]
            tile3 = board[(columnIndex, rowIndex + 2)]
            tile4 = board[(columnIndex, rowIndex + 3)]
            if tile1 == tile2 == tile3 == tile4 == playerTile:
                return True

    for columnIndex in range(BOARD_WIDTH - 3):
        for rowIndex in range(BOARD_HEIGHT - 3):
            # 检查右下对角线的四个棋子：
            tile1 = board[(columnIndex, rowIndex)]
            tile2 = board[(columnIndex + 1, rowIndex + 1)]
            tile3 = board[(columnIndex + 2, rowIndex + 2)]
            tile4 = board[(columnIndex + 3, rowIndex + 3)]
            if tile1 == tile2 == tile3 == tile4 == playerTile:
                return True

            # 检查左下对角线的四个棋子：
            tile1 = board[(columnIndex + 3, rowIndex)]
            tile2 = board[(columnIndex + 2, rowIndex + 1)]
            tile3 = board[(columnIndex + 1, rowIndex + 2)]
            tile4 = board[(columnIndex, rowIndex + 3)]
            if tile1 == tile2 == tile3 == tile4 == playerTile:
                return True
    return False


# 如果程序运行（而不是导入），运行游戏：
if __name__ == '__main__':
    main()
