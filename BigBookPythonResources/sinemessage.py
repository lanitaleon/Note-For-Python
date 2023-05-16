"""正弦消息, 作者：Al Sweigart al@inventwithpython.com
创建一个正弦波信息。
此代码可在https://nostarch.com/big-book-small-python-programming获得
标签:小，艺术"""

import math, shutil, sys, time

# 获取终端窗口的大小:
WIDTH, HEIGHT = shutil.get_terminal_size()
# 在Windows上，如果不自动添加换行符，我们就无法打印到最后一列，所以将宽度减少1:
WIDTH -= 1

print('Sine Message, by Al Sweigart al@inventwithpython.com')
print('(Press Ctrl-C to quit.)')
print()
print('What message do you want to display? (Max', WIDTH // 2, 'chars.)')
while True:
    message = input('> ')
    if 1 <= len(message) <= (WIDTH // 2):
        break
    print('Message must be 1 to', WIDTH // 2, 'characters long.')


step = 0.0  # 这个“步长”决定了我们进入正弦波的多远。
# sin从-1.0到1.0，所以我们需要用乘数来改变它:
multiplier = (WIDTH - len(message)) / 2
try:
    while True:  # 主程序循环
        sinOfStep = math.sin(step)
        padding = ' ' * int((sinOfStep + 1) * multiplier)
        print(padding + message)
        time.sleep(0.1)
        step += 0.25  # (!) 尝试将其更改为0.1或0.5。
except KeyboardInterrupt:
    sys.exit()  # 按下Ctrl-C后，结束程序。
