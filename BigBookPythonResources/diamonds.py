"""钻石，作者：Al Sweigart al@inventwithpython.com
绘制各种尺寸的钻石。
在 https://nostarch.com/big-book-small-python-projects 查看此代码
                           /\       /\
                          /  \     //\\
            /\     /\    /    \   ///\\\
           /  \   //\\  /      \ ////\\\\
 /\   /\  /    \ ///\\\ \      / \\\\////
/  \ //\\ \    / \\\///  \    /   \\\///
\  / \\//  \  /   \\//    \  /     \\//
 \/   \/    \/     \/      \/       \/
标签：小，初学者，艺术"""

def main():
    print('Diamonds, by Al Sweigart al@inventwithpython.com')

    # 显示大小为 0 到 6 的钻石：
    for diamondSize in range(0, 6):
        displayOutlineDiamond(diamondSize)
        print()  # 打印换行符。
        displayFilledDiamond(diamondSize)
        print()  # 打印换行符。


def displayOutlineDiamond(size):
    # 显示菱形的上半部分：
    for i in range(size):
        print(' ' * (size - i - 1), end='')  # 左侧空间。
        print('/', end='')  # 钻石的左侧。
        print(' ' * (i * 2), end='')  # 钻石内部。
        print('\\')  # 钻石的右侧。

    # 显示菱形的下半部分：
    for i in range(size):
        print(' ' * i, end='')  # 左侧空间。
        print('\\', end='')  # 钻石的左侧。
        print(' ' * ((size - i - 1) * 2), end='')  # 钻石内部。
        print('/')  # 钻石的右侧。


def displayFilledDiamond(size):
    # 显示菱形的上半部分：
    for i in range(size):
        print(' ' * (size - i - 1), end='')  # 左侧空间。
        print('/' * (i + 1), end='')  # 钻石的左半部分。
        print('\\' * (i + 1))  # 钻石的右半部分。

    # 显示菱形的下半部分：
    for i in range(size):
        print(' ' * i, end='')  # 左侧空间。
        print('\\' * (size - i), end='')  # 钻石的左侧。
        print('/' * (size - i))  # 钻石的右侧。


# 如果此程序已运行（而不是导入），请运行游戏：
if __name__ == '__main__':
    main()
