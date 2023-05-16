"""数独谜题，作者：Al Sweigart al@inventwithpython.com
经典的 9x9 数字放置拼图。
更多信息请访问 https://en.wikipedia.org/wiki/Sudoku
此代码可在 https://nostarch.com/big-book-small-python-programming 获得
标签：大型、游戏、面向对象、益智"""

import copy, random, sys

# 这个游戏需要一个包含谜题的 sudokupuzzle.txt 文件。
# 从 https://inventwithpython.com/sudokupuzzles.txt 下载
# 以下是此文件中的内容示例：
# ..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..
# 2...8.3...6..7..84.3.5..2.9...1.54.8.........4.27.6...3.1..7.4.72..4..6...4.1...3
# ......9.7...42.18....7.5.261..9.4....5.....4....5.7..992.1.8....34.59...5.7......
# .3..5..4...8.1.5..46.....12.7.5.2.8....6.3....4.1.9.3.25.....98..1.2.6...8..6..2.

# 设置常量：
EMPTY_SPACE = '.'
GRID_LENGTH = 9
BOX_LENGTH = 3
FULL_GRID_SIZE = GRID_LENGTH * GRID_LENGTH


class SudokuGrid:
    def __init__(self, originalSetup):
        # originalSetup 是用于拼图设置的 81 个字符的字符串，
        # 带有数字和句点（用于空格）。
        # 见 https://inventwithpython.com/sudokupuzzles.txt
        self.originalSetup = originalSetup

        # 数独网格的状态由字典表示，该字典具有 (x, y) 键和该空间处的数字值（作为字符串）。
        self.grid = {}
        self.resetGrid()  # 将网格状态设置为其原始设置。
        self.moves = []  # 跟踪撤消功能的每个移动。

    def resetGrid(self):
        """将 self.grid 跟踪的网格状态重置为
         self.originalSetup 中的状态。"""
        for x in range(1, GRID_LENGTH + 1):
            for y in range(1, GRID_LENGTH + 1):
                self.grid[(x, y)] = EMPTY_SPACE

        assert len(self.originalSetup) == FULL_GRID_SIZE
        i = 0  # i 从 0 到 80
        y = 0  # y 从 0 到 8
        while i < FULL_GRID_SIZE:
            for x in range(GRID_LENGTH):
                self.grid[(x, y)] = self.originalSetup[i]
                i += 1
            y += 1

    def makeMove(self, column, row, number):
        """将数字放在列（从 A 到 I 的字母）和行
         （从 1 到 9 的整数）在网格上。"""
        x = 'ABCDEFGHI'.find(column)  # 将其转换为整数。
        y = int(row) - 1

        # 检查移动是否在“给定”号码上进行：
        if self.originalSetup[y * GRID_LENGTH + x] != EMPTY_SPACE:
            return False

        self.grid[(x, y)] = number  # 将此数字放在网格上。

        # 我们需要存储字典对象的单独副本：
        self.moves.append(copy.copy(self.grid))
        return True

    def undo(self):
        """将当前网格状态设置为 self.moves 列表中的前一个状态。"""
        if self.moves == []:
            return  # self.moves 中没有状态，所以什么都不做。

        self.moves.pop()  # 删除当前状态。

        if self.moves == []:
            self.resetGrid()
        else:
            # 将网格设置为最后一步。
            self.grid = copy.copy(self.moves[-1])

    def display(self):
        """在屏幕上显示网格的当前状态。"""
        print('   A B C   D E F   G H I')  # 显示列标签。
        for y in range(GRID_LENGTH):
            for x in range(GRID_LENGTH):
                if x == 0:
                    # 显示行标签：
                    print(str(y + 1) + '  ', end='')

                print(self.grid[(x, y)] + ' ', end='')
                if x == 2 or x == 5:
                    # 显示一条垂直线：
                    print('| ', end='')
            print()  # 打印换行符。

            if y == 2 or y == 5:
                # 显示一条水平线：
                print('   ------+-------+------')

    def _isCompleteSetOfNumbers(self, numbers):
        """如果数字包含数字 1 到 9，则返回 True。"""
        return sorted(numbers) == list('123456789')

    def isSolved(self):
        """如果当前网格处于求解状态，则返回 True。"""
        # 检查每一行：
        for row in range(GRID_LENGTH):
            rowNumbers = []
            for x in range(GRID_LENGTH):
                number = self.grid[(x, row)]
                rowNumbers.append(number)
            if not self._isCompleteSetOfNumbers(rowNumbers):
                return False

        # 检查每一列：
        for column in range(GRID_LENGTH):
            columnNumbers = []
            for y in range(GRID_LENGTH):
                number = self.grid[(column, y)]
                columnNumbers.append(number)
            if not self._isCompleteSetOfNumbers(columnNumbers):
                return False

        # 选中每个框：
        for boxx in (0, 3, 6):
            for boxy in (0, 3, 6):
                boxNumbers = []
                for x in range(BOX_LENGTH):
                    for y in range(BOX_LENGTH):
                        number = self.grid[(boxx + x, boxy + y)]
                        boxNumbers.append(number)
                if not self._isCompleteSetOfNumbers(boxNumbers):
                    return False

        return True


