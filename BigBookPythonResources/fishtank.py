"""鱼缸，作者：Al Sweigart al@inventwithpython.com
一个鱼缸的和平动画。 按 Ctrl-C 停止。
类似于 ASCIIQuarium 或 @EmojiAquarium，但我的基于
用于 DOS 的旧 ASCII 鱼缸程序。
https://robobunny.com/projects/asciiquarium/html/
https://twitter.com/EmojiAquarium
此代码可在 https://nostarch.com/big-book-small-python-programming 获得
标签：特大号，艺术的，Bext"""

import random, sys, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# 设置常量：
WIDTH, HEIGHT = bext.size()
# 我们无法在 Windows 上打印到最后一列而不添加
# 自动换行，所以宽度减一：
WIDTH -= 1

NUM_KELP = 2  # (!) 尝试将其更改为 10。
NUM_FISH = 10  # (!) 尝试将其更改为 2 或 100。
NUM_BUBBLERS = 1  # (!) 尝试将其更改为 0 或 10。
FRAMES_PER_SECOND = 4  # (!) 尝试将此数字更改为 1 或 60。
# (!) 尝试更改常量以创建一个只有海带的鱼缸，
# 或仅起泡器。

# 注意：fish 字典中的每个字符串都应该具有相同的长度。
FISH_TYPES = [
  {'right': ['><>'],          'left': ['<><']},
  {'right': ['>||>'],         'left': ['<||<']},
  {'right': ['>))>'],         'left': ['<[[<']},
  {'right': ['>||o', '>||.'], 'left': ['o||<', '.||<']},
  {'right': ['>))o', '>)).'], 'left': ['o[[<', '.[[<']},
  {'right': ['>-==>'],        'left': ['<==-<']},
  {'right': [r'>\\>'],        'left': ['<//<']},
  {'right': ['><)))*>'],      'left': ['<*(((><']},
  {'right': ['}-[[[*>'],      'left': ['<*]]]-{']},
  {'right': [']-<)))b>'],     'left': ['<d(((>-[']},
  {'right': ['><XXX*>'],      'left': ['<*XXX><']},
  {'right': ['_.-._.-^=>', '.-._.-.^=>',
             '-._.-._^=>', '._.-._.^=>'],
   'left':  ['<=^-._.-._', '<=^.-._.-.',
             '<=^_.-._.-', '<=^._.-._.']},
  ]  # (!) 尝试将您自己的鱼添加到 FISH_TYPES。
LONGEST_FISH_LENGTH = 10  # FISH_TYPES 中最长的单个字符串。

# 鱼跑到屏幕边缘的 x 和 y 位置：
LEFT_EDGE = 0
RIGHT_EDGE = WIDTH - 1 - LONGEST_FISH_LENGTH
TOP_EDGE = 0
BOTTOM_EDGE = HEIGHT - 2


def main():
    global FISHES, BUBBLERS, BUBBLES, KELPS, STEP
    bext.bg('black')
    bext.clear()

    # 生成全局变量：
    FISHES = []
    for i in range(NUM_FISH):
        FISHES.append(generateFish())

    # 注意：气泡是绘制的，但不是气泡本身。
    BUBBLERS = []
    for i in range(NUM_BUBBLERS):
        # 每个起泡器从随机位置开始。
        BUBBLERS.append(random.randint(LEFT_EDGE, RIGHT_EDGE))
    BUBBLES = []

    KELPS = []
    for i in range(NUM_KELP):
        kelpx = random.randint(LEFT_EDGE, RIGHT_EDGE)
        kelp = {'x': kelpx, 'segments': []}
        # 生成海带的每一段：
        for i in range(random.randint(6, HEIGHT - 1)):
            kelp['segments'].append(random.choice(['(', ')']))
        KELPS.append(kelp)

    # 运行模拟：
    STEP = 1
    while True:
        simulateAquarium()
        drawAquarium()
        time.sleep(1 / FRAMES_PER_SECOND)
        clearAquarium()
        STEP += 1


