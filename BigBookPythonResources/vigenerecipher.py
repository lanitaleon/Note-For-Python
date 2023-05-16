"""维吉尼亚密码，作者：Al Sweigart al@inventwithpython.com
维吉尼亚密码是一种多字母替代密码
强大到足以保持数个世纪之久。
更多信息请访问：https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher
此代码可在 https://nostarch.com/big-book-small-python-programming 获得
标签：简短，密码学，数学"""

try:
    import pyperclip  # 将文本复制到剪贴板。
except ImportError:
    pass  # 如果未安装 pyperclip，则什么都不做。 这没什么大不了的。

# 可以加密/解密的每个可能的符号：
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    print('''Vigenère Cipher, by Al Sweigart al@inventwithpython.com
The Viegenère cipher is a polyalphabetic substitution cipher that was
powerful enough to remain unbroken for centuries.''')

    # 让用户指定他们是加密还是解密：
    while True:  # 一直询问直到用户输入 e 或 d。
        print('Do you want to (e)ncrypt or (d)ecrypt?')
        response = input('> ').lower()
        if response.startswith('e'):
            myMode = 'encrypt'
            break
        elif response.startswith('d'):
            myMode = 'decrypt'
            break
        print('Please enter the letter e or d.')

    # 让用户指定要使用的密钥：
    while True:  # 一直询问直到用户输入有效密钥。
        print('Please specify the key to use.')
        print('It can be a word or any combination of letters:')
        response = input('> ').upper()
        if response.isalpha():
            myKey = response
            break

    # 让用户指定要加密/解密的消息：
    print('Enter the message to {}.'.format(myMode))
    myMessage = input('> ')

    # 执行加密/解密：
    if myMode == 'encrypt':
        translated = encryptMessage(myMessage, myKey)
    elif myMode == 'decrypt':
        translated = decryptMessage(myMessage, myKey)

    print('%sed message:' % (myMode.title()))
    print(translated)

    try:
        pyperclip.copy(translated)
        print('Full %sed text copied to clipboard.' % (myMode))
    except:
        pass  # 如果未安装 pyperclip，则什么都不做。


def encryptMessage(message, key):
    """使用密钥加密消息。"""
    return translateMessage(message, key, 'encrypt')


def decryptMessage(message, key):
    """使用密钥解密消息。"""
    return translateMessage(message, key, 'decrypt')


def translateMessage(message, key, mode):
    """使用密钥加密或解密消息。"""
    translated = []  # 存储加密/解密的消息字符串。

    keyIndex = 0
    key = key.upper()

    for symbol in message:  # 循环遍历消息中的每个字符。
        num = LETTERS.find(symbol.upper())
        if num != -1:  # -1 表示 symbol.upper() 不在字母中。
            if mode == 'encrypt':
                # 添加如果加密：
                num += LETTERS.find(key[keyIndex])
            elif mode == 'decrypt':
                # 如果解密则减去：
                num -= LETTERS.find(key[keyIndex])

            num %= len(LETTERS)  # 处理潜在的环绕。

            # 将加密/解密符号添加到翻译中。
            if symbol.isupper():
                translated.append(LETTERS[num])
            elif symbol.islower():
                translated.append(LETTERS[num].lower())

            keyIndex += 1  # 移至键中的下一个字母。
            if keyIndex == len(key):
                keyIndex = 0
        else:
            # 只需添加符号而不加密/解密：
            translated.append(symbol)

    return ''.join(translated)


# 如果此程序已运行（而不是导入），请运行该程序：
if __name__ == '__main__':
    main()
