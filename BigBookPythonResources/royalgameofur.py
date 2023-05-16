"""吾尔的皇家游戏, 作者：Al Sweigart al@inventwithpython.com
一种来自美索不达米亚的有5000年历史的棋盘游戏。两名球员在冲向球门时互相撞倒对方。
更多信息在https://en.wikipedia.org/wiki/Royal_Game_of_Ur获得
此代码可在https://nostarch.com/big-book-small-python-programming获得
标签:大型，棋盘游戏，游戏，双人游戏
"""

import random, sys

X_PLAYER = 'X'
O_PLAYER = 'O'
EMPTY = ' '

# 设置空间标签的常量:
X_HOME = 'x_home'
O_HOME = 'o_home'
X_GOAL = 'x_goal'
O_GOAL = 'o_goal'

# 空格按从左到右、从上到下的顺序排列:
ALL_SPACES = 'hgfetsijklmnopdcbarq'
X_TRACK = 'HefghijklmnopstG'  # (H代表家，G代表目标。)
O_TRACK = 'HabcdijklmnopqrG'

FLOWER_SPACES = ('h', 't', 'l', 'd', 'r')

BOARD_TEMPLATE = """
                   {}           {}
                   Home              Goal
                     v                 ^
+-----+-----+-----+--v--+           +--^--+-----+
|*****|     |     |     |           |*****|     |
|* {} *<  {}  <  {}  <  {}  |           |* {} *<  {}  |
|****h|    g|    f|    e|           |****t|    s|
+--v--+-----+-----+-----+-----+-----+-----+--^--+
|     |     |     |*****|     |     |     |     |
|  {}  >  {}  >  {}  >* {} *>  {}  >  {}  >  {}  >  {}  |
|    i|    j|    k|****l|    m|    n|    o|    p|
+--^--+-----+-----+-----+-----+-----+-----+--v--+
|*****|     |     |     |           |*****|     |
|* {} *<  {}  <  {}  <  {}  |           |* {} *<  {}  |
|****d|    c|    b|    a|           |****r|    q|
+-----+-----+-----+--^--+           +--v--+-----+
                     ^                 v
                   Home              Goal
                   {}           {}
"""


def main():
    print('''The Royal Game of Ur, by Al Sweigart

This is a 5,000 year old game. Two players must move their tokens
from their home to their goal. On your turn you flip four coins and can
move one token a number of spaces equal to the heads you got.

Ur is a racing game; the first player to move all seven of their tokens
to their goal wins. To do this, tokens must travel from their home to
their goal:

            X Home      X Goal
              v           ^
+---+---+---+-v-+       +-^-+---+
|v<<<<<<<<<<<<< |       | ^<|<< |
|v  |   |   |   |       |   | ^ |
+v--+---+---+---+---+---+---+-^-+
|>>>>>>>>>>>>>>>>>>>>>>>>>>>>>^ |
|>>>>>>>>>>>>>>>>>>>>>>>>>>>>>v |
+^--+---+---+---+---+---+---+-v-+
|^  |   |   |   |       |   | v |
|^<<<<<<<<<<<<< |       | v<<<< |
+---+---+---+-^-+       +-v-+---+
              ^           v
            O Home      O Goal

If you land on an opponent's token in the middle track, it gets sent
back home. The **flower** spaces let you take another turn. Tokens in
the middle flower space are safe and cannot be landed on.''')
    input('Press Enter to begin...')

    gameBoard = getNewBoard()
    turn = O_PLAYER
    while True:  # 主游戏循环
        # 为这个回合设置一些变量:
        if turn == X_PLAYER:
            opponent = O_PLAYER
            home = X_HOME
            track = X_TRACK
            goal = X_GOAL
            opponentHome = O_HOME
        elif turn == O_PLAYER:
            opponent = X_PLAYER
            home = O_HOME
            track = O_TRACK
            goal = O_GOAL
            opponentHome = X_HOME

        displayBoard(gameBoard)

        input('It is ' + turn + '\'s turn. Press Enter to flip...')

        flipTally = 0
        print('Flips: ', end='')
        for i in range(4):  # 交换4枚金币。
            result = random.randint(0, 1)
            if result == 0:
                print('T', end='')  # 尾。
            else:
                print('H', end='')  # 首。
            if i != 3:
                print('-', end='')  # 打印分隔符
            flipTally += result
        print('  ', end='')

        if flipTally == 0:
            input('You lose a turn. Press Enter to continue...')
            turn = opponent  # 将轮次转移给另一个玩家。
            continue

        # 询问玩家的行动:
        validMoves = getValidMoves(gameBoard, turn, flipTally)

        if validMoves == []:
            print('There are no possible moves, so you lose a turn.')
            input('Press Enter to continue...')
            turn = opponent  # 将轮次转移给另一个玩家。
            continue

        while True:
            print('Select move', flipTally, 'spaces: ', end='')
            print(' '.join(validMoves) + ' quit')
            move = input('> ').lower()

            if move == 'quit':
                print('Thanks for playing!')
                sys.exit()
            if move in validMoves:
                break  # 当一个有效的步骤被选择时退出循环。

            print('That is not a valid move.')

        # 在棋盘上执行选定的步骤:
        if move == 'home':
            # 如果从家里移动，在家里减去标记:
            gameBoard[home] -= 1
            nextTrackSpaceIndex = flipTally
        else:
            gameBoard[move] = EMPTY  # 设置“from”空间为空。
            nextTrackSpaceIndex = track.index(move) + flipTally

        movingOntoGoal = nextTrackSpaceIndex == len(track) - 1
        if movingOntoGoal:
            gameBoard[goal] += 1
            # 检查玩家是否赢了:
            if gameBoard[goal] == 7:
                displayBoard(gameBoard)
                print(turn, 'has won the game!')
                print('Thanks for playing!')
                sys.exit()
        else:
            nextBoardSpace = track[nextTrackSpaceIndex]
            # 检查对手那里是否有棋子:
            if gameBoard[nextBoardSpace] == opponent:
                gameBoard[opponentHome] += 1

            # 将“to”空间设置为玩家的标记:
            gameBoard[nextBoardSpace] = turn

        # 检查玩家是否落在一个最好的空间空间，并可以再次前进:
        if nextBoardSpace in FLOWER_SPACES:
            print(turn, 'landed on a flower space and goes again.')
            input('Press Enter to continue...')
        else:
            turn = opponent  # Swap turns to the other player.

