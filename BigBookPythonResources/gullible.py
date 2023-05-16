"""容易上当，作者：Al Sweigart al@inventwithpython.com
如何让一个容易上当的人忙上几个小时。 （这是一个笑话节目。）
此代码可在 https://nostarch.com/big-book-small-python-programming 获得
标签：小，初学者，幽默"""

print('Gullible, by Al Sweigart al@inventwithpython.com')

while True:  # 主程序循环。
    print('Do you want to know how to keep a gullible person busy for hours? Y/N')
    response = input('> ')  # 获取用户的响应。
    if response.lower() == 'no' or response.lower() == 'n':
        break  # 如果“否”，则跳出此循环。
    if response.lower() == 'yes' or response.lower() == 'y':
        continue  # 如果“是”，继续到这个循环的开始。
    print('"{}" is not a valid yes/no response.'.format(response))

print('Thank you. Have a nice day!')
