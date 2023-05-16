"""J的指控!, 作者：Al Sweigart al@inventwithpython.com
一个神秘的阴谋游戏和一只失踪的猫。
此代码可在https://nostarch.com/big-book-small-python-programming获得
标签: 超大，游戏，幽默，益智"""

# 玩原始的Flash 游戏，在：https://homestarrunner.com/videlectrix/wheresanegg.html
# 更多信息可在http://www.hrwiki.org/wiki/Where's_an_Egg%3F获得

import time, random, sys

# 建立常数:
SUSPECTS = ['DUKE HAUTDOG', 'MAXIMUM POWERS', 'BILL MONOPOLIS', 'SENATOR SCHMEAR', 'MRS. FEATHERTOSS', 'DR. JEAN SPLICER', 'RAFFLES THE CLOWN', 'ESPRESSA TOFFEEPOT', 'CECIL EDGAR VANDERTON']
ITEMS = ['FLASHLIGHT', 'CANDLESTICK', 'RAINBOW FLAG', 'HAMSTER WHEEL', 'ANIME VHS TAPE', 'JAR OF PICKLES', 'ONE COWBOY BOOT', 'CLEAN UNDERPANTS', '5 DOLLAR GIFT CARD']
PLACES = ['ZOO', 'OLD BARN', 'DUCK POND', 'CITY HALL', 'HIPSTER CAFE', 'BOWLING ALLEY', 'VIDEO GAME MUSEUM', 'UNIVERSITY LIBRARY', 'ALBINO ALLIGATOR PIT']
TIME_TO_SOLVE = 300  # 300秒(5分钟)解决游戏。

# 菜单显示需要第一个字母和位置的最长长度:
PLACE_FIRST_LETTERS = {}
LONGEST_PLACE_NAME_LENGTH = 0
for place in PLACES:
    PLACE_FIRST_LETTERS[place[0]] = place
    if len(place) > LONGEST_PLACE_NAME_LENGTH:
        LONGEST_PLACE_NAME_LENGTH = len(place)

# 常量基本的合理性键查：
assert len(SUSPECTS) == 9
assert len(ITEMS) == 9
assert len(PLACES) == 9
# 首字母必须唯一:
assert len(PLACE_FIRST_LETTERS.keys()) == len(PLACES)


knownSuspectsAndItems = []
# 需要注意的地方: 键=位置，值=嫌疑人和项目的字符串。
visitedPlaces = {}
currentLocation = 'TAXI'  # 在出租车上开始游戏
accusedSuspects = []  # 被指控的嫌疑人不会提供线索。
liars = random.sample(SUSPECTS, random.randint(3, 4))
accusationsLeft = 3  # 你最多可以指控3个人。
culprit = random.choice(SUSPECTS)

# 共同索引连接这些；例如嫌疑犯[0]和物品[0]都在地点[0].
random.shuffle(SUSPECTS)
random.shuffle(ITEMS)
random.shuffle(PLACES)

# 为讲真话的人提供的关于每个物品和嫌疑人的线索创建数据结构。
# 线索:键为被询问线索的嫌疑犯，值为“clue字典”。
clues = {}
for i, interviewee in enumerate(SUSPECTS):
    if interviewee in liars:
        continue  # 暂时跳过骗子。

    # 这个“clue字典”有键为物品和嫌疑人
    # 值为给定的线索。
    clues[interviewee] = {}
    clues[interviewee]['debug_liar'] = False  # 用于调试。
    for item in ITEMS:  # 选择每个项目的线索。
        if random.randint(0, 1) == 0:  # 告诉物品的位置:
            clues[interviewee][item] = PLACES[ITEMS.index(item)]
        else:  # 诉谁拥有该物品:
            clues[interviewee][item] = SUSPECTS[ITEMS.index(item)]
    for suspect in SUSPECTS:  # 选择有关每个嫌疑犯的线索。
        if random.randint(0, 1) == 0:  # 告诉嫌疑犯的位置:
            clues[interviewee][suspect] = PLACES[SUSPECTS.index(suspect)]
        else:  # 告诉嫌疑人拥有的物品：
            clues[interviewee][suspect] = ITEMS[SUSPECTS.index(suspect)]

