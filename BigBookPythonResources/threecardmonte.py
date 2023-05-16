"""三张牌蒙特，作者：Al Sweigart al@inventwithpython.com
交换卡片后找到红心皇后。
（在现实生活中，骗子会用手抚摸红心皇后，所以你
总是输。）
更多信息请访问 https://en.wikipedia.org/wiki/Three-card_Monte
此代码可在 https://nostarch.com/big-book-small-python-programming 获得
标签: 大型, 纸牌游戏, 游戏"""

import random, time

# 设置常量：
NUM_SWAPS = 16   # (!) 尝试将其更改为 30 或 100。
DELAY     = 0.8  # (!) 尝试更改此 2.0 或 0.0。

# 卡片套装字符：
HEARTS   = chr(9829)  # 字符 9829 是“♥”
DIAMONDS = chr(9830)  # 字符 9830 是“♦”
SPADES   = chr(9824)  # 字符 9824 是 '♠'
CLUBS    = chr(9827)  # 字符 9827 是 '♣'
# chr() 代码列表位于 https://inventwithpython.com/chr

# 三张牌表的索引：
LEFT   = 0
MIDDLE = 1
RIGHT  = 2


def displayCards(cards):
    """在“卡片”中显示卡片，这是（等级，花色）的列表
     元组。"""
    rows = ['', '', '', '', '']  # 存储要显示的文本。

    for i, card in enumerate(cards):
        rank, suit = card  # 卡片是元组数据结构。
        rows[0] += ' ___  '  # 打印卡片的顶行。
        rows[1] += '|{} | '.format(rank.ljust(2))
        rows[2] += '| {} | '.format(suit)
        rows[3] += '|_{}| '.format(rank.rjust(2, '_'))


    # 在屏幕上打印每一行：
    for i in range(5):
        print(rows[i])


def getRandomCard():
    """返回一张不是红心皇后的随机卡片。"""
    while True:  # 制作卡片，直到您获得非红心皇后。
        rank = random.choice(list('23456789JQKA') + ['10'])
        suit = random.choice([HEARTS, DIAMONDS, SPADES, CLUBS])

        # 只要它不是红心皇后，就返回这张牌：
        if rank != 'Q' and suit != HEARTS:
            return (rank, suit)


print('Three-Card Monte, by Al Sweigart al@inventwithpython.com')
print()
print('Find the red lady (the Queen of Hearts)! Keep an eye on how')
print('the cards move.')
print()

# 显示原始排列：
cards = [('Q', HEARTS), getRandomCard(), getRandomCard()]
random.shuffle(cards)  # 将红心皇后放在随机位置。
print('Here are the cards:')
displayCards(cards)
input('Press Enter when you are ready to begin...')

# 打印交换：
for i in range(NUM_SWAPS):
    swap = random.choice(['l-m', 'm-r', 'l-r', 'm-l', 'r-m', 'r-l'])

    if swap == 'l-m':
        print('swapping left and middle...')
        cards[LEFT], cards[MIDDLE] = cards[MIDDLE], cards[LEFT]
    elif swap == 'm-r':
        print('swapping middle and right...')
        cards[MIDDLE], cards[RIGHT] = cards[RIGHT], cards[MIDDLE]
    elif swap == 'l-r':
        print('swapping left and right...')
        cards[LEFT], cards[RIGHT] = cards[RIGHT], cards[LEFT]
    elif swap == 'm-l':
        print('swapping middle and left...')
        cards[MIDDLE], cards[LEFT] = cards[LEFT], cards[MIDDLE]
    elif swap == 'r-m':
        print('swapping right and middle...')
        cards[RIGHT], cards[MIDDLE] = cards[MIDDLE], cards[RIGHT]
    elif swap == 'r-l':
        print('swapping right and left...')
        cards[RIGHT], cards[LEFT] = cards[LEFT], cards[RIGHT]

    time.sleep(DELAY)

# 打印几行新行以隐藏交换。
print('\n' * 60)

# 要求用户找到红娘子：
while True:  # 继续询问直到输入 LEFT、MIDDLE 或 RIGHT。
    print('Which card has the Queen of Hearts? (LEFT MIDDLE RIGHT)')
    guess = input('> ').upper()

    # 获取玩家输入位置的卡片索引：
    if guess in ['LEFT', 'MIDDLE', 'RIGHT']:
        if guess == 'LEFT':
            guessIndex = 0
        elif guess == 'MIDDLE':
            guessIndex = 1
        elif guess == 'RIGHT':
            guessIndex = 2
        break

# (!) 取消注释这段代码，让玩家总是输：
#if cards[guessIndex] == ('Q', HEARTS):
#    # 玩家赢了，所以让我们移动皇后。
#    possibleNewIndexes = [0, 1, 2]
#    possibleNewIndexes.remove(guessIndex)  # 删除女王的索引。
#    newInd = random.choice(possibleNewIndexes)  # 选择一个新索引。
#    # 将皇后放在新索引处：
#    cards[guessIndex], cards[newInd] = cards[newInd], cards[guessIndex]

displayCards(cards)  # 显示所有卡片。

# 检查玩家是否赢了：
if cards[guessIndex] == ('Q', HEARTS):
    print('You won!')
    print('Thanks for playing!')
else:
    print('You lost!')
    print('Thanks for playing, sucker!')
