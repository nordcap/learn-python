"""
Суть задачи та же, что и Caesar cipher, с одним отличием: кодируются символы из интервала
1F600—1F64F таблицы символов Юникода. Используется кодировка UTF-8.

Для всех символов сдвиг один и тот же. Сдвиг циклический, т.е. если к последнему символу алфавита
применить единичный сдвиг, то он заменится на первый символ, и наоборот.

Напишите программу, которая шифрует текст шифром Цезаря.

Формат ввода:
На первой строке указывается используемый сдвиг шифрования: целое число. Положительное число
соответствует сдвигу вправо. На второй строке указывается непустая фраза для шифрования.

Не обращайте внимания, если у вас отображаются прямоугольники вместо некоторых символов.
Это значит, что ваш шрифт не содержит этих символов. Для решения задачи это не имеет никакого значения.

Формат вывода:
Единственная строка, в которой записана фраза: Result: "..." , где вместо многоточия внутри
кавычек записана зашифрованная последовательность.
"""
a = int(input())  # сдвиг
b = input().strip()
c = [n for n in range(128512, 128592)]
res = []
len_c = len(c)
for i in b:
    res.append(c[(c.index(ord(i)) + a) % len_c])

print('Result: ', '"', ''.join((str(chr(i)) for i in res)), '"', sep='')
