"""简单换位密码, 作者：Al Sweigart al@inventwithpython.com
简单替换密码对明文中的每个符号和密文中的每个符号进行一对一的转换。
更多信息在https://en.wikipedia.org/wiki/Substitution_cipher获得
此代码可在https://nostarch.com/big-book-small-python-programming获得
标签:短，密码，数学"""

import random

try:
    import pyperclip  # Pyperclip将文本复制到剪贴板。
except ImportError:
    pass  # 如果pyperclip没有安装，什么也不做。没什么大不了的。

# 每一个可能被加密/解密的符号:
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    print('''Simple Substitution Cipher, by Al Sweigart
A simple substitution cipher has a one-to-one translation for each
symbol in the plaintext and each symbol in the ciphertext.''')

    #让用户指定他们是加密还是解密:
    while True:  # 一直问，直到用户输入e或d。
        print('Do you want to (e)ncrypt or (d)ecrypt?')
        response = input('> ').lower()
        if response.startswith('e'):
            myMode = 'encrypt'
            break
        elif response.startswith('d'):
            myMode = 'decrypt'
            break
        print('Please enter the letter e or d.')

    # 让用户指定要使用的键:
    while True:  # 一直询问，直到用户输入有效的密钥。
        print('Please specify the key to use.')
        if myMode == 'encrypt':
            print('Or enter RANDOM to have one generated for you.')
        response = input('> ').upper()
        if response == 'RANDOM':
            myKey = generateRandomKey()
            print('The key is {}. KEEP THIS SECRET!'.format(myKey))
            break
        else:
            if checkKey(response):
                myKey = response
                break

    # 让用户指定要加密/解密的消息:
    print('Enter the message to {}.'.format(myMode))
    myMessage = input('> ')

    # 执行加密/解密:
    if myMode == 'encrypt':
        translated = encryptMessage(myMessage, myKey)
    elif myMode == 'decrypt':
        translated = decryptMessage(myMessage, myKey)

    #展示结果:
    print('The %sed message is:' % (myMode))
    print(translated)

    try:
        pyperclip.copy(translated)
        print('Full %sed text copied to clipboard.' % (myMode))
    except:
        pass  # 如果pyperclip没有安装，什么也不做。


def checkKey(key):
    """如果key有效则返回True。否则返回False。"""
    keyList = list(key)
    lettersList = list(LETTERS)
    keyList.sort()
    lettersList.sort()
    if keyList != lettersList:
        print('There is an error in the key or symbol set.')
        return False
    return True


def encryptMessage(message, key):
    """使用密钥加密消息。"""
    return translateMessage(message, key, 'encrypt')


def decryptMessage(message, key):
    """使用密钥解密消息。"""
    return translateMessage(message, key, 'decrypt')


def translateMessage(message, key, mode):
    """使用密钥加密或解密消息"""
    translated = ''
    charsA = LETTERS
    charsB = key
    if mode == 'decrypt':
        # 对于解密，我们可以使用与加密相同的代码。
        # 我们只需要交换key和LETTERS字符串的使用位置。
        charsA, charsB = charsB, charsA

    # 循环遍历消息中的每个符号:
    for symbol in message:
        if symbol.upper() in charsA:
            # 加密/解密的符号:
            symIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[symIndex].upper()
            else:
                translated += charsB[symIndex].lower()
        else:
            # 该符号不在字母中，只需添加它不变。
            translated += symbol

    return translated


def generateRandomKey():
    """生成并随机返回一个加密密钥。"""
    key = list(LETTERS)  # 从LETTERS字符串中获取一个列表。
    random.shuffle(key)  # 随机打乱列表。
    return ''.join(key)  # 从列表中获取一个字符串。


# 如果程序运行(而不是导入)，则运行该程序:
if __name__ == '__main__':
    main()