#为了寻找撒谎者给出的关于每件物品和怀疑的线索创建数据结构:
for i, interviewee in enumerate(SUSPECTS):
    if interviewee not in liars:
        continue  # 我们已经对付过那些说真话的人了。

    # 这个“clue字典”有键为物品和嫌疑人。
    # 值为给出的线索:
    clues[interviewee] = {}
    clues[interviewee]['debug_liar'] = True  # 用于调试。

    # 这个受访者是个骗子，给出了错误的线索:
    for item in ITEMS:
        if random.randint(0, 1) == 0:
            while True:  # 选择一个随机的(错误的)地点线索
                # 在物品的位置上撒谎
                clues[interviewee][item] = random.choice(PLACES)
                if clues[interviewee][item] != PLACES[ITEMS.index(item)]:
                    # 当错误的线索被选择时跳出循环。
                    break
        else:
            while True:  # 选择一个随机的(错误的)可疑线索。
                clues[interviewee][item] = random.choice(SUSPECTS)
                if clues[interviewee][item] != SUSPECTS[ITEMS.index(item)]:
                    # 当错误的线索被选择时跳出循环。
                    break
    for suspect in SUSPECTS:
        if random.randint(0, 1) == 0:
            while True:  # 选择一个随机的(错误的)地点线索。
                clues[interviewee][suspect] = random.choice(PLACES)
                if clues[interviewee][suspect] != PLACES[ITEMS.index(item)]:
                    #当错误的线索被选择时跳出循环。
                    break
        else:
            while True:  # 选择一个随机的(错误的)道具线索。
                clues[interviewee][suspect] = random.choice(ITEMS)
                if clues[interviewee][suspect] != ITEMS[SUSPECTS.index(suspect)]:
                    # 当错误的线索被选择时跳出循环。
                    break

# 创建关于Zophie的线索的数据结构:
zophieClues = {}
for interviewee in random.sample(SUSPECTS, random.randint(3, 4)):
    kindOfClue = random.randint(1, 3)
    if kindOfClue == 1:
        if interviewee not in liars:
            # 他们会告诉你谁抓了Zophie。
            zophieClues[interviewee] = culprit
        elif interviewee in liars:
            while True:
                # 选择一个(错误的)可疑线索。
                zophieClues[interviewee] = random.choice(SUSPECTS)
                if zophieClues[interviewee] != culprit:
                    # 当错误的线索被选择时跳出循环。
                    break

    elif kindOfClue == 2:
        if interviewee not in liars:
            # 他们会告诉你Zophie在哪里。
            zophieClues[interviewee] = PLACES[SUSPECTS.index(culprit)]
        elif interviewee in liars:
            while True:
                # 选择一个(错误的)地点线索。
                zophieClues[interviewee] = random.choice(PLACES)
                if zophieClues[interviewee] != PLACES[SUSPECTS.index(culprit)]:
                    # 当错误的线索被选择时跳出循环。
                    break
    elif kindOfClue == 3:
        if interviewee not in liars:
            # 他们会告诉你Zophie在哪里。
            zophieClues[interviewee] = ITEMS[SUSPECTS.index(culprit)]
        elif interviewee in liars:
            while True:
                # 选择一个(错误的)道具线索。
                zophieClues[interviewee] = random.choice(ITEMS)
                if zophieClues[interviewee] != ITEMS[SUSPECTS.index(culprit)]:
                    # 当错误的线索被选择时跳出循环。
                    break

#实验:取消注释该代码以查看线索数据结构:
#import pprint
#pprint.pprint(clues)
#pprint.pprint(zophieClues)
#print('culprit =', culprit)

# 开始游戏
print("""J'ACCUSE! (a mystery game)")
By Al Sweigart al@inventwithpython.com
Inspired by Homestar Runner\'s "Where\'s an Egg?" game

You are the world-famous detective, Mathilde Camus.
ZOPHIE THE CAT has gone missing, and you must sift through the clues.
Suspects either always tell lies, or always tell the truth. Ask them
about other people, places, and items to see if the details they give are
truthful and consistent with your observations. Then you will know if
their clue about ZOPHIE THE CAT is true or not. Will you find ZOPHIE THE
CAT in time and accuse the guilty party?
""")
input('Press Enter to begin...')


startTime = time.time()
endTime = startTime + TIME_TO_SOLVE

