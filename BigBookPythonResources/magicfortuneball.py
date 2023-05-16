"""神奇的幸运球, 作者：Al Sweigart al@inventwithpython.com
关于你的未来，问一个是/不是的问题。灵感来自魔术8号球。
此代码可在https://nostarch.com/big-book-small-python-programming获得
标签:微小，初学者，幽默"""

import random, time


def slowSpacePrint(text, interval=0.1):
    """缓慢显示文本，在每个字母和小写字母i之间有空格。"""
    for character in text:
        if character == 'I':
            # I是以小写形式显示:
            print('i ', end='', flush=True)
        else:
            # 其他字符正常显示:
            print(character + ' ', end='', flush=True)
        time.sleep(interval)
    print()  # 在末尾打印两个换行符。
    print()


# 问题提示:
slowSpacePrint('MAGIC FORTUNE BALL, BY AL SWEiGART')
time.sleep(0.5)
slowSpacePrint('ASK ME YOUR YES/NO QUESTION.')
input('> ')

# 显示一个简短的回复:
replies = [
    'LET ME THINK ON THIS...',
    'AN INTERESTING QUESTION...',
    'HMMM... ARE YOU SURE YOU WANT TO KNOW..?',
    'DO YOU THINK SOME THINGS ARE BEST LEFT UNKNOWN..?',
    'I MIGHT TELL YOU, BUT YOU MIGHT NOT LIKE THE ANSWER...',
    'YES... NO... MAYBE... I WILL THINK ON IT...',
    'AND WHAT WILL YOU DO WHEN YOU KNOW THE ANSWER? WE SHALL SEE...',
    'I SHALL CONSULT MY VISIONS...',
    'YOU MAY WANT TO SIT DOWN FOR THIS...',
]
slowSpacePrint(random.choice(replies))

# 戏剧性的停顿:
slowSpacePrint('.' * random.randint(4, 12), 0.7)

# 给出答案
slowSpacePrint('I HAVE AN ANSWER...', 0.2)
time.sleep(1)
answers = [
    'YES, FOR SURE',
    'MY ANSWER IS NO',
    'ASK ME LATER',
    'I AM PROGRAMMED TO SAY YES',
    'THE STARS SAY YES, BUT I SAY NO',
    'I DUNNO MAYBE',
    'FOCUS AND ASK ONCE MORE',
    'DOUBTFUL, VERY DOUBTFUL',
    'AFFIRMATIVE',
    'YES, THOUGH YOU MAY NOT LIKE IT',
    'NO, BUT YOU MAY WISH IT WAS SO',
]
slowSpacePrint(random.choice(answers), 0.05)
