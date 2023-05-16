"""生日悖论模拟，作者：Al Sweigart al@inventwithpython.com
探索“生日悖论”的惊人概率。
更多信息请访问 https://en.wikipedia.org/wiki/Birthday_problem
此代码可在 https://nostarch.com/big-book-small-python-programming 获得
标签：简短，数学，模拟"""

import datetime, random


def getBirthdays(numberOfBirthdays):
    """返回生日的数字随机日期对象列表。"""
    birthdays = []
    for i in range(numberOfBirthdays):
        # 年份对于我们的模拟并不重要，只要所有生日都在同一年。
        startOfYear = datetime.date(2001, 1, 1)

        # 获取一年中的随机一天：
        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays


def getMatch(birthdays):
    """返回在生日列表中出现多次的生日的日期对象。"""
    if len(birthdays) == len(set(birthdays)):
        return None  # 所有生日都是唯一的，所以返回 None。

    # 将每个生日与其他每个生日进行比较：
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1 :]):
            if birthdayA == birthdayB:
                return birthdayA  # 返回匹配的生日。


# 显示介绍：
print('''Birthday Paradox, by Al Sweigart al@inventwithpython.com

The birthday paradox shows us that in a group of N people, the odds
that two of them have matching birthdays is surprisingly large.
This program does a Monte Carlo simulation (that is, repeated random
simulations) to explore this concept.

(It's not actually a paradox, it's just a surprising result.)
''')

# 按顺序设置月份名称元组：
MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True:  # 继续询问直到用户输入有效金额。
    print('How many birthdays shall I generate? (Max 100)')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        numBDays = int(response)
        break  # 用户输入了有效金额。
print()

# 生成并显示生日：
print('Here are', numBDays, 'birthdays:')
birthdays = getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        # 在第一个生日之后为每个生日显示一个逗号。
        print(', ', end='')
    monthName = MONTHS[birthday.month - 1]
    dateText = '{} {}'.format(monthName, birthday.day)
    print(dateText, end='')
print()
print()

# 确定是否有两个匹配的生日。
match = getMatch(birthdays)

# 显示结果：
print('In this simulation, ', end='')
if match != None:
    monthName = MONTHS[match.month - 1]
    dateText = '{} {}'.format(monthName, match.day)
    print('multiple people have a birthday on', dateText)
else:
    print('there are no matching birthdays.')
print()

# 运行 100,000 次模拟：
print('Generating', numBDays, 'random birthdays 100,000 times...')
input('Press Enter to begin...')

print('Let\'s run another 100,000 simulations.')
simMatch = 0  # 有多少模拟中有匹配的生日。
for i in range(100000):
    # 每 10,000 次模拟报告进度：
    if i % 10000 == 0:
        print(i, 'simulations run...')
    birthdays = getBirthdays(numBDays)
    if getMatch(birthdays) != None:
        simMatch = simMatch + 1
print('100,000 simulations run.')

# 显示模拟结果：
probability = round(simMatch / 100000 * 100, 2)
print('Out of 100,000 simulations of', numBDays, 'people, there was a')
print('matching birthday in that group', simMatch, 'times. This means')
print('that', numBDays, 'people have a', probability, '% chance of')
print('having a matching birthday in their group.')
print('That\'s probably more than you would think!')
