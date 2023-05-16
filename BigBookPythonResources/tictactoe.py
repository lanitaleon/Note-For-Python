"""井字游戏，作者：Al Sweigart al@inventwithpython.com
经典的棋盘游戏。
此代码可在 https://nostarch.com/big-book-small-python-programming 获得
标签： 短，棋盘游戏，游戏，两人"""

ALL_SPACES = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
X, O, BLANK = 'X', 'O', ' '  # 字符串值的常量。


def main():
    print('Welcome to Tic-Tac-Toe!')
    gameBoard = getBlankBoard()  # 创建 TTT 板字典。
    currentPlayer, nextPlayer = X, O  # X 在前，O 在后。

    while True:  # 主游戏循环。
        # 在屏幕上显示板：
        print(getBoardStr(gameBoard))

        # 不断询问玩家，直到他们输入数字 1-9：
        move = None
        while not isValidSpace(gameBoard, move):
            print('What is {}\'s move? (1-9)'.format(currentPlayer))
            move = input('> ')
        updateBoard(gameBoard, move, currentPlayer)  # 行动起来。

        # 检查游戏是否结束：
        if isWinner(gameBoard, currentPlayer):  # 检查获胜者。
            print(getBoardStr(gameBoard))
            print(currentPlayer + ' has won the game!')
            break
        elif isBoardFull(gameBoard):  # 检查平局。
            print(getBoardStr(gameBoard))
            print('The game is a tie!')
            break
        # 切换到下一个玩家：
        currentPlayer, nextPlayer = nextPlayer, currentPlayer
    print('Thanks for playing!')


def getBlankBoard():
    """创建一个新的空白井字棋棋盘。"""
    # 空间数字映射：           1|2|3
    #                       -+-+-
    #                       4|5|6
    #                       -+-+-
    #                       7|8|9
    # 键为 1 到 9，值为 X、O 或 BLANK：
    board = {}
    for space in ALL_SPACES:
        board[space] = BLANK  # 所有空格都以空白开头。
    return board


def getBoardStr(board):
    """返回板的文本表示。"""
    return '''
      {}|{}|{}  1 2 3
      -+-+-
      {}|{}|{}  4 5 6
      -+-+-
      {}|{}|{}  7 8 9'''.format(board['1'], board['2'], board['3'],
                                board['4'], board['5'], board['6'],
                                board['7'], board['8'], board['9'])

def isValidSpace(board, space):
    """如果板上的空格是有效的空格编号，则返回 True
     并且空间是空白的。"""
    return space in ALL_SPACES and board[space] == BLANK


def isWinner(board, player):
    """如果玩家在此 TTTBoard 上获胜，则返回 True。"""
    # 此处使用的简短变量名以提高可读性：
    b, p = board, player
    # 检查 3 行、3 列和 2 条对角线上的 3 个标记。
    return ((b['1'] == b['2'] == b['3'] == p) or  # 横跨顶部
            (b['4'] == b['5'] == b['6'] == p) or  # 穿过中间
            (b['7'] == b['8'] == b['9'] == p) or  # 横跨底部
            (b['1'] == b['4'] == b['7'] == p) or  # 左下
            (b['2'] == b['5'] == b['8'] == p) or  # 中下
            (b['3'] == b['6'] == b['9'] == p) or  # 右下
            (b['3'] == b['5'] == b['7'] == p) or  # 对角线
            (b['1'] == b['5'] == b['9'] == p))    # 对角线

def isBoardFull(board):
    """如果板上的每个空间都已被占用，则返回 True。"""
    for space in ALL_SPACES:
        if board[space] == BLANK:
            return False  # 如果任何空格为空白，则返回 False。
    return True  # 没有空格是空白的，所以返回 True。


def updateBoard(board, space, mark):
    """设置板上要标记的空间。"""
    board[space] = mark


if __name__ == '__main__':
    main()  # 如果此模块正在运行，则调用 main()，但在导入时不调用。
