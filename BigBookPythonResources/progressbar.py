"""进度条模拟, 作者：Al Sweigart al@inventwithpython.com
一个示例进度条动画，可以在其他程序中使用。
此代码可在https://nostarch.com/big-book-small-python-programming获得
标签:小，模拟"""

import random, time

BAR = chr(9608) # 字符9608 是'█'

def main():
    # 模拟下载:
    print('Progress Bar Simulation, by Al Sweigart')
    bytesDownloaded = 0
    downloadSize = 4096
    while bytesDownloaded < downloadSize:
        # 下载”随机数量的“字节":
        bytesDownloaded += random.randint(0, 100)

        # 获取此进度数量的进度条字符串:
        barStr = getProgressBar(bytesDownloaded, downloadSize)

        # 不要在末尾打印换行符，
        # 立即将打印的字符串刷新到屏幕上  :
        print(barStr, end='', flush=True)

        time.sleep(0.2)  # 暂停一下:

        # 打印退格符，将文本光标移动到行首:
        print('\b' * len(barStr), end='', flush=True)


def getProgressBar(progress, total, barWidth=40):
    """返回一个字符串，该字符串表示一个进度条，
    该进度条具有barWidth条并已从总进度中取得进度。  """

    progressBar = ''  # 度条将是一个字符串值。
    progressBar += '['  # 创建进度条的左端。

    # 确保进度的数量在0和总量之间:
    if progress > total:
        progress = total
    if progress < 0:
        progress = 0

    # 计算要显示的“条”的数量:
    numberOfBars = int((progress / total) * barWidth)

    progressBar += BAR * numberOfBars  # 添加进度条。
    progressBar += ' ' * (barWidth - numberOfBars)  # 添加空白。
    progressBar += ']'  # 添加进度条的右端。

    # 计算完成百分比:
    percentComplete = round(progress / total * 100, 1)
    progressBar += ' ' + str(percentComplete) + '%'  # 增加百分比。

    # 把所有数字加起来
    progressBar += ' ' + str(progress) + '/' + str(total)

    return progressBar  # 返回进度条字符串。


# 如果程序运行(而不是导入)，运行游戏:
if __name__ == '__main__':
    main()
