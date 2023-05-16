"""英语黑话, 作者：Al Sweigart al@inventwithpython.com
将英语信息翻译成英语黑话。
此代码可在https://nostarch.com/big-book-small-python-programming获得
标签:短,词语"""

try:
    import pyperclip  # Pyperclip将文本复制到剪贴板。
except ImportError:
    pass  # 如果pyperclip没有安装，什么也不做。没什么大不了的。

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')


def main():
    print('''Igpay Atinlay (Pig Latin)
By Al Sweigart al@inventwithpython.com

Enter your message:''')
    pigLatin = englishToPigLatin(input('> '))

    # 将所有单词重新连接到一个字符串中:
    print(pigLatin)

    try:
        pyperclip.copy(pigLatin)
        print('(Copied pig latin to clipboard.)')
    except NameError:
        pass  # 如果pyperclip没有安装，什么也不做。


def englishToPigLatin(message):
    pigLatin = ''  # 一串黑话的翻译。
    for word in message.split():
        # 将这个单词开头的非字母分开:
        prefixNonLetters = ''
        while len(word) > 0 and not word[0].isalpha():
            prefixNonLetters += word[0]
            word = word[1:]
        if len(word) == 0:
            pigLatin = pigLatin + prefixNonLetters + ' '
            continue

        # 将这个单词末尾的非字母分开:
        suffixNonLetters = ''
        while not word[-1].isalpha():
            suffixNonLetters = word[-1] + suffixNonLetters
            word = word[:-1]

        # 记住单词是全部大写还是首字母大写：
        wasUpper = word.isupper()
        wasTitle = word.istitle()

        word = word.lower()  # 把这个字写成小写以便翻译。

        # 把这个单词开头的辅音字母分开:
        prefixConsonants = ''
        while len(word) > 0 and not word[0] in VOWELS:
            prefixConsonants += word[0]
            word = word[1:]

        # 在单词后面加上黑话结尾:
        if prefixConsonants != '':
            word += prefixConsonants + 'ay'
        else:
            word += 'yay'

        # 将单词设置为全部大写或首字母大写:
        if wasUpper:
            word = word.upper()
        if wasTitle:
            word = word.title()

        # 将非字母添加回单词的开头或结尾
        pigLatin += prefixNonLetters + word + suffixNonLetters + ' '
    return pigLatin


if __name__ == '__main__':
    main()