def getRandomColor():
    """返回一个随机颜色的字符串。"""
    return random.choice(('black', 'red', 'green', 'yellow', 'blue',
                          'purple', 'cyan', 'white'))


def generateFish():
    """返回代表一条鱼的字典。"""
    fishType = random.choice(FISH_TYPES)

    # 为鱼文本中的每个字符设置颜色：
    colorPattern = random.choice(('random', 'head-tail', 'single'))
    fishLength = len(fishType['right'][0])
    if colorPattern == 'random':  # 所有零件都是随机着色的。
        colors = []
        for i in range(fishLength):
            colors.append(getRandomColor())
    if colorPattern == 'single' or colorPattern == 'head-tail':
        colors = [getRandomColor()] * fishLength  # 都是一样的颜色。
    if colorPattern == 'head-tail':  # 头部/尾部与身体不同。
        headTailColor = getRandomColor()
        colors[0] = headTailColor  # 设置头部颜色。
        colors[-1] = headTailColor  # 设置尾部颜色。

    # 设置其余的fish数据结构：
    fish = {'right':            fishType['right'],
            'left':             fishType['left'],
            'colors':           colors,
            'hSpeed':           random.randint(1, 6),
            'vSpeed':           random.randint(5, 15),
            'timeToHDirChange': random.randint(10, 60),
            'timeToVDirChange': random.randint(2, 20),
            'goingRight':       random.choice([True, False]),
            'goingDown':        random.choice([True, False])}

    # 'x' 总是鱼体的最左边：
    fish['x'] = random.randint(0, WIDTH - 1 - LONGEST_FISH_LENGTH)
    fish['y'] = random.randint(0, HEIGHT - 2)
    return fish


def simulateAquarium():
    """模拟水族箱中的一步运动。"""
    global FISHES, BUBBLERS, BUBBLES, KELP, STEP

    # 模拟鱼的一步：
    for fish in FISHES:
        # 水平移动鱼：
        if STEP % fish['hSpeed'] == 0:
            if fish['goingRight']:
                if fish['x'] != RIGHT_EDGE:
                    fish['x'] += 1  # 将鱼向右移动。
                else:
                    fish['goingRight'] = False  # 把鱼翻过来。
                    fish['colors'].reverse()  # 把颜色转过来。
            else:
                if fish['x'] != LEFT_EDGE:
                    fish['x'] -= 1  # 将鱼向左移动。
                else:
                    fish['goingRight'] = True  # 把鱼翻过来。
                    fish['colors'].reverse()  # 把颜色转过来。

        # 鱼可以随机改变它们的水平方向：
        fish['timeToHDirChange'] -= 1
        if fish['timeToHDirChange'] == 0:
            fish['timeToHDirChange'] = random.randint(10, 60)
            # 把鱼翻过来：
            fish['goingRight'] = not fish['goingRight']

        # 垂直移动鱼：
        if STEP % fish['vSpeed'] == 0:
            if fish['goingDown']:
                if fish['y'] != BOTTOM_EDGE:
                    fish['y'] += 1  # 把鱼往下移。
                else:
                    fish['goingDown'] = False  # 把鱼翻过来。
            else:
                if fish['y'] != TOP_EDGE:
                    fish['y'] -= 1  # 把鱼向上移动。
                else:
                    fish['goingDown'] = True  # 把鱼翻过来。

        # 鱼可以随机改变它们的垂直方向：
        fish['timeToVDirChange'] -= 1
        if fish['timeToVDirChange'] == 0:
            fish['timeToVDirChange'] = random.randint(2, 20)
            # 把鱼翻过来：
            fish['goingDown'] = not fish['goingDown']

    # 从起泡器中产生气泡：
    for bubbler in BUBBLERS:
        # 有五分之一的机会制造泡沫：
        if random.randint(1, 5) == 1:
            BUBBLES.append({'x': bubbler, 'y': HEIGHT - 2})

    # 移动气泡：
    for bubble in BUBBLES:
        diceRoll = random.randint(1, 6)
        if (diceRoll == 1) and (bubble['x'] != LEFT_EDGE):
            bubble['x'] -= 1  # 泡泡向左走。
        elif (diceRoll == 2) and (bubble['x'] != RIGHT_EDGE):
            bubble['x'] += 1  # 泡泡向右走。

        bubble['y'] -= 1  # 泡沫总是向上的。

    # 反向迭代 BUBBLES，因为我要在迭代它时，将它从 BUBBLES 中删除

    for i in range(len(BUBBLES) - 1, -1, -1):
        if BUBBLES[i]['y'] == TOP_EDGE:  # 删除到达顶部的气泡。
            del BUBBLES[i]

    # 模拟海带挥动的一步：
    for kelp in KELPS:
        for i, kelpSegment in enumerate(kelp['segments']):
            # 20 分之一的机会改变摆动：
            if random.randint(1, 20) == 1:
                if kelpSegment == '(':
                    kelp['segments'][i] = ')'
                elif kelpSegment == ')':
                    kelp['segments'][i] = '('


