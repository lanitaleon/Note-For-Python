"""ROT13密码, 作者：Al Sweigart al@inventwithpython.com
为加密和解密的文本添加最简单的移位密码。
更多信息可在https://en.wikipedia.org/wiki/ROT13获得
此代码可在https://nostarch.com/big-book-small-python-programming获得
标签：小，密码学"""

try:
    import pyperclip  # Pyperclip将文本复制到剪贴板。
except ImportError:
    pass  # 如果pyperclip没有安装，什么也不做。没什么大不了的。

# 建立常数:
UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWER_LETTERS = 'abcdefghijklmnopqrstuvwxyz'

print('ROT13 Cipher, by Al Sweigart al@inventwithpython.com')
print()

while True:  # 主程序循环。
    print('Enter a message to encrypt/decrypt (or QUIT):')
    message = input('> ')

    if message.upper() == 'QUIT':
        break  # 跳出主程序循环。

    # 将消息中的字母旋转13个字符。
    translated = ''
    for character in message:
        if character.isupper():
            # 连接大写翻译字符。
            transCharIndex = (UPPER_LETTERS.find(character) + 13) % 26
            translated += UPPER_LETTERS[transCharIndex]
        elif character.islower():
            # 连接小写翻译字符。
            transCharIndex = (LOWER_LETTERS.find(character) + 13) % 26
            translated += LOWER_LETTERS[transCharIndex]
        else:
            # 连接未翻译的字符。
            translated += character

    # 显示翻译:
    print('The translated message is:')
    print(translated)
    print()

    try:
        # 复制翻译到剪贴板:
        pyperclip.copy(translated)
        print('(Copied to clipboard.)')
    except:
        pass