def getNewBoard():
    """
    返回表示board状态的字典。键是空格标签的字符串，值是X_PLAYER、O_PLAYER或EMPTY。
    游戏中还设置了计数器，以指示玩家家中和目标处有多少标记。
    """
    board = {X_HOME: 7, X_GOAL: 0, O_HOME: 7, O_GOAL: 0}
    # 设置每个空格为空开始:
    for spaceLabel in ALL_SPACES:
        board[spaceLabel] = EMPTY
    return board


def displayBoard(board):
    """在屏幕上显示挡板。"""
    # 通过打印许多新行来清除屏幕，所以旧的挡板不再可见。
    print('\n' * 60)

    xHomeTokens = ('X' * board[X_HOME]).ljust(7, '.')
    xGoalTokens = ('X' * board[X_GOAL]).ljust(7, '.')
    oHomeTokens = ('O' * board[O_HOME]).ljust(7, '.')
    oGoalTokens = ('O' * board[O_GOAL]).ljust(7, '.')

    #按照从左到右，从上到下的顺序，添加应该填充BOARD_TEMPLATE的字符串。
    spaces = []
    spaces.append(xHomeTokens)
    spaces.append(xGoalTokens)
    for spaceLabel in ALL_SPACES:
        spaces.append(board[spaceLabel])
    spaces.append(oHomeTokens)
    spaces.append(oGoalTokens)

    print(BOARD_TEMPLATE.format(*spaces))


def getValidMoves(board, player, flipTally):
    validMoves = []  # 包含带有可移动标记的空格。
    if player == X_PLAYER:
        opponent = O_PLAYER
        track = X_TRACK
        home = X_HOME
    elif player == O_PLAYER:
        opponent = X_PLAYER
        track = O_TRACK
        home = O_HOME

    #检查玩家是否可以从家里移动标记：
    if board[home] > 0 and board[track[flipTally]] == EMPTY:
        validMoves.append('home')

    # 检查哪些空间有玩家可以移动的标记:
    for trackSpaceIndex, space in enumerate(track):
        if space == 'H' or space == 'G' or board[space] != player:
            continue
        nextTrackSpaceIndex = trackSpaceIndex + flipTally
        if nextTrackSpaceIndex >= len(track):
            # 你必须在目标上翻转准确的移动次数，否则你无法在目标上移动。
            continue
        else:
            nextBoardSpaceKey = track[nextTrackSpaceIndex]
            if nextBoardSpaceKey == 'G':
                # 这个标记可以移出棋盘:
                validMoves.append(space)
                continue
        if board[nextBoardSpaceKey] in (EMPTY, opponent):
            # 如果下一个空间是受保护的中间空间，你只能在它为空的情况下移动到那里:
            if nextBoardSpaceKey == 'l' and board['l'] == opponent:
                continue  # 跳过此步，空间受到保护。
            validMoves.append(space)

    return validMoves


if __name__ == '__main__':
    main()
