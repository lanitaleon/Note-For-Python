"""二四十八，Al Sweigart al@inventwithpython.com
一个滑动瓷砖游戏，结合指数增加的数字。
灵感来自 Gabriele Cirulli 的 2048，它是 Veewo Studios 的克隆
1024，这又是三胞胎的分身！ 游戏。
更多信息请访问 https://en.wikipedia.org/wiki/2048_(video_game)
此代码可在 https://nostarch.com/big-book-small-python-programming 获得
标签：大，游戏，拼图"""

import random, sys

# 设置常量：
BLANK = ''  # 表示板上空白的值。


def main():
    print('''Twenty Forty-Eight, by Al Sweigart al@inventwithpython.com

Slide all the tiles on the board in one of four directions. Tiles with
like numbers will combine into larger-numbered tiles. A new 2 tile is
added to the board on each move. You win if you can create a 2048 tile.
You lose if the board fills up the tiles before then.''')
    input('Press Enter to begin...')

    gameBoard = getNewBoard()

    while True:  # 主游戏循环。
        drawBoard(gameBoard)
        print('Score:', getScore(gameBoard))
        playerMove = askForPlayerMove()
        gameBoard = makeMove(gameBoard, playerMove)
        addTwoToBoard(gameBoard)

        if isFull(gameBoard):
            drawBoard(gameBoard)
            print('Game Over - Thanks for playing!')
            sys.exit()


def getNewBoard():
    """返回表示板的新数据结构。

    它是一个字典，其中包含 (x, y) 元组的键和该空间的图块值。
    图块是一个 2 的幂整数或空白。
     坐标布置为：
       X0 1 2 3
      Y+-+-+-+-+
      0| | | | |
       +-+-+-+-+
      1| | | | |
       +-+-+-+-+
      2| | | | |
       +-+-+-+-+
      3| | | | |
       +-+-+-+-+"""

    newBoard = {}  # 包含要返回的板数据结构。
    # 遍历所有可能的空间并将所有图块设置为空白：
    for x in range(4):
        for y in range(4):
            newBoard[(x, y)] = BLANK

    # 为两个起始 2 选择两个随机空格：
    startingTwosPlaced = 0  # 选择的起始空格数。
    while startingTwosPlaced < 2:  # 重复重复的空格。
        randomSpace = (random.randint(0, 3), random.randint(0, 3))
        # 确保随机选择的空间尚未被占用：
        if newBoard[randomSpace] == BLANK:
            newBoard[randomSpace] = 2
            startingTwosPlaced = startingTwosPlaced + 1

    return newBoard


def drawBoard(board):
    """在屏幕上绘制板数据结构。"""

    # 从左到右，从上到下，遍历每个可能的空间
    # 创建每个空间的标签应该是什么的列表。
    labels = []  # 该磁贴的数字/空白的字符串列表。
    for y in range(4):
        for x in range(4):
            tile = board[(x, y)]  # 在这个空间拿到瓷砖。
            # 确保标签长度为 5 个空格：
            labelForThisTile = str(tile).center(5)
            labels.append(labelForThisTile)

    # {} 替换为该磁贴的标签：
    print("""
+-----+-----+-----+-----+
|     |     |     |     |
|{}|{}|{}|{}|
|     |     |     |     |
+-----+-----+-----+-----+
|     |     |     |     |
|{}|{}|{}|{}|
|     |     |     |     |
+-----+-----+-----+-----+
|     |     |     |     |
|{}|{}|{}|{}|
|     |     |     |     |
+-----+-----+-----+-----+
|     |     |     |     |
|{}|{}|{}|{}|
|     |     |     |     |
+-----+-----+-----+-----+
""".format(*labels))


def getScore(board):
    """返回棋盘数据结构上所有图块的总和。"""
    score = 0
    # 循环遍历每个空间并将瓷砖添加到分数中：
    for x in range(4):
        for y in range(4):
            # 只在分数中添加非空白图块：
            if board[(x, y)] != BLANK:
                score = score + board[(x, y)]
    return score


def combineTilesInColumn(column):
    """该列是四个磁贴的列表。 索引 0 是“底部”
     列和瓷砖被“下拉”并合并，如果它们是
     相同的。 例如， combineTilesInColumn([2, BLANK, 2, BLANK])
     返回 [4, BLANK, BLANK, BLANK]。"""

    # 仅将列中的数字（而不是空白）复制到 combineTiles
    combinedTiles = []  # 列中非空白图块的列表。
    for i in range(4):
        if column[i] != BLANK:
            combinedTiles.append(column[i])

    # 继续添加空白直到有 4 个图块：
    while len(combinedTiles) < 4:
        combinedTiles.append(BLANK)

    # 如果“上面”的数字相同，则合并数字，并将其加倍。
    for i in range(3):  # 跳过索引 3：它是最顶层的空间。
        if combinedTiles[i] == combinedTiles[i + 1]:
            combinedTiles[i] *= 2  # 将图块中的数字加倍。
            # 将其上方的瓷砖向下移动一格：
            for aboveIndex in range(i + 1, 3):
                combinedTiles[aboveIndex] = combinedTiles[aboveIndex + 1]
            combinedTiles[3] = BLANK  # 最上面的空间总是空白。
    return combinedTiles


