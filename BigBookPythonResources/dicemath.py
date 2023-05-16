"""骰子数学，作者：Al Sweigart al@inventwithpython.com
一种闪卡加法游戏，您可以在其中对随机骰子的总数求和。
在 https://nostarch.com/big-book-small-python-projects 查看此代码
标签：大，艺术，游戏，数学"""

import random, time

# 设置常量：
DICE_WIDTH = 9
DICE_HEIGHT = 5
CANVAS_WIDTH = 79
CANVAS_HEIGHT = 24 - 3  # -3 用于在底部输入总和的空间。

# 持续时间以秒为单位：
QUIZ_DURATION = 30  # (!) 尝试将其更改为 10 或 60。
MIN_DICE = 2  # (!) 尝试将其更改为 1 或 5。
MAX_DICE = 6  # (!) 尝试将其更改为 14。

# (!) 尝试将这些更改为不同的数字：
REWARD = 4  # (!) 回答正确可得积分。
PENALTY = 1  # (!) 因答案错误而被删除的分数。
# (!) 尝试将 PENALTY 设置为负数以给出
# 错误答案的分数！

# 如果所有骰子都无法显示在屏幕上，程序就会挂起：
assert MAX_DICE <= 14

D1 = (['+-------+',
       '|       |',
       '|   O   |',
       '|       |',
       '+-------+'], 1)

D2a = (['+-------+',
        '| O     |',
        '|       |',
        '|     O |',
        '+-------+'], 2)

D2b = (['+-------+',
        '|     O |',
        '|       |',
        '| O     |',
        '+-------+'], 2)

D3a = (['+-------+',
        '| O     |',
        '|   O   |',
        '|     O |',
        '+-------+'], 3)

D3b = (['+-------+',
        '|     O |',
        '|   O   |',
        '| O     |',
        '+-------+'], 3)

D4 = (['+-------+',
       '| O   O |',
       '|       |',
       '| O   O |',
       '+-------+'], 4)

D5 = (['+-------+',
       '| O   O |',
       '|   O   |',
       '| O   O |',
       '+-------+'], 5)

D6a = (['+-------+',
        '| O   O |',
        '| O   O |',
        '| O   O |',
        '+-------+'], 6)

D6b = (['+-------+',
        '| O O O |',
        '|       |',
        '| O O O |',
        '+-------+'], 6)

ALL_DICE = [D1, D2a, D2b, D3a, D3b, D4, D5, D6a, D6b]

print('''Dice Math, by Al Sweigart al@inventwithpython.com

Add up the sides of all the dice displayed on the screen. You have
{} seconds to answer as many as possible. You get {} points for each
correct answer and lose {} point for each incorrect answer.
'''.format(QUIZ_DURATION, REWARD, PENALTY))
input('Press Enter to begin...')

# 跟踪有多少答案是正确的和不正确的：
correctAnswers = 0
incorrectAnswers = 0
startTime = time.time()
while time.time() < startTime + QUIZ_DURATION:  # 主游戏循环。
    # 拿出骰子来显示：
    sumAnswer = 0
    diceFaces = []
    for i in range(random.randint(MIN_DICE, MAX_DICE)):
        die = random.choice(ALL_DICE)
        # die[0] 包含模具面的字符串列表：
        diceFaces.append(die[0])
        # die[1] 包含脸上的整数点数：
        sumAnswer += die[1]

    # 包含每个骰子左上角的 (x, y) 元组。
    topLeftDiceCorners = []

    # 弄清楚骰子应该去哪里：
    for i in range(len(diceFaces)):
        while True:
            # 在画布上随机找一个地方放置骰子：
            left = random.randint(0, CANVAS_WIDTH  - 1 - DICE_WIDTH)
            top  = random.randint(0, CANVAS_HEIGHT - 1 - DICE_HEIGHT)

            # 获取所有四个角的 x, y 坐标：
            #      left
            #      v
            #top > +-------+ ^
            #      | O     | |
            #      |   O   | DICE_HEIGHT (5)
            #      |     O | |
            #      +-------+ v
            #      <------->
            #      DICE_WIDTH (9)
            topLeftX = left
            topLeftY = top
            topRightX = left + DICE_WIDTH
            topRightY = top
            bottomLeftX = left
            bottomLeftY = top + DICE_HEIGHT
            bottomRightX = left + DICE_WIDTH
            bottomRightY = top + DICE_HEIGHT

            # 检查此骰子是否与之前的骰子重叠。
            overlaps = False
            for prevDieLeft, prevDieTop in topLeftDiceCorners:
                prevDieRight = prevDieLeft + DICE_WIDTH
                prevDieBottom = prevDieTop + DICE_HEIGHT
                # 检查这个骰子的每个角落，看看它是否在
                # 前一个骰子的区域的里面：
                for cornerX, cornerY in ((topLeftX, topLeftY),
                                         (topRightX, topRightY),
                                         (bottomLeftX, bottomLeftY),
                                         (bottomRightX, bottomRightY)):
                    if (prevDieLeft <= cornerX < prevDieRight
                        and prevDieTop <= cornerY < prevDieBottom):
                            overlaps = True
            if not overlaps:
                # 它不重叠，所以我们可以把它放在这里：
                topLeftDiceCorners.append((left, top))
                break

    # 在画布上绘制骰子：

    # 键是整数的 (x, y) 元组，取值该处的字符
    # 在画布上的位置：
    canvas = {}
    # 循环每个骰子：
    for i, (dieLeft, dieTop) in enumerate(topLeftDiceCorners):
        # 循环遍历骰子面上的每个点数：
        dieFace = diceFaces[i]
        for dx in range(DICE_WIDTH):
            for dy in range(DICE_HEIGHT):
                # 将此字符复制到画布上的正确位置：
                canvasX = dieLeft + dx
                canvasY = dieTop + dy
                # 注意在 dieFace 中，一个字符串列表，x 和 y
                # 被交换：
                canvas[(canvasX, canvasY)] = dieFace[dy][dx]

    # 在屏幕上显示画布：
    for cy in range(CANVAS_HEIGHT):
        for cx in range(CANVAS_WIDTH):
            print(canvas.get((cx, cy), ' '), end='')
        print()  # 打印换行符。

    # 让玩家输入他们的答案：
    response = input('Enter the sum: ').strip()
    if response.isdecimal() and int(response) == sumAnswer:
        correctAnswers += 1
    else:
        print('Incorrect, the answer is', sumAnswer)
        time.sleep(2)
        incorrectAnswers += 1

# 显示最终得分：
score = (correctAnswers * REWARD) - (incorrectAnswers * PENALTY)
print('Correct:  ', correctAnswers)
print('Incorrect:', incorrectAnswers)
print('Score:    ', score)
