"""水桶拼图，作者：Al Sweigart al@inventwithpython.com
一个浇水拼图。
更多信息：https://en.wikipedia.org/wiki/Water_pouring_puzzle
此代码可在 https://nostarch.com/big-book-small-python-programming 获得
标签：大，游戏，数学，拼图"""

import sys


print('Water Bucket Puzzle, by Al Sweigart al@inventwithpython.com')

GOAL = 4  # 桶中的确切水量才能获胜。
steps = 0  # 记录玩家为解决这个问题所采取的步骤。

# 每桶水量：
waterInBucket = {'8': 0, '5': 0, '3': 0}

while True:  # 主游戏循环。
    # 显示桶的当前状态：
    print()
    print('Try to get ' + str(GOAL) + 'L of water into one of these')
    print('buckets:')

    waterDisplay = []  # 包含表示水或空白空间的字符串。

    # 获取 8L 桶的字符串：
    for i in range(1, 9):
        if waterInBucket['8'] < i:
            waterDisplay.append('      ')  # 添加空白空间。
        else:
            waterDisplay.append('WWWWWW')  # 加水。

    # 获取 5L 桶的字符串：
    for i in range(1, 6):
        if waterInBucket['5'] < i:
            waterDisplay.append('      ')  # 添加空白空间。
        else:
            waterDisplay.append('WWWWWW')  # 加水。

    # 获取 3L 桶的字符串：
    for i in range(1, 4):
        if waterInBucket['3'] < i:
            waterDisplay.append('      ')  # 添加空白空间。
        else:
            waterDisplay.append('WWWWWW')  # 加水。

    # 显示每个桶的水量：
    print('''
8|{7}|
7|{6}|
6|{5}|
5|{4}|  5|{12}|
4|{3}|  4|{11}|
3|{2}|  3|{10}|  3|{15}|
2|{1}|  2|{9}|  2|{14}|
1|{0}|  1|{8}|  1|{13}|
 +------+   +------+   +------+
    8L         5L         3L
'''.format(*waterDisplay))

    # 检查是否有任何桶具有目标水量：
    for waterAmount in waterInBucket.values():
        if waterAmount == GOAL:
            print('Good job! You solved it in', steps, 'steps!')
            sys.exit()

    # 让玩家选择一个动作来处理一个桶：
    print('You can:')
    print('  (F)ill the bucket')
    print('  (E)mpty the bucket')
    print('  (P)our one bucket into another')
    print('  (Q)uit')

    while True:  # 不断询问直到玩家输入有效动作。
        move = input('> ').upper()
        if move == 'QUIT' or move == 'Q':
            print('Thanks for playing!')
            sys.exit()

        if move in ('F', 'E', 'P'):
            break  # 玩家选择了一个有效的动作。
        print('Enter F, E, P, or Q')

    # 让玩家选择一个桶：
    while True:  # 继续询问，直到输入有效的存储桶。
        print('Select a bucket 8, 5, 3, or QUIT:')
        srcBucket = input('> ').upper()

        if srcBucket == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        if srcBucket in ('8', '5', '3'):
            break  # 玩家选择了一个有效的桶。

    # 执行选定的操作：
    if move == 'F':
        # 将水量设置为最大尺寸。
        srcBucketSize = int(srcBucket)
        waterInBucket[srcBucket] = srcBucketSize
        steps += 1

    elif move == 'E':
        waterInBucket[srcBucket] = 0  # 将水量设置为无。
        steps += 1

    elif move == 'P':
        # 让玩家选择一个桶来倒入：
        while True:  # 继续询问，直到输入有效的存储桶。
            print('Select a bucket to pour into: 8, 5, or 3')
            dstBucket = input('> ').upper()
            if dstBucket in ('8', '5', '3'):
                break  # 玩家选择了一个有效的桶。

        # 计算要倒的量：
        dstBucketSize = int(dstBucket)
        emptySpaceInDstBucket = dstBucketSize - waterInBucket[dstBucket]
        waterInSrcBucket = waterInBucket[srcBucket]
        amountToPour = min(emptySpaceInDstBucket, waterInSrcBucket)

        # 从这个桶里倒水：
        waterInBucket[srcBucket] -= amountToPour

        # 将倒出的水倒入另一个桶中：
        waterInBucket[dstBucket] += amountToPour
        steps += 1

    elif move == 'C':
        pass  # 如果玩家选择取消，则什么都不做。
