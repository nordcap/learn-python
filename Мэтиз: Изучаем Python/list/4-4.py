"""
Миллион: создайте список чисел от 1 до 1 000 000, затем воспользуйтесь циклом for
для вывода чисел. (Если вывод занимает слишком много времени, остановите его нажатием
Ctrl+C или закройте окно вывода.)
"""
lst = list(range(1,1000001))
for i in lst:
    print(i)