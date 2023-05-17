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

# print('Hello')
# print('World')
# print('Hello', end='')
# print('World')
# print('cats', 'dogs', 'mice')
# print('cats', 'dogs', 'mice', sep=',')

"""
python真有意思 关键字参数
"""

# def spam():
#     eggs = 'spam local'
#     print(eggs)

# def bacon():
#     eggs = 'bacon local'
#     print(eggs)
#     spam()
#     print(eggs)

# eggs = 'global'
# bacon()
# print(eggs)

"""
避免重复命名，但是可以重复，重复的时候感觉是就近原则，局部变量互相隔离
"""

# def spam():
#     global eggs
#     eggs = 'spam' # glocal

# def bacon():
#     eggs = 'bacon' # local

# def ham():
#     print(eggs) # global

# eggs = 42 # global
# spam()
# print(eggs)

"""
以及python不会默认引用全局变量 看下边的例子
"""

# def spam():
#     print(eggs) #ERROR local variable 'eggs' referenced before assignment
#     eggs = 'span local'

# eggs = 'global'
# spam()

"""
引用全局变量必须global var
"""

# def spam(divideBy):
#     try:
#         return 42 / divideBy
#     except ZeroDivisionError:
#         print("Error! Invalid argument.")

# print(spam(2))
# print(spam(0))
# print(spam(6))

"""
try catch
"""

# import time, sys
# indent = 0
# indentIncreasing = True

# try:
#     while True:
#         print('  ' * indent, end = '')
#         print('********')
#         time.sleep(0.1)

#         if indentIncreasing:
#             indent = indent + 1
#             if indent == 20:
#                 indentIncreasing = False
#         else:
#             indent = indent - 1
#             if indent == 0:
#                 indentIncreasing = True
# except KeyboardInterrupt:
#     sys.exit()                        

"""
control+z quit
"""

def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

def cal():
    result = collatz(int(input()))
    print(result)
    while result != 1:
        result = collatz(result)
        print(result)

cal()  

"""
3.12.1 课后练习 Collatz序列
额，对比了一下collatz.py的实现，哈哈完犊子
"""