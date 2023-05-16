"""凯撒密码，作者：Al Sweigart al@inventwithpython.com
凯撒密码是一种使用加法和减法的移位密码
加密和解密信件。
更多信息请访问：https://en.wikipedia.org/wiki/Caesar_cipher
在 https://nostarch.com/big-book-small-python-projects 查看此代码
标签：简短，初学者，密码学，数学"""

try:
    import pyperclip  # 将文本复制到剪贴板。
except ImportError:
    pass  # 如果未安装 pyperclip，则什么都不做。 这没什么大不了的。

# 可以加密/解密的每个可能的符号：
# (!) 您可以添加数字和标点符号来加密它们
# 符号也是如此。
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print('Caesar Cipher, by Al Sweigart al@inventwithpython.com')
print('The Caesar cipher encrypts letters by shifting them over by a')
print('key number. For example, a key of 2 means the letter A is')
print('encrypted into C, the letter B encrypted into D, and so on.')
print()

# 让用户输入是加密还是解密：
while True:  # 一直询问直到用户输入 e 或 d。
    print('Do you want to (e)ncrypt or (d)ecrypt?')
    response = input('> ').lower()
    if response.startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break
    print('Please enter the letter e or d.')

# 让用户输入要使用的密钥：
while True:  # 一直询问直到用户输入有效密钥。
    maxKey = len(SYMBOLS) - 1
    print('Please enter the key (0 to {}) to use.'.format(maxKey))
    response = input('> ').upper()
    if not response.isdecimal():
        continue

    if 0 <= int(response) < len(SYMBOLS):
        key = int(response)
        break

# 让用户输入要加密/解密的消息：
print('Enter the message to {}.'.format(mode))
message = input('> ')

# 凯撒密码仅适用于大写字母：
message = message.upper()

# 存储消息的加密/解密形式：
translated = ''

# 加密/解密消息中的每个符号：
for symbol in message:
    if symbol in SYMBOLS:
        # 获取此符号的加密（或解密）编号。
        num = SYMBOLS.find(symbol)  # 获取符号的编号。
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key

        # 如果 num 大于符号的长度或小于0，则进行环绕处理：
        if num >= len(SYMBOLS):
            num = num - len(SYMBOLS)
        elif num < 0:
            num = num + len(SYMBOLS)

        # 将加密/解密数字的符号添加到翻译中：
        translated = translated + SYMBOLS[num]
    else:
        # 只需添加符号而不加密/解密：
        translated = translated + symbol

# 在屏幕上显示加密/解密的字符串：
print(translated)

try:
    pyperclip.copy(translated)
    print('Full {}ed text copied to clipboard.'.format(mode))
except:
    pass  # 如果未安装 pyperclip，则什么都不做。