while True:  # 主游戏循环
    if time.time() > endTime or accusationsLeft == 0:
        # 处理“游戏结束”条件:
        if time.time() > endTime:
            print('You have run out of time!')
        elif accusationsLeft == 0:
            print('You have accused too many innocent people!')
        culpritIndex = SUSPECTS.index(culprit)
        print('It was {} at the {} with the {} who catnapped her!'.format(culprit, PLACES[culpritIndex], ITEMS[culpritIndex]))
        print('Better luck next time, Detective.')
        sys.exit()

    print()
    minutesLeft = int(endTime - time.time()) // 60
    secondsLeft = int(endTime - time.time()) % 60
    print('Time left: {} min, {} sec'.format(minutesLeft, secondsLeft))

    if currentLocation == 'TAXI':
        print('  You are in your TAXI. Where do you want to go?')
        for place in sorted(PLACES):
            placeInfo = ''
            if place in visitedPlaces:
                placeInfo = visitedPlaces[place]
            nameLabel = '(' + place[0] + ')' + place[1:]
            spacing = " " * (LONGEST_PLACE_NAME_LENGTH - len(place))
            print('{} {}{}'.format(nameLabel, spacing, placeInfo))
        print('(Q)UIT GAME')
        while True:  # 一直问下去，直到得到一个有效的回答。
            response = input('> ').upper()
            if response == '':
                continue  # 在问一遍
            if response == 'Q':
                print('Thanks for playing!')
                sys.exit()
            if response in PLACE_FIRST_LETTERS.keys():
                break
        currentLocation = PLACE_FIRST_LETTERS[response]
        continue  # 回到主游戏循环的开始。

    # 在一个地方;玩家可以询问线索。
    print('  You are at the {}.'.format(currentLocation))
    currentLocationIndex = PLACES.index(currentLocation)
    thePersonHere = SUSPECTS[currentLocationIndex]
    theItemHere = ITEMS[currentLocationIndex]
    print('  {} with the {} is here.'.format(thePersonHere, theItemHere))

    # 把这里的嫌疑人和物品加到我们已知的嫌疑人和物品清单中
    if thePersonHere not in knownSuspectsAndItems:
        knownSuspectsAndItems.append(thePersonHere)
    if ITEMS[currentLocationIndex] not in knownSuspectsAndItems:
        knownSuspectsAndItems.append(ITEMS[currentLocationIndex])
    if currentLocation not in visitedPlaces.keys():
        visitedPlaces[currentLocation] = '({}, {})'.format(thePersonHere.lower(), theItemHere.lower())

    #如果玩家之前错误地指责了这个人，他们就不会提供线索:
    if thePersonHere in accusedSuspects:
        print('They are offended that you accused them,')
        print('and will not help with your investigation.')
        print('You go back to your TAXI.')
        print()
        input('Press Enter to continue...')
        currentLocation = 'TAXI'
        continue  # 回到主游戏循环的开始。

    # 显示已知的嫌疑人和物品的菜单来进行询问：
    print()
    print('(J) "J\'ACCUSE!" ({} accusations left)'.format(accusationsLeft))
    print('(Z) Ask if they know where ZOPHIE THE CAT is.')
    print('(T) Go back to the TAXI.')
    for i, suspectOrItem in enumerate(knownSuspectsAndItems):
        print('({}) Ask about {}'.format(i + 1, suspectOrItem))

    while True:  # 一直问下去，直到得到一个有效的回答。
        response = input('> ').upper()
        if response in 'JZT' or (response.isdecimal() and 0 < int(response) <= len(knownSuspectsAndItems)):
            break

    if response == 'J':  #玩家指控该嫌疑犯。
        accusationsLeft -= 1  # 用尽一个指控。
        if thePersonHere == culprit:
            # 你指控的嫌疑人是正确的。
            print('You\'ve cracked the case, Detective!')
            print('It was {} who had catnapped ZOPHIE THE CAT.'.format(culprit))
            minutesTaken = int(time.time() - startTime) // 60
            secondsTaken = int(time.time() - startTime) % 60
            print('Good job! You solved it in {} min, {} sec.'.format(minutesTaken, secondsTaken))
            sys.exit()
        else:
            # 你指控的嫌疑人是错误的。
            accusedSuspects.append(thePersonHere)
            print('You have accused the wrong person, Detective!')
            print('They will not help you with anymore clues.')
            print('You go back to your TAXI.')
            currentLocation = 'TAXI'

    elif response == 'Z':  # 玩家询问关于Zophie的情况。
        if thePersonHere not in zophieClues:
            print('"I don\'t know anything about ZOPHIE THE CAT."')
        elif thePersonHere in zophieClues:
            print('  They give you this clue: "{}"'.format(zophieClues[thePersonHere]))
            # 在已知事物列表中添加非地点的线索:
            if zophieClues[thePersonHere] not in knownSuspectsAndItems and zophieClues[thePersonHere] not in PLACES:
                knownSuspectsAndItems.append(zophieClues[thePersonHere])

    elif response == 'T':  # 玩家回到出租车上。
        currentLocation = 'TAXI'
        continue  # 回到主游戏循环的开始。

    else:  # 玩家询问嫌疑犯或道具。
        thingBeingAskedAbout = knownSuspectsAndItems[int(response) - 1]
        if thingBeingAskedAbout in (thePersonHere, theItemHere):
            print('  They give you this clue: "No comment."')
        else:
            print('  They give you this clue: "{}"'.format(clues[thePersonHere][thingBeingAskedAbout]))
            # 在已知事物列表中添加非地点的线索:
            if clues[thePersonHere][thingBeingAskedAbout] not in knownSuspectsAndItems and clues[thePersonHere][thingBeingAskedAbout] not in PLACES:
                knownSuspectsAndItems.append(clues[thePersonHere][thingBeingAskedAbout])

    input('Press Enter to continue...')
