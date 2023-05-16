"""日历制作器，作者：Al Sweigart al@inventwithpython.com
创建月历，保存到文本文件并适合打印。
此代码可在 https://nostarch.com/big-book-small-python-programming 获得
标签： 短"""

import datetime

# 设置常量：
DAYS = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday')
MONTHS = ('January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December')

print('Calendar Maker, by Al Sweigart al@inventwithpython.com')

while True:  # 循环从用户那里得到一年。
    print('Enter the year for the calendar:')
    response = input('> ')

    if response.isdecimal() and int(response) > 0:
        year = int(response)
        break

    print('Please enter a numeric year, like 2023.')
    continue

while True:  # 循环从用户那里得到一个月。
    print('Enter the month for the calendar, 1-12:')
    response = input('> ')

    if not response.isdecimal():
        print('Please enter a numeric month, like 3 for March.')
        continue

    month = int(response)
    if 1 <= month <= 12:
        break

    print('Please enter a number from 1 to 12.')


def getCalendarFor(year, month):
    calText = ''  # calText 将包含我们日历的字符串。

    # 将月份和年份放在日历的顶部：
    calText += (' ' * 34) + MONTHS[month - 1] + ' ' + str(year) + '\n'

    # 将星期标签添加到日历：
    # (!) 尝试将其更改为缩写：SUN、MON、TUE 等。
    calText += '...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..\n'

    # 分隔周的水平线字符串：
    weekSeparator = ('+----------' * 7) + '+\n'

    # 空白行之间有十个空格 | 天分隔符：
    blankRow = ('|          ' * 7) + '|\n'

    # 获取当月的第一个日期。 （日期时间模块处理所有
    # 在这里为我们准备的复杂的日历内容。）
    currentDate = datetime.date(year, month, 1)

    # 回滚 currentDate 直到它是礼拜日。 (weekday() 返回 6
    # 表示星期日，而不是0。）
    while currentDate.weekday() != 6:
        currentDate -= datetime.timedelta(days=1)

    while True:  # 每月循环一周。
        calText += weekSeparator

        # dayNumberRow 是带有天数标签的行：
        dayNumberRow = ''
        for i in range(7):
            dayNumberLabel = str(currentDate.day).rjust(2)
            dayNumberRow += '|' + dayNumberLabel + (' ' * 8)
            currentDate += datetime.timedelta(days=1) # 循环至下一天
        dayNumberRow += '|\n'  # 在星期六之后添加垂直线。

        # 将天数行和 3 个空白行添加到日历文本中。
        calText += dayNumberRow
        for i in range(3):  # (!) 尝试将 4 更改为 5 或 10。
            calText += blankRow

        # 检查我们是否完成了月份：
        if currentDate.month != month:
            break

    # 在日历的最底部添加水平线。
    calText += weekSeparator
    return calText


calText = getCalendarFor(year, month)
print(calText)  # 显示日历。

# 将日历保存到文本文件：
calendarFilename = 'calendar_{}_{}.txt'.format(year, month)
with open(calendarFilename, 'w') as fileObj:
    fileObj.write(calText)

print('Saved to ' + calendarFilename)
