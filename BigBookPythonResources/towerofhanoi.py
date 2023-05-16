"""河内塔，作者：Al Sweigart al@inventwithpython.com
一个堆栈移动的益智游戏。
此代码可在 https://nostarch.com/big-book-small-python-programming 获得
标签：短，游戏，拼图"""

import copy
import sys

TOTAL_DISKS = 5  # 更多的磁盘意味着更难的谜题。

# 从 A 塔上的所有磁盘开始：
COMPLETE_TOWER = list(range(TOTAL_DISKS, 0, -1))


def main():
    print("""The Tower of Hanoi, by Al Sweigart al@inventwithpython.com

Move the tower of disks, one disk at a time, to another tower. Larger
disks cannot rest on top of a smaller disk.

More info at https://en.wikipedia.org/wiki/Tower_of_Hanoi
"""
    )

    # 设置塔。 列表的末尾是塔顶。
    towers = {'A': copy.copy(COMPLETE_TOWER), 'B': [], 'C': []}

    while True:  # 跑一圈。
        # 显示塔和磁盘：
        displayTowers(towers)

        # 要求用户移动：
        fromTower, toTower = askForPlayerMove(towers)

        # 将顶部磁盘从 fromTower 移动到 toTower：
        disk = towers[fromTower].pop()
        towers[toTower].append(disk)

        # 检查用户是否已经解决了这个难题：
        if COMPLETE_TOWER in (towers['B'], towers['C']):
            displayTowers(towers)  # 最后一次展示塔。
            print('You have solved the puzzle! Well done!')
            sys.exit()


def askForPlayerMove(towers):
    """要求玩家移动。 返回（从塔，到塔）。"""

    while True:  # 不断询问玩家，直到他们输入有效的移动。
        print('Enter the letters of "from" and "to" towers, or QUIT.')
        print('(e.g. AB to moves a disk from tower A to tower B.)')
        response = input('> ').upper().strip()

        if response == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        # 确保用户输入了有效的塔式字母：
        if response not in ('AB', 'AC', 'BA', 'BC', 'CA', 'CB'):
            print('Enter one of AB, AC, BA, BC, CA, or CB.')
            continue  # 再次询问玩家他们的举动。

        # 语法糖 - 使用更具描述性的变量名称：
        fromTower, toTower = response[0], response[1]

        if len(towers[fromTower]) == 0:
            # “from” 塔不能是空塔：
            print('You selected a tower with no disks.')
            continue  # 再次询问玩家他们的举动。
        elif len(towers[toTower]) == 0:
            # 任何磁盘都可以移动到空的“to”塔上：
            return fromTower, toTower
        elif towers[toTower][-1] < towers[fromTower][-1]:
            print('Can\'t put larger disks on top of smaller ones.')
            continue  # 再次询问玩家他们的举动。
        else:
            # 这是一个有效的移动，因此返回选定的塔：
            return fromTower, toTower


def displayTowers(towers):
    """显示当前状态。"""

    # 展示三座塔：
    for level in range(TOTAL_DISKS, -1, -1):
        for tower in (towers['A'], towers['B'], towers['C']):
            if level >= len(tower):
                displayDisk(0)  # 显示没有磁盘的裸极。
            else:
                displayDisk(tower[level])  # 显示磁盘。
        print()

    # 显示塔标签 A、B 和 C。
    emptySpace = ' ' * (TOTAL_DISKS)
    print('{0} A{0}{0} B{0}{0} C\n'.format(emptySpace))


def displayDisk(width):
    """显示给定宽度的圆盘。 宽度为 0 表示没有磁盘。"""
    emptySpace = ' ' * (TOTAL_DISKS - width)

    if width == 0:
        # 显示没有圆盘的极段：
        print(emptySpace + '||' + emptySpace, end='')
    else:
        # 显示磁盘：
        disk = '@' * width
        numLabel = str(width).rjust(2, '_')
        print(emptySpace + disk + numLabel + disk + emptySpace, end='')


# 如果程序运行（而不是导入），运行游戏：
if __name__ == '__main__':
    main()
