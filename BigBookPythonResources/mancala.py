"""非洲棋, 作者：Al Sweigart al@inventwithpython.com
古代播种的游戏。
此代码可在https://nostarch.com/big-book-small-python-programming获得
标签:大型，棋盘游戏，游戏，双人游戏"""

import sys

# 玩家的pits元组:
PLAYER_1_PITS = ('A', 'B', 'C', 'D', 'E', 'F')
PLAYER_2_PITS = ('G', 'H', 'I', 'J', 'K', 'L')

# 一个键为pit，值为相反pit字典:
OPPOSITE_PIT = {'A': 'G', 'B': 'H', 'C': 'I', 'D': 'J', 'E': 'K',
                   'F': 'L', 'G': 'A', 'H': 'B', 'I': 'C', 'J': 'D',
                   'K': 'E', 'L': 'F'}

# 一个键是pit，值是下一个pit字典:
NEXT_PIT = {'A': 'B', 'B': 'C', 'C': 'D', 'D': 'E', 'E': 'F', 'F': '1',
            '1': 'L', 'L': 'K', 'K': 'J', 'J': 'I', 'I': 'H', 'H': 'G',
            'G': '2', '2': 'A'}

# 每个pit标签，从A开始逆时针顺序旋转
PIT_LABELS = 'ABCDEF1LKJIHG2'

# 在新游戏开始时，每个坑中有多少颗种子:
STARTING_NUMBER_OF_SEEDS = 4  # (!) 着把这个改成1或10。


def main():
    print('''Mancala, by Al Sweigart al@inventwithpython.com

The ancient two-player, seed-sowing game. Grab the seeds from a pit on
your side and place one in each following pit, going counterclockwise
and skipping your opponent's store. If your last seed lands in an empty
pit of yours, move the opposite pit's seeds into your store. The
goal is to get the most seeds in your store on the side of the board.
If the last placed seed is in your store, you get a free turn.

The game ends when all of one player's pits are empty. The other player
claims the remaining seeds for their store, and the winner is the one
with the most seeds.

More info at https://en.wikipedia.org/wiki/Mancala
''')
    input('Press Enter to begin...')

    gameBoard = getNewBoard()
    playerTurn = '1'  # 玩家1先走。

    while True:  # 运行一个玩家的轮次。
        #  通过打印许多新行来“清除”屏幕，，所以旧的挡板不再可见。
        print('\n' * 60)
        # 显示挡板并获得玩家的移动:
        displayBoard(gameBoard)
        playerMove = askForPlayerMove(playerTurn, gameBoard)

        # 执行玩家的移动:
        playerTurn = makeMove(gameBoard, playerTurn, playerMove)

        # 检查游戏是否结束并有玩家获胜:
        winner = checkForWinner(gameBoard)
        if winner == '1' or winner == '2':
            displayBoard(gameBoard)  # 最后一次显示电路板。
            print('Player ' + winner + ' has won!')
            sys.exit()
        elif winner == 'tie':
            displayBoard(gameBoard)  # 最后一次显示电路板。
            print('There is a tie!')
            sys.exit()


def getNewBoard():
    """返回表示开始状态下非洲棋板的字典:每个坑中有4颗种子，商店中有0颗种子。"""

    # 美化语法-使用更短的变量名:  Syntactic sugar - Use a shorter variable name:
    s = STARTING_NUMBER_OF_SEEDS

    # 创建board的数据结构，包括在商店中0个种子以及开始时在坑中种子的数量:
    return {'1': 0, '2': 0, 'A': s, 'B': s, 'C': s, 'D': s, 'E': s,
            'F': s, 'G': s, 'H': s, 'I': s, 'J': s, 'K': s, 'L': s}


def displayBoard(board):
    """在棋盘字典的基础上以字符画格式显示游戏棋盘。"""

    seedAmounts = []
    # 这个'GHIJKL21ABCDEF'字符串是pits按照从左到右和从上到下的顺序排列的:
    for pit in 'GHIJKL21ABCDEF':
        numSeedsInThisPit = str(board[pit]).rjust(2)
        seedAmounts.append(numSeedsInThisPit)

    print("""
+------+------+--<<<<<-Player 2----+------+------+------+
2      |G     |H     |I     |J     |K     |L     |      1
       |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |
S      |      |      |      |      |      |      |      S
T  {}  +------+------+------+------+------+------+  {}  T
O      |A     |B     |C     |D     |E     |F     |      O
R      |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |      R
E      |      |      |      |      |      |      |      E
+------+------+------+-Player 1->>>>>-----+------+------+

""".format(*seedAmounts))