def drawAquarium():
    """在屏幕上画出水族馆。"""
    global FISHES, BUBBLERS, BUBBLES, KELP, STEP

    # 绘制退出消息。
    bext.fg('white')
    bext.goto(0, 0)
    print('Fish Tank, by Al Sweigart    Ctrl-C to quit.', end='')

    # 绘制气泡：
    bext.fg('white')
    for bubble in BUBBLES:
        bext.goto(bubble['x'], bubble['y'])
        print(random.choice(('o', 'O')), end='')

    # 画鱼：
    for fish in FISHES:
        bext.goto(fish['x'], fish['y'])

        # 获取正确的朝右或朝左的鱼文本。
        if fish['goingRight']:
            fishText = fish['right'][STEP % len(fish['right'])]
        else:
            fishText = fish['left'][STEP % len(fish['left'])]

        # 以正确的颜色绘制鱼文本的每个字符。
        for i, fishPart in enumerate(fishText):
            bext.fg(fish['colors'][i])
            print(fishPart, end='')

    # 画海带：
    bext.fg('green')
    for kelp in KELPS:
        for i, kelpSegment in enumerate(kelp['segments']):
            if kelpSegment == '(':
                bext.goto(kelp['x'], BOTTOM_EDGE - i)
            elif kelpSegment == ')':
                bext.goto(kelp['x'] + 1, BOTTOM_EDGE - i)
            print(kelpSegment, end='')

    # 在底部画沙子：
    bext.fg('yellow')
    bext.goto(0, HEIGHT - 1)
    print(chr(9617) * (WIDTH - 1), end='')  # 绘制“░”字符。

    sys.stdout.flush()  # (下次使用程序时需要。)


def clearAquarium():
    """在屏幕上的所有内容上绘制空白区域。"""
    global FISHES, BUBBLERS, BUBBLES, KELP

    # 绘制气泡：
    for bubble in BUBBLES:
        bext.goto(bubble['x'], bubble['y'])
        print(' ', end='')

    # 画鱼：
    for fish in FISHES:
        bext.goto(fish['x'], fish['y'])

        # 以正确的颜色绘制鱼文本的每个字符。
        print(' ' * len(fish['left'][0]), end='')

    # 画海带：
    for kelp in KELPS:
        for i, kelpSegment in enumerate(kelp['segments']):
            bext.goto(kelp['x'], HEIGHT - 2 - i)
            print('  ', end='')

    sys.stdout.flush()  # (下次使用程序时需要。)


# 如果此程序已运行（而不是导入），请运行游戏：
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # 当按下 Ctrl-C 时，结束程序。