print('''Sudoku Puzzle, by Al Sweigart al@inventwithpython.com

Sudoku is a number placement logic puzzle game. A Sudoku grid is a 9x9
grid of numbers. Try to place numbers in the grid such that every row,
column, and 3x3 box has the numbers 1 through 9 once and only once.

For example, here is a starting Sudoku grid and its solved form:

    5 3 . | . 7 . | . . .     5 3 4 | 6 7 8 | 9 1 2
    6 . . | 1 9 5 | . . .     6 7 2 | 1 9 5 | 3 4 8
    . 9 8 | . . . | . 6 .     1 9 8 | 3 4 2 | 5 6 7
    ------+-------+------     ------+-------+------
    8 . . | . 6 . | . . 3     8 5 9 | 7 6 1 | 4 2 3
    4 . . | 8 . 3 | . . 1 --> 4 2 6 | 8 5 3 | 7 9 1
    7 . . | . 2 . | . . 6     7 1 3 | 9 2 4 | 8 5 6
    ------+-------+------     ------+-------+------
    . 6 . | . . . | 2 8 .     9 6 1 | 5 3 7 | 2 8 4
    . . . | 4 1 9 | . . 5     2 8 7 | 4 1 9 | 6 3 5
    . . . | . 8 . | . 7 9     3 4 5 | 2 8 6 | 1 7 9
''')
input('Press Enter to begin...')


# 加载 sudokupuzzles.txt 文件：
with open('sudokupuzzles.txt') as puzzleFile:
    puzzles = puzzleFile.readlines()

# 删除每个拼图末尾的换行符：
for i, puzzle in enumerate(puzzles):
    puzzles[i] = puzzle.strip()

grid = SudokuGrid(random.choice(puzzles))

while True:  # 主游戏循环。
    grid.display()

    # 检查拼图是否已解决。
    if grid.isSolved():
        print('Congratulations! You solved the puzzle!')
        print('Thanks for playing!')
        sys.exit()

    # 获取玩家的动作：
    while True:  # 不断询问直到玩家输入有效动作。
        print()  # 打印换行符。
        print('Enter a move, or RESET, NEW, UNDO, ORIGINAL, or QUIT:')
        print('(For example, a move looks like "B4 9".)')

        action = input('> ').upper().strip()

        if len(action) > 0 and action[0] in ('R', 'N', 'U', 'O', 'Q'):
            # 玩家输入了一个有效的动作。
            break

        if len(action.split()) == 2:
            space, number = action.split()
            if len(space) != 2:
                continue

            column, row = space
            if column not in list('ABCDEFGHI'):
                print('There is no column', column)
                continue
            if not row.isdecimal() or not (1 <= int(row) <= 9):
                print('There is no row', row)
                continue
            if not (1 <= int(number) <= 9):
                print('Select a number from 1 to 9, not ', number)
                continue
            break  # 玩家输入了一个有效的移动。

    print()  # 打印换行符。

    if action.startswith('R'):
        # 重置网格：
        grid.resetGrid()
        continue

    if action.startswith('N'):
        # 得到一个新的谜题：
        grid = SudokuGrid(random.choice(puzzles))
        continue

    if action.startswith('U'):
        # 撤消最后一步：
        grid.undo()
        continue

    if action.startswith('O'):
        # 查看原始数字：
        originalGrid = SudokuGrid(grid.originalSetup)
        print('The original grid looked like this:')
        originalGrid.display()
        input('Press Enter to continue...')

    if action.startswith('Q'):
        # 退出游戏。
        print('Thanks for playing!')
        sys.exit()

    # 处理玩家选择的移动。
    if grid.makeMove(column, row, number) == False:
        print('You cannot overwrite the original grid\'s numbers.')
        print('Enter ORIGINAL to view the original grid.')
        input('Press Enter to continue...')
