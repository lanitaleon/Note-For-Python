"""快速拔枪，作者：Al Sweigart al@inventwithpython.com
测试你的反应能力，看看你是否是西部最快的牛仔。
此代码可在 https://nostarch.com/big-book-small-python-programming 获得
标签：小，初学者，游戏"""

import random, sys, time

print('Fast Draw, by Al Sweigart al@inventwithpython.com')
print()
print('Time to test your reflexes and see if you are the fastest')
print('draw in the west!')
print('When you see "DRAW", you have 0.3 seconds to press Enter.')
print('But you lose if you press Enter before "DRAW" appears.')
print()
input('Press Enter to begin...')

while True:
    print()
    print('It is high noon...')
    time.sleep(random.randint(20, 50) / 10.0)
    print('DRAW!')
    drawTime = time.time()
    input()  # 在按下 Enter 之前，此函数调用不会返回。
    timeElapsed = time.time() - drawTime

    if timeElapsed < 0.01:
        # 如果玩家在 DRAW 前按下 Enter 键！ 出现，输入（）
        # call 几乎立即返回。
        print('You drew before "DRAW" appeared! You lose.')
    elif timeElapsed > 0.3:
        timeElapsed = round(timeElapsed, 4)
        print('You took', timeElapsed, 'seconds to draw. Too slow!')
    else:
        timeElapsed = round(timeElapsed, 4)
        print('You took', timeElapsed, 'seconds to draw.')
        print('You are the fastest draw in the west! You win!')

    print('Enter QUIT to stop, or press Enter to play again.')
    response = input('> ').upper()
    if response == 'QUIT':
        print('Thanks for playing!')
        sys.exit()
