"""
В римской системе счисления для обозначения чисел используются следующие символы (справа записаны числа, которым они соответствуют в десятичной системе счисления):
I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000
Будем использовать вариант, в котором числа 4, 9, 40, 90, 400 и 900 записываются как вычитание из большего числа меньшего: IV, IX, XL, XC, CD и CM, соответственно.
Напишите программу, которая переводит число из римской в десятичную систему счисления.
Формат ввода:
Строка, содержащая число, закодированное в римской системе счисления. Гарантируется, что число меньше 4000.
Формат вывода:
Строка, содержащая число в десятичной системе счисления, соответствующее введённому.
Sample Input 1:
MCMLXXXIV
Sample Output 1:
1984
Sample Input 2:
IX
Sample Output 2:
9
Sample Input 3:
III
Sample Output 3:
3
Нажмите, чтобы начать решать ✍
"""
import re

roman = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}
roman_ext = {
    'IV': 4,
    'IX': 9,
    'XL': 40,
    'XC': 90,
    'CD': 400,
    'CM': 900
}

Lat_s = input()
for key_rep in roman_ext:
    Lat_s = Lat_s.replace(key_rep, str(roman_ext[key_rep]))
for key_rep in roman:
    Lat_s = Lat_s.replace(key_rep, str(roman[key_rep]))

find_all = re.findall(r"([1-9]{1}[0]*)", Lat_s)
decimal = 0
for i in find_all:
    decimal += int(i)

print(decimal)