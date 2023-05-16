"""蚀刻抽屉，作者：Al Sweigart al@inventwithpython.com
一个艺术程序，它在屏幕周围使用WASD 键画一条连续线。
灵感来自 Etch A Sketch 玩具。

例如，您可以绘制希尔伯特曲线分形：
SDWDDSASDSAAWASSDSASSDWDSDWWAWDDDSASSDWDSDWWAWDWWASAAWDWAWDDSDW

或者更大的希尔伯特曲线分形：
DDSAASSDDWDDSDDWWAAWDDDDSDDWDDDDSAASDDSAAAAWAASSSDDWDDDDSAASDDSAAAAWA
ASAAAAWDDWWAASAAWAASSDDSAASSDDWDDDDSAASDDSAAAAWAASSDDSAASSDDWDDSDDWWA
AWDDDDDDSAASSDDWDDSDDWWAAWDDWWAASAAAAWDDWAAWDDDDSDDWDDSDDWDDDDSAASDDS
AAAAWAASSDDSAASSDDWDDSDDWWAAWDDDDDDSAASSDDWDDSDDWWAAWDDWWAASAAAAWDDWA
AWDDDDSDDWWAAWDDWWAASAAWAASSDDSAAAAWAASAAAAWDDWAAWDDDDSDDWWWAASAAAAWD
DWAAWDDDDSDDWDDDDSAASSDDWDDSDDWWAAWDD

此代码可在 https://nostarch.com/big-book-small-python-programming 获得
标签：大，艺术"""

import shutil, sys

# 为行字符设置常量：
UP_DOWN_CHAR         = chr(9474)  # 字符 9474 是“│”
LEFT_RIGHT_CHAR      = chr(9472)  # 字符 9472 是 '─'
DOWN_RIGHT_CHAR      = chr(9484)  # 字符 9484 是 '┌'
DOWN_LEFT_CHAR       = chr(9488)  # 字符 9488 是 '┐'
UP_RIGHT_CHAR        = chr(9492)  # 字符 9492 是 '└'
UP_LEFT_CHAR         = chr(9496)  # 字符 9496 是 '┘'
UP_DOWN_RIGHT_CHAR   = chr(9500)  # 字符 9500 是 '├'
UP_DOWN_LEFT_CHAR    = chr(9508)  # 字符 9508 是 '┤'
DOWN_LEFT_RIGHT_CHAR = chr(9516)  # 字符 9516 是 '┬'
UP_LEFT_RIGHT_CHAR   = chr(9524)  # 字符 9524 是 '┴'
CROSS_CHAR           = chr(9532)  # 字符 9532 是 '┼'
# chr() 代码列表位于 https://inventwithpython.com/chr

# 获取终端窗口的大小：
CANVAS_WIDTH, CANVAS_HEIGHT = shutil.get_terminal_size()
# 我们无法在 Windows 上打印到最后一列而不添加
# 自动换行，所以宽度减一：
CANVAS_WIDTH -= 1
# 在命令信息行的底部几行留出空间。
CANVAS_HEIGHT -= 5

"""The keys for canvas will be (x, y) integer tuples for the coordinate,
and the value is a set of letters W, A, S, D that tell what kind of line
should be drawn."""
canvas = {}
cursorX = 0
cursorY = 0


