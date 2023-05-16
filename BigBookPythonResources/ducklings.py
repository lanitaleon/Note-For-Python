"""小鸭屏幕保护程序，由 Al Sweigart al@inventwithpython.com
许多小鸭的屏幕保护程序。

>" )   =^^)    (``=   ("=  >")    ("=
(  >)  (  ^)  (v  )  (^ )  ( >)  (v )
 ^ ^    ^ ^    ^ ^    ^^    ^^    ^^

此代码可在 https://nostarch.com/big-book-small-python-programming 获得
标签：大型、艺术、面向对象、滚动"""

import random, shutil, sys, time

# 设置常量：
PAUSE = 0.2  # (!) 尝试将其更改为 1.0 或 0.0。
DENSITY = 0.10  # (!) 尝试将其更改为从 0.0 到 1.0 的任何内容。

DUCKLING_WIDTH = 5
LEFT = 'left'
RIGHT = 'right'
BEADY = 'beady'
WIDE = 'wide'
HAPPY = 'happy'
ALOOF = 'aloof'
CHUBBY = 'chubby'
VERY_CHUBBY = 'very chubby'
OPEN = 'open'
CLOSED = 'closed'
OUT = 'out'
DOWN = 'down'
UP = 'up'
HEAD = 'head'
BODY = 'body'
FEET = 'feet'

# 获取终端窗口的大小：
WIDTH = shutil.get_terminal_size()[0]
# 我们无法在 Windows 上打印到最后一列而不添加
# 自动换行，所以宽度减一：
WIDTH -= 1


def main():
    print('Duckling Screensaver, by Al Sweigart')
    print('Press Ctrl-C to quit...')
    time.sleep(2)

    ducklingLanes = [None] * (WIDTH // DUCKLING_WIDTH)

    while True:  # 主程序循环。
        for laneNum, ducklingObj in enumerate(ducklingLanes):
            # 看看我们是否应该在这条车道上创建一只小鸭：
            if (ducklingObj == None and random.random() <= DENSITY):
                    # 在这条车道上放一只小鸭：
                    ducklingObj = Duckling()
                    ducklingLanes[laneNum] = ducklingObj

            if ducklingObj != None:
                # 如果这条车道上有一只小鸭，就画一只小鸭：
                print(ducklingObj.getNextBodyPart(), end='')
                # 如果我们画完了小鸭，就删除它：
                if ducklingObj.partToDisplayNext == None:
                    ducklingLanes[laneNum] = None
            else:
                # 画五个空格，因为这里没有小鸭。
                print(' ' * DUCKLING_WIDTH, end='')

        print()  # 打印换行符。
        sys.stdout.flush()  # 确保文本出现在屏幕上。
        time.sleep(PAUSE)


class Duckling:
    def __init__(self):
        """创建一个具有随机身体特征的新小鸭。"""
        self.direction = random.choice([LEFT, RIGHT])
        self.body = random.choice([CHUBBY, VERY_CHUBBY])
        self.mouth = random.choice([OPEN, CLOSED])
        self.wing = random.choice([OUT, UP, DOWN])

        if self.body == CHUBBY:
            # 胖嘟嘟的小鸭子只能长着珠子的眼睛。
            self.eyes = BEADY
        else:
            self.eyes = random.choice([BEADY, WIDE, HAPPY, ALOOF])

        self.partToDisplayNext = HEAD

    def getHeadStr(self):
        """返回小鸭头的字符串。"""
        headStr = ''
        if self.direction == LEFT:
            # 得到嘴：
            if self.mouth == OPEN:
                headStr += '>'
            elif self.mouth == CLOSED:
                headStr += '='

            # 获取眼睛：
            if self.eyes == BEADY and self.body == CHUBBY:
                headStr += '"'
            elif self.eyes == BEADY and self.body == VERY_CHUBBY:
                headStr += '" '
            elif self.eyes == WIDE:
                headStr += "''"
            elif self.eyes == HAPPY:
                headStr += '^^'
            elif self.eyes == ALOOF:
                headStr += '``'

            headStr += ') '  # 得到后脑勺。

        if self.direction == RIGHT:
            headStr += ' ('  # 得到后脑勺。

            # 获取眼睛：
            if self.eyes == BEADY and self.body == CHUBBY:
                headStr += '"'
            elif self.eyes == BEADY and self.body == VERY_CHUBBY:
                headStr += ' "'
            elif self.eyes == WIDE:
                headStr += "''"
            elif self.eyes == HAPPY:
                headStr += '^^'
            elif self.eyes == ALOOF:
                headStr += '``'

            # 得到嘴：
            if self.mouth == OPEN:
                headStr += '<'
            elif self.mouth == CLOSED:
                headStr += '='

        if self.body == CHUBBY:
            # 得到一个额外的空间，让胖小鸭
            # 宽度都和非常胖的小鸭子一样。
            headStr += ' '

        return headStr

    def getBodyStr(self):
        """返回小鸭身体的字符串。"""
        bodyStr = '('  # 得到身体的左侧。
        if self.direction == LEFT:
            # 获取车身内部空间：
            if self.body == CHUBBY:
                bodyStr += ' '
            elif self.body == VERY_CHUBBY:
                bodyStr += '  '

            # 获得翅膀：
            if self.wing == OUT:
                bodyStr += '>'
            elif self.wing == UP:
                bodyStr += '^'
            elif self.wing == DOWN:
                bodyStr += 'v'

        if self.direction == RIGHT:
            # 获得翅膀：
            if self.wing == OUT:
                bodyStr += '<'
            elif self.wing == UP:
                bodyStr += '^'
            elif self.wing == DOWN:
                bodyStr += 'v'

            # 获取车身内部空间：
            if self.body == CHUBBY:
                bodyStr += ' '
            elif self.body == VERY_CHUBBY:
                bodyStr += '  '

        bodyStr += ')'  # 得到身体的右侧。

        if self.body == CHUBBY:
            # 得到一个额外的空间，让胖小鸭
            # 宽度都和非常胖的小鸭子一样。
            bodyStr += ' '

        return bodyStr

    def getFeetStr(self):
        """返回小鸭脚的字符串。"""
        if self.body == CHUBBY:
            return ' ^^  '
        elif self.body == VERY_CHUBBY:
            return ' ^ ^ '

    def getNextBodyPart(self):
        """为下一个主体调用适当的显示方法
         显示需要的部分。 当完成后将 partToDisplayNext 设置为None。
         """
        if self.partToDisplayNext == HEAD:
            self.partToDisplayNext = BODY
            return self.getHeadStr()
        elif self.partToDisplayNext == BODY:
            self.partToDisplayNext = FEET
            return self.getBodyStr()
        elif self.partToDisplayNext == FEET:
            self.partToDisplayNext = None
            return self.getFeetStr()



# 如果此程序已运行（而不是导入），请运行游戏：
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # 当按下 Ctrl-C 时，结束程序。
