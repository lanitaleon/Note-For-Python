"""黑客文, 作者：Al Sweigart al@inventwithpython.com
将英语信息翻译成 l33t5p34]<.
此代码可在https://nostarch.com/big-book-small-python-programming获得
标签:小，初学者，单词"""

import random

try:
    import pyperclip  # pyperclip 将文本复制到剪贴板。
except ImportError:
    pass  # 如果pyperclip没有安装，什么也不做。没什么大不了的。


def main():
    print('''L3375P34]< (leetspeek)
By Al Sweigart al@inventwithpython.com

Enter your leet message:''')
    english = input('> ')
    print()
    leetspeak = englishToLeetspeak(english)
    print(leetspeak)

    try:
        #如果没有导入pyperclip，尝试使用它将引发“名字错误”异常:
        pyperclip.copy(leetspeak)
        print('(Copied leetspeak to clipboard.)')
    except NameError:
        pass  # 如果pyperclip没有安装，什么也不做。


def englishToLeetspeak(message):
    """转换消息中的英文字符串并返回leetspeak。"""
    # 确保' charMapping '中的所有键都是小写的。
    charMapping = {
    'a': ['4', '@', '/-\\'], 'c': ['('], 'd': ['|)'], 'e': ['3'],
    'f': ['ph'], 'h': [']-[', '|-|'], 'i': ['1', '!', '|'], 'k': [']<'],
    'o': ['0'], 's': ['$', '5'], 't': ['7', '+'], 'u': ['|_|'],
    'v': ['\\/']}
    leetspeak = ''
    for char in message:  # 检查每个字符:
        # 我们有70%的机会把这个角色改成黑客文。
        if char.lower() in charMapping and random.random() <= 0.70:
            possibleLeetReplacements = charMapping[char.lower()]
            leetReplacement = random.choice(possibleLeetReplacements)
            leetspeak = leetspeak + leetReplacement
        else:
            # 不要翻译这个字符:
            leetspeak = leetspeak + char
    return leetspeak


# 如果程序运行(而不是导入)，运行游戏:
if __name__ == '__main__':
    main()
