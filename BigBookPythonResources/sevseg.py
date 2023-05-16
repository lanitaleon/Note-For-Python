"""数码管驱动, 作者：Al Sweigart al@inventwithpython.com
一个用于倒计时和数字时钟程序的七段数字显示模块。
更多信息可在https://en.wikipedia.org/wiki/Seven-segment_display获得
此代码可在https://nostarch.com/big-book-small-python-programming获得
标签:短,模块"""

"""A labeled seven-segment display, with each segment labeled A to G:
 __A__
|     |    Each digit in a seven-segment display:
F     B     __       __   __        __   __  __   __   __
|__G__|    |  |   |  __|  __| |__| |__  |__    | |__| |__|
|     |    |__|   | |__   __|    |  __| |__|   | |__|  __|
E     C
|__D__|"""


def getSevSegStr(number, minWidth=0):
    """返回一个由数字组成的七段显示为字符串。 如果返回的字符串小于最小宽度，则返回的字符串将被填充为0。"""

    # 转换数字为字符串，以防它是整数或浮点数:
    number = str(number).zfill(minWidth)

    rows = ['', '', '']
    for i, numeral in enumerate(number):
        if numeral == '.':  # 呈现为小数点。
            rows[0] += ' '
            rows[1] += ' '
            rows[2] += '.'
            continue  # 跳过数字之间的空格。
        elif numeral == '-':  # 呈现负号:
            rows[0] += '    '
            rows[1] += ' __ '
            rows[2] += '    '
        elif numeral == '0':  # 呈现0。
            rows[0] += ' __ '
            rows[1] += '|  |'
            rows[2] += '|__|'
        elif numeral == '1':  #呈现1。
            rows[0] += '    '
            rows[1] += '   |'
            rows[2] += '   |'
        elif numeral == '2':  #  呈现2。
            rows[0] += ' __ '
            rows[1] += ' __|'
            rows[2] += '|__ '
        elif numeral == '3':  # 呈现3.
            rows[0] += ' __ '
            rows[1] += ' __|'
            rows[2] += ' __|'
        elif numeral == '4':  # 呈现4.
            rows[0] += '    '
            rows[1] += '|__|'
            rows[2] += '   |'
        elif numeral == '5':  # 呈现5.
            rows[0] += ' __ '
            rows[1] += '|__ '
            rows[2] += ' __|'
        elif numeral == '6':  # 呈现6.
            rows[0] += ' __ '
            rows[1] += '|__ '
            rows[2] += '|__|'
        elif numeral == '7':  # 呈现7。
            rows[0] += ' __ '
            rows[1] += '   |'
            rows[2] += '   |'
        elif numeral == '8':  # 呈现8。
            rows[0] += ' __ '
            rows[1] += '|__|'
            rows[2] += '|__|'
        elif numeral == '9':  # 呈现9。
            rows[0] += ' __ '
            rows[1] += '|__|'
            rows[2] += ' __|'

        # 如果这不是最后一个数字，小数点也不是下一个，
        # 则添加一个空格(用于数字之间的空格):
        if i != len(number) - 1 and number[i + 1] != '.':
            rows[0] += ' '
            rows[1] += ' '
            rows[2] += ' '

    return '\n'.join(rows)


# 如果这个程序没有被导入，显示数字00到99。
if __name__ == '__main__':
    print('This module is meant to be imported rather than run.')
    print('For example, this code:')
    print('    import sevseg')
    print('    myNumber = sevseg.getSevSegStr(42, 3)')
    print('    print(myNumber)')
    print()
    print('...will print 42, zero-padded to three digits:')
    print(' __        __ ')
    print('|  | |__|  __|')
    print('|__|    | |__ ')
