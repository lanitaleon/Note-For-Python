"""黑客小游戏，作者：Al Sweigart al@inventwithpython.com
《辐射3》中的黑客小游戏。 找出哪个七个字母
word 是使用每个猜测给你的线索的密码。
此代码可在 https://nostarch.com/big-book-small-python-programming 获得
标签：大，艺术，游戏，拼图"""

# 注意：这个程序需要sevenletterwords.txt 文件。 你可以
# 从 https://inventwithpython.com/sevenletterwords.txt 下载

import random, sys

# 设置常量：
# 用于“计算机内存”显示的垃圾填充字符。
GARBAGE_CHARS = '~!@#$%^&*()_+-={}[]|;:,.<>?/'

# 从包含 7 个字母的单词的文本文件加载 WORDS 列表。
with open('sevenletterwords.txt') as wordListFile:
    WORDS = wordListFile.readlines()
for i in range(len(WORDS)):
    # 将每个单词转换为大写并删除尾随的换行符：
    WORDS[i] = WORDS[i].strip().upper()


def main():
    """运行一个黑客游戏。"""
    print('''Hacking Minigame, by Al Sweigart al@inventwithpython.com
Find the password in the computer's memory. You are given clues after
each guess. For example, if the secret password is MONITOR but the
player guessed CONTAIN, they are given the hint that 2 out of 7 letters
were correct, because both MONITOR and CONTAIN have the letter O and N
as their 2nd and 3rd letter. You get four guesses.\n''')
    input('Press Enter to begin...')

    gameWords = getWords()
    # “计算机内存”只是装饰品，但看起来很酷：
    computerMemory = getComputerMemoryString(gameWords)
    secretPassword = random.choice(gameWords)

    print(computerMemory)
    # 从剩余的 4 次尝试开始，下降：
    for triesRemaining in range(4, 0, -1):
        playerMove = askForPlayerGuess(gameWords, triesRemaining)
        if playerMove == secretPassword:
            print('A C C E S S   G R A N T E D')
            return
        else:
            numMatches = numMatchingLetters(secretPassword, playerMove)
            print('Access Denied ({}/7 correct)'.format(numMatches))
    print('Out of tries. Secret password was {}.'.format(secretPassword))


def getWords():
    """返回可能是密码的 12 个单词的列表。

    秘密密码将是列表中的第一个单词。
     为了让游戏公平，我们尽量确保文字有
     一系列匹配的字母数字作为密语。"""
    secretPassword = random.choice(WORDS)
    words = [secretPassword]

    # 再找两个词； 这些有零个匹配字母。
    # 我们使用“< 3”是因为秘密密码已经在单词中。
    while len(words) < 3:
        randomWord = getOneWordExcept(words)
        if numMatchingLetters(secretPassword, randomWord) == 0:
            words.append(randomWord)

    # 找到两个有 3 个匹配字母的单词（但如果找不到足够的，
    # 则放弃 500 次尝试）。
    for i in range(500):
        if len(words) == 5:
            break  # 找到 5 个词，跳出循环。

        randomWord = getOneWordExcept(words)
        if numMatchingLetters(secretPassword, randomWord) == 3:
            words.append(randomWord)

    # 找到至少七个至少有一个匹配字母的单词
    # （但如果找不到足够的，则在 500 次尝试中放弃）。
    for i in range(500):
        if len(words) == 12:
            break  # 找到 7 个或更多单词，因此跳出循环。

        randomWord = getOneWordExcept(words)
        if numMatchingLetters(secretPassword, randomWord) != 0:
            words.append(randomWord)

    # 添加所需的任何随机单词以获得总共 12 个单词。
    while len(words) < 12:
        randomWord = getOneWordExcept(words)
        words.append(randomWord)

    assert len(words) == 12
    return words


def getOneWordExcept(blocklist=None):
    """从 WORDS 中返回一个不在阻止列表中的随机单词。"""
    if blocklist == None:
        blocklist = []

    while True:
        randomWord = random.choice(WORDS)
        if randomWord not in blocklist:
            return randomWord


def numMatchingLetters(word1, word2):
    """返回这两个单词中匹配字母的数量。"""
    matches = 0
    for i in range(len(word1)):
        if word1[i] == word2[i]:
            matches += 1
    return matches


def getComputerMemoryString(words):
    """返回一个表示“计算机内存”的字符串。"""

    # 每个单词选择一行来包含一个单词。 有 16 行，但是
    # 它们被分成两半。
    linesWithWords = random.sample(range(16 * 2), len(words))
    # 起始内存地址（这也是装饰性的）。
    memoryAddress = 16 * random.randint(0, 4000)

    # 创建“计算机内存”字符串。
    computerMemory = []  # 将包含 16 个字符串，每行一个。
    nextWord = 0  # 要放入一行的单词的单词索引。
    for lineNum in range(16):  # “计算机内存”有 16 行。
        # 创建半行垃圾字符：
        leftHalf = ''
        rightHalf = ''
        for j in range(16):  # 每半行有 16 个字符。
            leftHalf += random.choice(GARBAGE_CHARS)
            rightHalf += random.choice(GARBAGE_CHARS)

        # 从单词中填写密码：
        if lineNum in linesWithWords:
            # 在半行中找一个随机位置插入单词：
            insertionIndex = random.randint(0, 9)
            # 插入一句话：
            leftHalf = (leftHalf[:insertionIndex] + words[nextWord]
                + leftHalf[insertionIndex + 7:])
            nextWord += 1  # 更新单词以放入半行。
        if lineNum + 16 in linesWithWords:
            # 在半行中找一个随机位置插入单词：
            insertionIndex = random.randint(0, 9)
            # 插入一句话：
            rightHalf = (rightHalf[:insertionIndex] + words[nextWord]
                + rightHalf[insertionIndex + 7:])
            nextWord += 1  # 更新单词以放入半行。

        computerMemory.append('0x' + hex(memoryAddress)[2:].zfill(4)
                     + '  ' + leftHalf + '    '
                     + '0x' + hex(memoryAddress + (16*16))[2:].zfill(4)
                     + '  ' + rightHalf)

        memoryAddress += 16  # 例如，从 0xe680 跳转到 0xe690。

    # computerMemory 列表中的每个字符串都加入一个大的
    # 字符串并返回：
    return '\n'.join(computerMemory)


def askForPlayerGuess(words, tries):
    """让玩家输入密码猜测。"""
    while True:
        print('Enter password: ({} tries remaining)'.format(tries))
        guess = input('> ').upper()
        if guess in words:
            return guess
        print('That is not one of the possible passwords listed above.')
        print('Try entering "{}" or "{}".'.format(words[0], words[1]))


# 如果此程序已运行（而不是导入），请运行游戏：
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # 当按下 Ctrl-C 时，结束程序。
