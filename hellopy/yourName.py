# name = ''
# while name != 'your name':
#     print('Please type your name.')
#     name = input()
# print('Thank you!')   

"""
这个控制台输入竟然要带上 'sss', 'your name', 不然就被当成变量...
"""

# total = 0
# for num in range(5):
#     total = total + num
# print(total)

# for i in range(0, 10, 2):
#     print(i)

# for i in range(5, -1, -1):
#     print(i)    

# import random
# for i in range(5):
#     print(random.randint(1, 10))

# import sys
# while True:
#     print('Type exit to exit.')
#     response = input()
#     if response == 'exit':
#         sys.exit()
#     print('You typed ' + response + '.')

"""
vscode python run exit 不了一点啊 debug就正常exit了 不懂
"""   

# import random
# secretNumber = random.randint(1, 20)
# print('I am thinking of a number between 1 and 20.')

# for guessesTaken in range(1, 7):
#     print('Take a guess.')
#     guess = int(input())

#     if guess < secretNumber:
#         print('Your guess is too low.')
#     elif guess > secretNumber:
#         print('Your guess is too high.')
#     else:
#         break

# if guess == secretNumber:
#     print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
# else:
#     print('Nope. The number I was thinking of was ' + str(secretNumber))        

"""
剪刀石头布的源码就不手敲了resources里也有
第二章结束
"""