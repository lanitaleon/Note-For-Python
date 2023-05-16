"""饥饿的机器人, 作者：Al Sweigart al@inventwithpython.com
通过让饥饿的机器人碰撞到彼此脱离他们。
此代码可在https://nostarch.com/big-book-small-python-programming获得
标签: 大，游戏"""

import random, sys

# 建立常数:
WIDTH = 40           # (!) 试着把它改成70或10。
HEIGHT = 20          # (!) 试着把它改成10.
NUM_ROBOTS = 10      # (!) 试着把它改成1或30.
NUM_TELEPORTS = 2    # (!) 试着把它改成0或9999.
NUM_DEAD_ROBOTS = 2  # (!) 试着把它改成0或20.
NUM_WALLS = 100      # (!) 试着把它改成0或300.

EMPTY_SPACE = ' '    # (!) 试着把它改成 '.'.
PLAYER = '@'         # (!) T试着把它改成'R'.
ROBOT = 'R'          # (!) 试着把它改成 '@'.
DEAD_ROBOT = 'X'     # (!) 试着把它改成'R'.

# (!) 试着把它改成'#'或'O'或' ':
WALL = chr(9617)  # 字符 9617 is '░'


def main():
    print('''Hungry Robots, by Al Sweigart al@inventwithpython.com

You are trapped in a maze with hungry robots! You don't know why robots
need to eat, but you don't want to find out. The robots are badly
programmed and will move directly toward you, even if blocked by walls.
You must trick the robots into crashing into each other (or dead robots)
without being caught. You have a personal teleporter device, but it only
has enough battery for {} trips. Keep in mind, you and robots can slip
through the corners of two diagonal walls!
'''.format(NUM_TELEPORTS))

    input('Press Enter to begin...')

    # 创建一个新游戏
    board = getNewBoard()
    robots = addRobots(board)
    playerPosition = getRandomEmptySpace(board, robots)
    while True:  # 主游戏循环。
        displayBoard(board, robots, playerPosition)

        if len(robots) == 0:  # 检查玩家是否赢
            print('All the robots have crashed into each other and you')
            print('lived to tell the tale! Good job!')
            sys.exit()

        # 移动玩家和机器人：
        playerPosition = askForPlayerMove(board, robots, playerPosition)
        robots = moveRobots(board, robots, playerPosition)

        for x, y in robots:  # 键查玩家是否失踪。
            if (x, y) == playerPosition:
                displayBoard(board, robots, playerPosition)
                print('You have been caught by a robot!')
                sys.exit()


def getNewBoard():
    """返回代表该board字典.键是(x, y)整数索引元组，用于表示板位置，其值是
    WALL, EMPTY_SPACE,或DEAD_ROBOT.字典中也有键“传送”，
    表示玩家还剩多少次传送机会，这些存活的机器人会在挡board的字典中被分开的存储。"""
    board = {'teleports': NUM_TELEPORTS}

    # 创建一个空板：
    for x in range(WIDTH):
        for y in range(HEIGHT):
            board[(x, y)] = EMPTY_SPACE

    # 在挡板的边缘添加墙壁:
    for x in range(WIDTH):
        board[(x, 0)] = WALL  # 布置上盘。
        board[(x, HEIGHT - 1)] = WALL  # 布置底盘。
    for y in range(HEIGHT):
        board[(0, y)] = WALL  # 布置左墙。
        board[(WIDTH - 1, y)] = WALL  # 布置右墙。

    # 添加随机墙壁:
    for i in range(NUM_WALLS):
        x, y = getRandomEmptySpace(board, [])
        board[(x, y)] = WALL

    # 添加起始死亡机器人:
    for i in range(NUM_DEAD_ROBOTS):
        x, y = getRandomEmptySpace(board, [])
        board[(x, y)] = DEAD_ROBOT
    return board


def getRandomEmptySpace(board, robots):
    """返回一个(x, y)整数元组，表示board上的一个空的空间。"""
    while True:
        randomX = random.randint(1, WIDTH - 2)
        randomY = random.randint(1, HEIGHT - 2)
        if isEmpty(randomX, randomY, board, robots):
            break
    return (randomX, randomY)


def isEmpty(x, y, board, robots):
    """如果board上的(x, y)为空，并且没有机器人，则返回True。"""
    return board[(x, y)] == EMPTY_SPACE and (x, y) not in robots


def addRobots(board):
    """将NUM_ROBOTS数量添加到board上的空白区域，并返回机器人现在所在的这些(x, y)空间的列表。"""
    robots = []
    for i in range(NUM_ROBOTS):
        x, y = getRandomEmptySpace(board, robots)
        robots.append((x, y))
    return robots


