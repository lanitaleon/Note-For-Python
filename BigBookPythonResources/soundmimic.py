"""声音模仿, 作者：Al Sweigart al@inventwithpython.com
一个带有声音模式的匹配游戏。试着记住越来越多的字母。
受到西蒙的电子游戏启发。
此代码可在https://nostarch.com/big-book-small-python-programming获得
标签:短，初学者，游戏"""

import random, sys, time

# 从这些URL下载声音文件(或使用你自己的):
# https://inventwithpython.com/soundA.wav
# https://inventwithpython.com/soundS.wav
# https://inventwithpython.com/soundD.wav
# https://inventwithpython.com/soundF.wav

try:
    import playsound
except ImportError:
    print('The playsound module needs to be installed to run this')
    print('program. On Windows, open a Command Prompt and run:')
    print('pip install playsound')
    print('On macOS and Linux, open a Terminal and run:')
    print('pip3 install playsound')
    sys.exit()


print('''Sound Mimic, by Al Sweigart al@inventwithpython.com
Try to memorize a pattern of A S D F letters (each with its own sound)
as it gets longer and longer.''')

input('Press Enter to begin...')

pattern = ''
while True:
    print('\n' * 60)  # 通过打印几个新行来清除屏幕。

    # 在模式中添加一个随机字母:
    pattern = pattern + random.choice('ASDF')

    # 显示模式(并播放它们的声音):
    print('Pattern: ', end='')
    for letter in pattern:
        print(letter, end=' ', flush=True)
        playsound.playsound('sound' + letter + '.wav')

    time.sleep(1)  # 在结尾添加一个轻微的停顿。
    print('\n' * 60)  #通过打印几个换行符来清除屏幕。

    # 让玩家进入模式:
    print('Enter the pattern:')
    response = input('> ').upper()

    if response != pattern:
        print('Incorrect!')
        print('The pattern was', pattern)
    else:
        print('Correct!')

    for letter in pattern:
        playsound.playsound('sound' + letter + '.wav')

    if response != pattern:
        print('You scored', len(pattern) - 1, 'points.')
        print('Thanks for playing!')
        break

    time.sleep(1)