def getCanvasString(canvasData, cx, cy):
    """返回在 canvasData 中绘制的线的多行字符串。"""
    canvasStr = ''

    """canvasData is a dictionary with (x, y) tuple keys and values that
    are sets of 'W', 'A', 'S', and/or 'D' strings to show which
    directions the lines are drawn at each xy point."""
    for rowNum in range(CANVAS_HEIGHT):
        for columnNum in range(CANVAS_WIDTH):
            if columnNum == cx and rowNum == cy:
                canvasStr += '#'
                continue

            # 将此点的行字符添加到canvasStr。
            cell = canvasData.get((columnNum, rowNum))
            if cell in (set(['W', 'S']), set(['W']), set(['S'])):
                canvasStr += UP_DOWN_CHAR
            elif cell in (set(['A', 'D']), set(['A']), set(['D'])):
                canvasStr += LEFT_RIGHT_CHAR
            elif cell == set(['S', 'D']):
                canvasStr += DOWN_RIGHT_CHAR
            elif cell == set(['A', 'S']):
                canvasStr += DOWN_LEFT_CHAR
            elif cell == set(['W', 'D']):
                canvasStr += UP_RIGHT_CHAR
            elif cell == set(['W', 'A']):
                canvasStr += UP_LEFT_CHAR
            elif cell == set(['W', 'S', 'D']):
                canvasStr += UP_DOWN_RIGHT_CHAR
            elif cell == set(['W', 'S', 'A']):
                canvasStr += UP_DOWN_LEFT_CHAR
            elif cell == set(['A', 'S', 'D']):
                canvasStr += DOWN_LEFT_RIGHT_CHAR
            elif cell == set(['W', 'A', 'D']):
                canvasStr += UP_LEFT_RIGHT_CHAR
            elif cell == set(['W', 'A', 'S', 'D']):
                canvasStr += CROSS_CHAR
            elif cell == None:
                canvasStr += ' '
        canvasStr += '\n'  # 在每一行的末尾添加一个换行符。
    return canvasStr


moves = []
while True:  # 主程序循环。
    # 根据画布中的数据绘制线条:
    print(getCanvasString(canvas, cursorX, cursorY))

    print('WASD keys to move, H for help, C to clear, '
        + 'F to save, or QUIT.')
    response = input('> ').upper()

    if response == 'QUIT':
        print('Thanks for playing!')
        sys.exit()  # 退出程序。
    elif response == 'H':
        print('Enter W, A, S, and D characters to move the cursor and')
        print('draw a line behind it as it moves. For example, ddd')
        print('draws a line going right and sssdddwwwaaa draws a box.')
        print()
        print('You can save your drawing to a text file by entering F.')
        input('Press Enter to return to the program...')
        continue
    elif response == 'C':
        canvas = {}  # 擦除画布数据。
        moves.append('C')  # 记录这一举动。
    elif response == 'F':
        # 将画布字符串保存为一个文本文件:
        try:
            print('Enter filename to save to:')
            filename = input('> ')

            # 确保文件名以.txt结尾:
            if not filename.endswith('.txt'):
                filename += '.txt'
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(''.join(moves) + '\n')
                file.write(getCanvasString(canvas, None, None))
        except:
            print('ERROR: Could not save file.')

    for command in response:
        if command not in ('W', 'A', 'S', 'D'):
            continue  # 忽略这封信，继续下一封信。
        moves.append(command)  # 记录这一举动。

        # 我们添加的第一行需要形成一个完整的行:
        if canvas == {}:
            if command in ('W', 'S'):
                # 使第一行是水平的:
                canvas[(cursorX, cursorY)] = set(['W', 'S'])
            elif command in ('A', 'D'):
                # 让第一行是垂直的:
                canvas[(cursorX, cursorY)] = set(['A', 'D'])

        # 更新x和y:
        if command == 'W' and cursorY > 0:
            canvas[(cursorX, cursorY)].add(command)
            cursorY = cursorY - 1
        elif command == 'S' and cursorY < CANVAS_HEIGHT - 1:
            canvas[(cursorX, cursorY)].add(command)
            cursorY = cursorY + 1
        elif command == 'A' and cursorX > 0:
            canvas[(cursorX, cursorY)].add(command)
            cursorX = cursorX - 1
        elif command == 'D' and cursorX < CANVAS_WIDTH - 1:
            canvas[(cursorX, cursorY)].add(command)
            cursorX = cursorX + 1
        else:
            # 如果光标没有移动，因为它会移动到
            # 画布的边缘，然后不要更改
            # 画布的设置[(cursorX, cursorY)]。
            continue

        # 如果没有设置（cursorX，cursorY），请添加一个空集：
        if (cursorX, cursorY) not in canvas:
            canvas[(cursorX, cursorY)] = set()

        # 将方向弦添加到xy点的集合中:
        if command == 'W':
            canvas[(cursorX, cursorY)].add('S')
        elif command == 'S':
            canvas[(cursorX, cursorY)].add('W')
        elif command == 'A':
            canvas[(cursorX, cursorY)].add('D')
        elif command == 'D':
            canvas[(cursorX, cursorY)].add('A')
