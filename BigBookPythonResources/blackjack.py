"""二十一点，作者：Al Sweigart al@inventwithpython.com
经典的纸牌游戏也被称为21。（这个版本没有
分拆或保险。）
更多信息请访问：https://en.wikipedia.org/wiki/Blackjack
此代码可在 https://nostarch.com/big-book-small-python-programming 获得
标签: 大型, 游戏, 纸牌游戏"""

import random, sys

# 设置常量：
HEARTS   = chr(9829) # Character 9829 is '♥'.
DIAMONDS = chr(9830) # Character 9830 is '♦'.
SPADES   = chr(9824) # Character 9824 is '♠'.
CLUBS    = chr(9827) # Character 9827 is '♣'.
# （chr 代码列表位于 https://inventwithpython.com/charactermap）
BACKSIDE = 'backside'


def main():
    print('''Blackjack, by Al Sweigart al@inventwithpython.com

    Rules:
      Try to get as close to 21 without going over.
      Kings, Queens, and Jacks are worth 10 points.
      Aces are worth 1 or 11 points.
      Cards 2 through 10 are worth their face value.
      (H)it to take another card.
      (S)tand to stop taking cards.
      On your first play, you can (D)ouble down to increase your bet
      but must hit exactly one more time before standing.
      In case of a tie, the bet is returned to the player.
      The dealer stops hitting at 17.''')

    money = 5000
    while True:  # 主游戏循环。
        # 检查玩家是否已经用完钱：
        if money <= 0:
            print("You're broke!")
            print("Good thing you weren't playing with real money.")
            print('Thanks for playing!')
            sys.exit()

        # 让玩家输入他们在这一轮的赌注：
        print('Money:', money)
        bet = getBet(money)

        # 给庄家和玩家各两张牌：
        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]

        # 处理玩家动作：
        print('Bet:', bet)
        while True:  # 继续循环直到玩家站立或崩溃。
            displayHands(playerHand, dealerHand, False)
            print()

            # 检查玩家是否有超过21点：
            if getHandValue(playerHand) > 21:
                break

            # 获取玩家的移动，H、S 或 D：
            move = getMove(playerHand, money - bet)

            # 处理玩家动作：
            if move == 'D':
                # 玩家加倍下注，他们可以增加赌注：
                additionalBet = getBet(min(bet, (money - bet)))
                bet += additionalBet
                print('Bet increased to {}.'.format(bet))
                print('Bet:', bet)

            if move in ('H', 'D'):
                # 击中/加倍需要另一张牌。
                newCard = deck.pop()
                rank, suit = newCard
                print('You drew a {} of {}.'.format(rank, suit))
                playerHand.append(newCard)

                if getHandValue(playerHand) > 21:
                    # 玩家已经崩溃：
                    continue

            if move in ('S', 'D'):
                # 站立/加倍停止玩家的回合。
                break

        # 处理庄家的动作：
        if getHandValue(playerHand) <= 21:
            while getHandValue(dealerHand) < 17:
                # 庄家打：
                print('Dealer hits...')
                dealerHand.append(deck.pop())
                displayHands(playerHand, dealerHand, False)

                if getHandValue(dealerHand) > 21:
                    break  # 庄家已经破产了。
                input('Press Enter to continue...')
                print('\n\n')

        # 显示最后的手：
        displayHands(playerHand, dealerHand, True)

        playerValue = getHandValue(playerHand)
        dealerValue = getHandValue(dealerHand)
        # 处理玩家是赢、输还是平：
        if dealerValue > 21:
            print('Dealer busts! You win ${}!'.format(bet))
            money += bet
        elif (playerValue > 21) or (playerValue < dealerValue):
            print('You lost!')
            money -= bet
        elif playerValue > dealerValue:
            print('You won ${}!'.format(bet))
            money += bet
        elif playerValue == dealerValue:
            print('It\'s a tie, the bet is returned to you.')

        input('Press Enter to continue...')
        print('\n\n')


def getBet(maxBet):
    """询问玩家他们想在这一轮下注多少。"""
    while True:  # 继续询问，直到他们输入有效金额。
        print('How much do you bet? (1-{}, or QUIT)'.format(maxBet))
        bet = input('> ').upper().strip()
        if bet == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        if not bet.isdecimal():
            continue  # 如果玩家没有下注，请再次询问。

        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet  # 玩家输入了一个有效的赌注。


def getDeck():
    """返回所有 52 张牌的 (rank,suit) 元组列表。"""
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))  # 添加编号卡。
        for rank in ('J', 'Q', 'K', 'A'):
            deck.append((rank, suit))  # 添加人脸和王牌卡。
    random.shuffle(deck)
    return deck


def displayHands(playerHand, dealerHand, showDealerHand):
    """展示玩家和庄家的牌。 如果 showDealerHand 为 False，则隐藏庄家的第一张牌。"""
    print()
    if showDealerHand:
        print('DEALER:', getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print('DEALER: ???')
        # 隐藏庄家的第一张牌：
        displayCards([BACKSIDE] + dealerHand[1:])

    # 显示玩家的牌：
    print('PLAYER:', getHandValue(playerHand))
    displayCards(playerHand)


def getHandValue(cards):
    """返回卡片的价值。 人脸牌值 10，A 值 11 或 1（此功能选择最合适的 A 值）。"""
    value = 0
    numberOfAces = 0

    # 添加非 A 卡的值：
    for card in cards:
        rank = card[0]  # card 是一个像 (rank,suit) 这样的元组
        if rank == 'A':
            numberOfAces += 1
        elif rank in ('K', 'Q', 'J'):  # 人脸卡价值 10 分。
            value += 10
        else:
            value += int(rank)  # 编号卡值得他们的号码。

    # 添加 ace 的值：
    value += numberOfAces  # 每亩加1。
    for i in range(numberOfAces):
        # 如果可以在不破坏的情况下再添加 10 个，请执行以下操作：
        if value + 10 <= 21:
            value += 10

    return value


def displayCards(cards):
    """显示卡片列表中的所有卡片。"""
    rows = ['', '', '', '', '']  # 每行显示的文本。

    for i, card in enumerate(cards):
        rows[0] += ' ___  '  # 打印卡片的顶行。
        if card == BACKSIDE:
            # 打印卡片背面：
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '|_##| '
        else:
            # 打印卡片正面：
            rank, suit = card  # 卡片是元组数据结构。
            rows[1] += '|{} | '.format(rank.ljust(2))
            rows[2] += '| {} | '.format(suit)
            rows[3] += '|_{}| '.format(rank.rjust(2, '_'))

    # 在屏幕上打印每一行：
    for row in rows:
        print(row)


def getMove(playerHand, money):
    """询问玩家的移动，并返回“H”表示击球，“S”表示站立，“D”表示双下。"""
    while True:  # 继续循环直到玩家输入正确的动作。
        # 确定玩家可以进行哪些移动：
        moves = ['(H)it', '(S)tand']

        # 玩家可以在他们的第一步加倍下注，我们可以看出这是因为他们将正好有两张牌：
        if len(playerHand) == 2 and money > 0:
            moves.append('(D)ouble down')

        # 获取玩家的动作：
        movePrompt = ', '.join(moves) + '> '
        move = input(movePrompt).upper()
        if move in ('H', 'S'):
            return move  # 玩家输入了一个有效的移动。
        if move == 'D' and '(D)ouble down' in moves:
            return move  # 玩家输入了一个有效的移动。


# 如果程序运行（而不是导入），运行游戏：
if __name__ == '__main__':
    main()
