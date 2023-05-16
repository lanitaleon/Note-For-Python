"""凯撒密码黑客，作者：Al Sweigart al@inventwithpython.com
该程序通过执行以下操作来破解使用凯撒密码加密的消息
对所有可能的密钥进行蛮力攻击。
更多信息请访问：
https://en.wikipedia.org/wiki/Caesar_cipher#Breaking_the_cipher
此代码可在 https://nostarch.com/big-book-small-python-programming 获得
标签：小，初学者，密码学，数学"""

print('Caesar Cipher Hacker, by Al Sweigart al@inventwithpython.com')

# 让用户指定要破解的消息：
print('Enter the encrypted Caesar cipher message to hack.')
message = input('> ')

# 可以加密/解密的每个可能的符号：
#（这必须与加密消息时使用的 SYMBOLS 匹配。）
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(SYMBOLS)):  # 循环遍历每个可能的键。
    translated = ''

    # 解密消息中的每个符号：
    for symbol in message:
        if symbol in SYMBOLS:
            num = SYMBOLS.find(symbol)  # 获取符号的编号。
            num = num - key  # 解密号码。

            # 如果 num 小于 0，则进行环绕处理：
            if num < 0:
                num = num + len(SYMBOLS)

            # 将解密数字的符号添加到翻译中：
            translated = translated + SYMBOLS[num]
        else:
            # 只需添加符号而不解密：
            translated = translated + symbol

    # 显示正在测试的密钥及其解密文本：
    print('Key #{}: {}'.format(key, translated))
