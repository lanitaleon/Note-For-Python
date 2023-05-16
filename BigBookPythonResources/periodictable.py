"""元素周期表, 作者：Al Sweigart al@inventwithpython.com
显示所有元素的原子信息。
此代码可在https://nostarch.com/big-book-small-python-programming获得
标签:短,科学"""

# 数据来源：https://en.wikipedia.org/wiki/List_of_chemical_elements
# 突出显示表格，复制它，然后粘贴到如Excel或谷歌表格一个电子表格程序 ，如https://invpy.com/elements
# 然后将该文件保存为periodictable.csv。
# 或从https://invpy.com/periodictable.csv下载此csv文件

import csv, sys, re

# 从periodictable.csv中读取所有数据。
elementsFile = open('periodictable.csv', encoding='utf-8')
elementsCsvReader = csv.reader(elementsFile)
elements = list(elementsCsvReader)
elementsFile.close()

ALL_COLUMNS = ['Atomic Number', 'Symbol', 'Element', 'Origin of name',
               'Group', 'Period', 'Atomic weight', 'Density',
               'Melting point', 'Boiling point',
               'Specific heat capacity', 'Electronegativity',
               'Abundance in earth\'s crust']

# 为了调整文本，我们需要找到ALL_COLUMNS中最长的字符串。
LONGEST_COLUMN = 0
for key in ALL_COLUMNS:
    if len(key) > LONGEST_COLUMN:
        LONGEST_COLUMN = len(key)

# 将所有的元素数据放到一个数据结构中:
ELEMENTS = {}  # 存储所有元素数据的数据结构。
for line in elements:
    element = {'Atomic Number':  line[0],
               'Symbol':         line[1],
               'Element':        line[2],
               'Origin of name': line[3],
               'Group':          line[4],
               'Period':         line[5],
               'Atomic weight':  line[6] + ' u', # 原子质量单位
               'Density':        line[7] + ' g/cm^3', # 克/立方厘米
               'Melting point':  line[8] + ' K', # kelvin
               'Boiling point':  line[9] + ' K', # kelvin
               'Specific heat capacity':      line[10] + ' J/(g*K)',
               'Electronegativity':           line[11],
               'Abundance in earth\'s crust': line[12] + ' mg/kg'}

    # 一些数据包含了我们想要的来自维基百科的文本
    # 去除，如硼的原子量:
    # "10.81[III][IV][V][VI]" 应该变成 "10.81"

    for key, value in element.items():
        # 删除[罗马数字]文本:
        element[key] = re.sub(r'\[(I|V|X)+\]', '', value)

    ELEMENTS[line[0]] = element  # 将原子序数映射到元素。
    ELEMENTS[line[1]] = element  # 将符号映射到元素。

print('Periodic Table of Elements')
print('By Al Sweigart al@inventwithpython.com')
print()

while True:  # 主程序循环。
    # 显示表格并让用户选择一个元素:
    print('''            Periodic Table of Elements
      1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18
    1 H                                                  He
    2 Li Be                               B  C  N  O  F  Ne
    3 Na Mg                               Al Si P  S  Cl Ar
    4 K  Ca Sc Ti V  Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr
    5 Rb Sr Y  Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I  Xe
    6 Cs Ba La Hf Ta W  Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn
    7 Fr Ra Ac Rf Db Sg Bh Hs Mt Ds Rg Cn Nh Fl Mc Lv Ts Og

            Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu
            Th Pa U  Np Pu Am Cm Bk Cf Es Fm Md No Lr''')
    print('Enter a symbol or atomic number to examine, or QUIT to quit.')
    response = input('> ').title()

    if response == 'Quit':
        sys.exit()

    # 显示所选元素的数据:
    if response in ELEMENTS:
        for key in ALL_COLUMNS:
            keyJustified = key.rjust(LONGEST_COLUMN)
            print(keyJustified + ': ' + ELEMENTS[response][key])
        input('Press Enter to continue...')