def displayBoard(board, robots, playerPosition):
    """在屏幕上显示挡板、机器人和玩家。"""
    # 循环遍历board上的每个空格:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            # 画出适当的字符:
            if board[(x, y)] == WALL:
                print(WALL, end='')
            elif board[(x, y)] == DEAD_ROBOT:
                print(DEAD_ROBOT, end='')
            elif (x, y) == playerPosition:
                print(PLAYER, end='')
            elif (x, y) in robots:
                print(ROBOT, end='')
            else:
                print(EMPTY_SPACE, end='')
        print()  # 打印出一行新行。


def askForPlayerMove(board, robots, playerPosition):
    """返回玩家下一步移动位置的(x, y)整数元组，给定他们当前的位置和挡板的墙壁。"""
    playerX, playerY = playerPosition

    # 找到那些不会被墙挡住的方向:
    q = 'Q' if isEmpty(playerX - 1, playerY - 1, board, robots) else ' '
    w = 'W' if isEmpty(playerX + 0, playerY - 1, board, robots) else ' '
    e = 'E' if isEmpty(playerX + 1, playerY - 1, board, robots) else ' '
    d = 'D' if isEmpty(playerX + 1, playerY + 0, board, robots) else ' '
    c = 'C' if isEmpty(playerX + 1, playerY + 1, board, robots) else ' '
    x = 'X' if isEmpty(playerX + 0, playerY + 1, board, robots) else ' '
    z = 'Z' if isEmpty(playerX - 1, playerY + 1, board, robots) else ' '
    a = 'A' if isEmpty(playerX - 1, playerY + 0, board, robots) else ' '
    allMoves = (q + w + e + d + c + x + a + z + 'S')

    while True:
        # 得到玩家的位置变动：
        print('(T)eleports remaining: {}'.format(board["teleports"]))
        print('                    ({}) ({}) ({})'.format(q, w, e))
        print('                    ({}) (S) ({})'.format(a, d))
        print('Enter move or QUIT: ({}) ({}) ({})'.format(z, x, c))

        move = input('> ').upper()
        if move == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif move == 'T' and board['teleports'] > 0:
            # 将玩家传送到一个随机的空白空间:
            board['teleports'] -= 1
            return getRandomEmptySpace(board, robots)
        elif move != '' and move in allMoves:
            # 根据他们的移动返回新的玩家位置:
            return {'Q': (playerX - 1, playerY - 1),
                    'W': (playerX + 0, playerY - 1),
                    'E': (playerX + 1, playerY - 1),
                    'D': (playerX + 1, playerY + 0),
                    'C': (playerX + 1, playerY + 1),
                    'X': (playerX + 0, playerY + 1),
                    'Z': (playerX - 1, playerY + 1),
                    'A': (playerX - 1, playerY + 0),
                    'S': (playerX, playerY)}[move]


def moveRobots(board, robotPositions, playerPosition):
    """在它们试图移动到玩家之后，返回一个(x, y)元组的新机器人位置列表。"""
    playerx, playery = playerPosition
    nextRobotPositions = []

    while len(robotPositions) > 0:
        robotx, roboty = robotPositions[0]

        # 确定机器人移动的方向。
        if robotx < playerx:
            movex = 1  # 向右移动
        elif robotx > playerx:
            movex = -1  # 向左移动。
        elif robotx == playerx:
            movex = 0  # 不要水平低移动。

        if roboty < playery:
            movey = 1  # 向上移动。
        elif roboty > playery:
            movey = -1  # 向下移动。
        elif roboty == playery:
            movey = 0  # 不要竖直的移动。

        # 检查机器人是否会撞到墙上，并调整路线:
        if board[(robotx + movex, roboty + movey)] == WALL:
            # 机器人会撞到墙，所以想出一个新动作:
            if board[(robotx + movex, roboty)] == EMPTY_SPACE:
                movey = 0  # 机器人不能水平移动。
            elif board[(robotx, roboty + movey)] == EMPTY_SPACE:
                movex = 0  # 机器人不能竖直移动。
            else:
                # 机器人不能移动。
                movex = 0
                movey = 0
        newRobotx = robotx + movex
        newRoboty = roboty + movey

        if (board[(robotx, roboty)] == DEAD_ROBOT
            or board[(newRobotx, newRoboty)] == DEAD_ROBOT):
            # 机器人相撞了，把它移走。
            del robotPositions[0]
            continue

        # 检查它是否撞到了一个机器人，然后两个机器人都损毁了。
        if (newRobotx, newRoboty) in nextRobotPositions:
            board[(newRobotx, newRoboty)] = DEAD_ROBOT
            nextRobotPositions.remove((newRobotx, newRoboty))
        else:
            nextRobotPositions.append((newRobotx, newRoboty))

        # 当机器人移动时，将其从机器人位置中移除。
        del robotPositions[0]
    return nextRobotPositions


# 如果程序运行（而不是导入），运行游戏：
if __name__ == '__main__':
    main()
