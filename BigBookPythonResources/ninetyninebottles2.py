"""在墙上的九十九瓶牛奶2 ，作者：Al Sweigart al@inventwithpython.com
打印最长的完整的歌词之一的歌曲! 这首歌随着每一段歌词变得越来越琐碎。 按Ctrl-C停止。
此代码可在https://nostarch.com/big-book-small-python-programming获得
标签:短，滚动，字"""

import random, sys, time

# 建立常数:
# (!) 试着改变这两个为0来立即打印所有的歌词。
SPEED = 0.01  # 印刷字母之间的停顿。
LINE_PAUSE = 1.5  # 每行末尾的停顿。


def slowPrint(text, pauseAmount=0.1):
    """慢慢地一次一个地打印出文本中的字符"""
    for character in text:
        # 在这里设置flush=True，以便立即打印文本:
        print(character, flush=True, end='')  # end=''意味着没有换行符。
        time.sleep(pauseAmount)  # 在每个字符之间停顿。
    print()  # 输出一个换行符。


print('niNety-nniinE BoOttels, by Al Sweigart al@inventwithpython.com')
print()
print('(Press Ctrl-C to quit.)')

time.sleep(2)

bottles = 99  #这是起始瓶数。

# ：这个列表保存了用于歌词的字符串:
lines = [' bottles of milk on the wall,',
         ' bottles of milk,',
         'Take one down, pass it around,',
         ' bottles of milk on the wall!']

try:
    while bottles > 0:  # 继续循环并显示歌词。
        slowPrint(str(bottles) + lines[0], SPEED)
        time.sleep(LINE_PAUSE)
        slowPrint(str(bottles) + lines[1], SPEED)
        time.sleep(LINE_PAUSE)
        slowPrint(lines[2], SPEED)
        time.sleep(LINE_PAUSE)
        bottles = bottles - 1  # 减少一瓶的数量。

        if bottles > 0:  # 打印当前节的最后一行。
            slowPrint(str(bottles) + lines[3], SPEED)
        else:  #打印整首歌的最后一行。
            slowPrint('No more bottles of milk on the wall!', SPEED)

        time.sleep(LINE_PAUSE)
        print()  # 输出一个换行符。

        # 选择一条随机的线使“愚蠢”:
        lineNum = random.randint(0, 3)

        # 从行字符串中创建一个列表，以便我们可以编辑它。 (Python中的字符串是不可变的。)
        line = list(lines[lineNum])

        effect = random.randint(0, 3)
        if effect == 0:  #用空格替换字符。
            charIndex = random.randint(0, len(line) - 1)
            line[charIndex] = ' '
        elif effect == 1:  # 更改字符的大小写。
            charIndex = random.randint(0, len(line) - 1)
            if line[charIndex].isupper():
                line[charIndex] = line[charIndex].lower()
            elif line[charIndex].islower():
                line[charIndex] = line[charIndex].upper()
        elif effect == 2:  # 转置两个字符。
            charIndex = random.randint(0, len(line) - 2)
            firstChar = line[charIndex]
            secondChar = line[charIndex + 1]
            line[charIndex] = secondChar
            line[charIndex + 1] = firstChar
        elif effect == 3:  # 重复一个字符
            charIndex = random.randint(0, len(line) - 2)
            line.insert(charIndex, line[charIndex])

        # 将行列表转换回字符串，并将其放在lines中:
        lines[lineNum] = ''.join(line)
except KeyboardInterrupt:
    sys.exit()  # 按下Ctrl-C后，结束程序。
