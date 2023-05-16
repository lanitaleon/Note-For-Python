"""刽子手，作者：Al Sweigart al@inventwithpython.com
在刽子手被画出来之前猜出了一个秘密的字
此代码可在https://nostarch.com/big-book-small-python-programming获得
标签:大，游戏，单词，谜题"""

# 这个游戏的一个版本在《发明你自己》一书中有介绍
# 使用Python的电脑游戏" https://nostarch.com/inventwithpython

import random, sys

# 建立常数:
# (!) 尝试在HANGMAN_PICS中添加或更改字符串以生成
# 用断头台代替绞刑架。
HANGMAN_PICS = [r"""
 +--+
 |  |
    |
    |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
    |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
 |  |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|  |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|\ |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|\ |
/   |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|\ |
/ \ |
    |
====="""]

# (!) 尝试用新的字符串替换CATEGORY和WORDS。
CATEGORY = 'Animals'
WORDS = 'ANT BABOON BADGER BAT BEAR BEAVER CAMEL CAT CLAM COBRA COUGAR COYOTE CROW DEER DOG DONKEY DUCK EAGLE FERRET FOX FROG GOAT GOOSE HAWK LION LIZARD LLAMA MOLE MONKEY MOOSE MOUSE MULE NEWT OTTER OWL PANDA PARROT PIGEON PYTHON RABBIT RAM RAT RAVEN RHINO SALMON SEAL SHARK SHEEP SKUNK SLOTH SNAKE SPIDER STORK SWAN TIGER TOAD TROUT TURKEY TURTLE WEASEL WHALE WOLF WOMBAT ZEBRA'.split()


def main():
    print('Hangman, by Al Sweigart al@inventwithpython.com')

    # 为新游戏设置变量:
    missedLetters = []  # 错误的字母猜测列表。
    correctLetters = []  # 猜对的字母列表。
    secretWord = random.choice(WORDS)  # 玩家必须猜出的单词。

    while True:  # 主要的游戏循环。
        drawHangman(missedLetters, correctLetters, secretWord)

        # 让玩家输入自己的字母猜:
        guess = getPlayerGuess(missedLetters + correctLetters)

        if guess in secretWord:
            # 将正确的猜测添加到correctLetters中:
            correctLetters.append(guess)

            # 检查玩家是否赢了:
            foundAllLetters = True  # 假设他们已经赢了。
            for secretWordLetter in secretWord:
                if secretWordLetter not in correctLetters:
                    # 秘密字里有一封信不是
                    # 所以玩家并没有获胜:
                    foundAllLetters = False
                    break
            if foundAllLetters:
                print('Yes! The secret word is:', secretWord)
                print('You have won!')
                break  # 跳出主游戏循环。
        else:
            # 玩家猜错了:
            missedLetters.append(guess)

            # 检查玩家是否猜得太多而失败。(
            # “- 1”是因为我们不把空绞刑架算进去
            # HANGMAN_PICS.)
            if len(missedLetters) == len(HANGMAN_PICS) - 1:
                drawHangman(missedLetters, correctLetters, secretWord)
                print('You have run out of guesses!')
                print('The word was "{}"'.format(secretWord))
                break


def drawHangman(missedLetters, correctLetters, secretWord):
    """画出刽子手的当前状态，以及失踪和猜对了秘密单词的字母。"""
    print(HANGMAN_PICS[len(missedLetters)])
    print('The category is:', CATEGORY)
    print()

    # 显示猜错的字母:
    print('Missed letters: ', end='')
    for letter in missedLetters:
        print(letter, end=' ')
    if len(missedLetters) == 0:
        print('No missed letters yet.')
    print()

    # 显示秘密单词的空格(每个字母一个空格):
    blanks = ['_'] * len(secretWord)

    # 用正确的字母替换空格:
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks[i] = secretWord[i]

    # 在每个字母之间用空格显示秘密单词:
    print(' '.join(blanks))


def getPlayerGuess(alreadyGuessed):
    """返回玩家输入的字母。这个函数确保玩家输入了一个他们之前没有猜到的字母。"""
    while True:  # 继续询问，直到玩家输入有效的信件。
        print('Guess a letter.')
        guess = input('> ').upper()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif not guess.isalpha():
            print('Please enter a LETTER.')
        else:
            return guess


# 如果这个程序运行(而不是导入)，运行游戏:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # 按下Ctrl-C后，结束程序。