def makeMove(board, move):
    """在棋盘上进行移动。

    移动参数是“W”、“A”、“S”或“D”，函数
     返回结果板数据结构。"""

    # 棋盘分为四列，各不相同
    # 取决于移动的方向：
    if move == 'W':
        allColumnsSpaces = [[(0, 0), (0, 1), (0, 2), (0, 3)],
                            [(1, 0), (1, 1), (1, 2), (1, 3)],
                            [(2, 0), (2, 1), (2, 2), (2, 3)],
                            [(3, 0), (3, 1), (3, 2), (3, 3)]]
    elif move == 'A':
        allColumnsSpaces = [[(0, 0), (1, 0), (2, 0), (3, 0)],
                            [(0, 1), (1, 1), (2, 1), (3, 1)],
                            [(0, 2), (1, 2), (2, 2), (3, 2)],
                            [(0, 3), (1, 3), (2, 3), (3, 3)]]
    elif move == 'S':
        allColumnsSpaces = [[(0, 3), (0, 2), (0, 1), (0, 0)],
                            [(1, 3), (1, 2), (1, 1), (1, 0)],
                            [(2, 3), (2, 2), (2, 1), (2, 0)],
                            [(3, 3), (3, 2), (3, 1), (3, 0)]]
    elif move == 'D':
        allColumnsSpaces = [[(3, 0), (2, 0), (1, 0), (0, 0)],
                            [(3, 1), (2, 1), (1, 1), (0, 1)],
                            [(3, 2), (2, 2), (1, 2), (0, 2)],
                            [(3, 3), (2, 3), (1, 3), (0, 3)]]

    # 移动后的棋盘数据结构：
    boardAfterMove = {}
    for columnSpaces in allColumnsSpaces:  # 循环遍历所有 4 列。
        # 获取该列的瓦片（第一次是列的“底部”）：
        firstTileSpace = columnSpaces[0]
        secondTileSpace = columnSpaces[1]
        thirdTileSpace = columnSpaces[2]
        fourthTileSpace = columnSpaces[3]

        firstTile = board[firstTileSpace]
        secondTile = board[secondTileSpace]
        thirdTile = board[thirdTileSpace]
        fourthTile = board[fourthTileSpace]

        # 形成列并组合其中的图块：
        column = [firstTile, secondTile, thirdTile, fourthTile]
        combinedTilesColumn = combineTilesInColumn(column)

        # 使用组合图块设置新的板数据结构：
        boardAfterMove[firstTileSpace] = combinedTilesColumn[0]
        boardAfterMove[secondTileSpace] = combinedTilesColumn[1]
        boardAfterMove[thirdTileSpace] = combinedTilesColumn[2]
        boardAfterMove[fourthTileSpace] = combinedTilesColumn[3]

    return boardAfterMove


def askForPlayerMove():
    """询问玩家下一步行动（或退出）的方向。

    确保他们输入有效的移动：“W”、“A”、“S”或“D”。"""
    print('Enter move: (WASD or Q to quit)')
    while True:  # 继续循环，直到他们进入有效的移动。
        move = input('> ').upper()
        if move == 'Q':
            # 结束程序：
            print('Thanks for playing!')
            sys.exit()

        # 要么返回有效的移动，要么循环返回并再次询问：
        if move in ('W', 'A', 'S', 'D'):
            return move
        else:
            print('Enter one of "W", "A", "S", "D", or "Q".')


def addTwoToBoard(board):
    """将新的 2 块随机添加到板上。"""
    while True:
        randomSpace = (random.randint(0, 3), random.randint(0, 3))
        if board[randomSpace] == BLANK:
            board[randomSpace] = 2
            return  # 找到一个非空白的瓷砖后返回。


def isFull(board):
    """如果电路板数据结构没有空格，则返回 True。"""
    # 遍历板上的每个空间：
    for x in range(4):
        for y in range(4):
            # 如果空格为空，则返回 False：
            if board[(x, y)] == BLANK:
                return False
    return True  # 没有空格是空白的，所以返回 True。


# 如果此程序已运行（而不是导入），请运行游戏：
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # 当按下 Ctrl-C 时，结束程序。
