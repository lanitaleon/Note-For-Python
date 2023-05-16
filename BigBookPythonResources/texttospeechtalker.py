"""文字转语音，作者：Al Sweigart al@inventwithpython.com
使用 pyttsx3 的文本到语音功能的示例程序
模块。
在 https://nostarch.com/big-book-small-python-projects 查看此代码
标签: 小, 初学者"""

import sys

try:
    import pyttsx3
except ImportError:
    print('The pyttsx3 module needs to be installed to run this')
    print('program. On Windows, open a Command Prompt and run:')
    print('pip install pyttsx3')
    print('On macOS and Linux, open a Terminal and run:')
    print('pip3 install pyttsx3')
    sys.exit()

tts = pyttsx3.init()  # 初始化 TTS 引擎。

print('Text To Speech Talker, by Al Sweigart al@inventwithpython.com')
print('Text-to-speech using the pyttsx3 module, which in turn uses')
print('the NSSpeechSynthesizer (on macOS), SAPI5 (on Windows), or')
print('eSpeak (on Linux) speech engines.')
print()
print('Enter the text to speak, or QUIT to quit.')
while True:
    text = input('> ')

    if text.upper() == 'QUIT':
        print('Thanks for playing!')
        sys.exit()

    tts.say(text)  # 为 TTS 引擎添加一些文字。
    tts.runAndWait()  # 让 TTS 引擎说出来。
