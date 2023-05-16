"""海绵盒形式, 作者:Al Sweigart al@inventwithpython.com
将英文信息翻译为海绵盒形式。
此代码可在https://nostarch.com/big-book-small-python-programming获得
标签:小，初学者，单词"""

import random

try:
    import pyperclip  # Pyperclip将文本复制到剪贴板。
except ImportError:
    pass  # 如果pyperclip没有安装，什么也不做。没什么大不了的。


def main():
    """以海绵盒形式运行程序。"""
    print('''sPoNgEtExT, bY aL sWeIGaRt Al@iNvEnTwItHpYtHoN.cOm

eNtEr YoUr MeSsAgE:''')
    spongecase = englishToSpongecase(input('> '))
    print()
    print(spongecase)

    try:
        pyperclip.copy(spongecase)
        print('(cOpIed SpOnGeCasE to ClIpbOaRd.)')
    except:
        pass  # 如果pyperclip没有安装，什么也不做。


def englishToSpongecase(message):
    """返回给定字符串的海绵盒形式"""
    spongecase = ''
    useUpper = False

    for character in message:
        if not character.isalpha():
            spongecase += character
            continue

        if useUpper:
            spongecase += character.upper()
        else:
            spongecase += character.lower()

        # 90%的情况下，转换这种形式。
        if random.randint(1, 100) <= 90:
            useUpper = not useUpper  # Flip the case.
    return spongecase


# 如果程序运行(而不是导入)，运行游戏:
if __name__ == '__main__':
    main()
