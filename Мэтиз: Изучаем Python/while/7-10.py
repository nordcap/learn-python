"""
Отпуск мечты: напишите программу, которая опрашивает пользователей, где бы они
хотели провести отпуск. Включите блок кода для вывода результатов опроса.
"""
holiday = []
while True:
    answer = input("Где бы вы хотели провести отпуск? -")
    if answer == 'quit': break
    holiday.append(answer)

print("Результаты опроса: ")
for i in holiday:
    print(i)