def askForPlayerMove(playerTurn, board):
    """询问玩家他们选择在哪一边的坑里播种。 返回所选凹坑的大写字母标签作为字符串。 """

    while True:  # 不断询问玩家，直到他们进入一个有效的移动。
        # 让玩家在自己这边选择一个坑:
        if playerTurn == '1':
            print('Player 1, choose move: A-F (or QUIT)')
        elif playerTurn == '2':
            print('Player 2, choose move: G-L (or QUIT)')
        response = input('> ').upper().strip()

        # 检查玩家是否想要退出:
        if response == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        # 确保它是一个有效的pit以供选择:
        if (playerTurn == '1' and response not in PLAYER_1_PITS) or (
            playerTurn == '2' and response not in PLAYER_2_PITS
        ):
            print('Please pick a letter on your side of the board.')
            continue  # 再次询问玩家他们的行动。
        if board.get(response) == 0:
            print('Please pick a non-empty pit.')
            continue  # 再次询问玩家他们的行动。
        return response


def makeMove(board, playerTurn, pit):
    """修改棋盘的数据结构，让1号或2号玩家依次选择一个坑作为他们播种的坑。 返回'1'或'2'。  """

    seedsToSow = board[pit]  # 从选定的坑中获得数量的种子。
    board[pit] = 0  # 清空选定的坑。

    while seedsToSow > 0:  # 继续播种，直到没有种子为止。
        pit = NEXT_PIT[pit]  # 去下一个坑。
        if (playerTurn == '1' and pit == '2') or (
            playerTurn == '2' and pit == '1'
        ):
            continue  # 跳过对手的商店。
        board[pit] += 1
        seedsToSow -= 1

    # 如果最后一颗种子进入玩家的商店，他们就会再来一次。
    if (pit == playerTurn == '1') or (pit == playerTurn == '2'):
        # 最后一颗种子落在玩家的商店中;再来一轮。
        return playerTurn

    # 检查最后一粒种子是否在一个空的坑里；取另一个坑的种子。
    if playerTurn == '1' and pit in PLAYER_1_PITS and board[pit] == 1:
        oppositePit = OPPOSITE_PIT[pit]
        board['1'] += board[oppositePit]
        board[oppositePit] = 0
    elif playerTurn == '2' and pit in PLAYER_2_PITS and board[pit] == 1:
        oppositePit = OPPOSITE_PIT[pit]
        board['2'] += board[oppositePit]
        board[oppositePit] = 0

    # 返回另一个玩家作为下一个玩家:
    if playerTurn == '1':
        return '2'
    elif playerTurn == '2':
        return '1'


def checkForWinner(board):
    """看着board，如果有赢家则返回'1'或'2'，如果没有则返回'平手'或'没有赢家'。
    当玩家的坑都空了，游戏结束; 另一个玩家为他们的商店索要剩下的种子。 种子数最多的人获胜。  """

    player1Total = board['A'] + board['B'] + board['C']
    player1Total += board['D'] + board['E'] + board['F']
    player2Total = board['G'] + board['H'] + board['I']
    player2Total += board['J'] + board['K'] + board['L']

    if player1Total == 0:
        #玩家2得到他们这边所有剩余的种子：
        board['2'] += player2Total
        for pit in PLAYER_2_PITS:
            board[pit] = 0  # Set all pits to 0.
    elif player2Total == 0:
        # 玩家1得到他们这边所有剩余的种子:
        board['1'] += player1Total
        for pit in PLAYER_1_PITS:
            board[pit] = 0  # 设置所有坑为0。
    else:
        return 'no winner'  # 目前还没有赢家。

    # 游戏结束，找到得分最高的玩家。
    if board['1'] > board['2']:
        return '1'
    elif board['2'] > board['1']:
        return '2'
    else:
        return 'tie'


# 如果程序运行（而不是导入），运行游戏：
if __name__ == '__main__':
    main()
