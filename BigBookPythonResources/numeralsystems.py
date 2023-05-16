"""数字系统计数器, 作者：Al Sweigart al@inventwithpython.com
用十进制、十六进制和二进制显示等价的数字。
此代码可在https://nostarch.com/big-book-small-python-programming获得
标签:小,数学"""


print('''Numeral System Counters, by Al Sweigart al@inventwithpython.com

This program shows you equivalent numbers in decimal (base 10),
hexadecimal (base 16), and binary (base 2) numeral systems.

(Ctrl-C to quit.)
''')

while True:
    response = input('Enter the starting number (e.g. 0) > ')
    if response == '':
        response = '0'  # 默认从0开始。
        break
    if response.isdecimal():
        break
    print('Please enter a number greater than or equal to 0.')
start = int(response)

while True:
    response = input('Enter how many numbers to display (e.g. 1000) > ')
    if response == '':
        response = '1000'  # 默认显示1000个号码。
        break
    if response.isdecimal():
        break
    print('Please enter a number.')
amount = int(response)

for number in range(start, start + amount):  # 主程序循环。
    # 转换为十六进制/二进制并删除前缀:
    hexNumber = hex(number)[2:].upper()
    binNumber = bin(number)[2:]

    print('DEC:', number, '   HEX:', hexNumber, '   BIN:', binNumber)
