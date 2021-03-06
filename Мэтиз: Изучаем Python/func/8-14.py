"""
8-14. Автомобили: напишите функцию для сохранения информации об автомобиле в слова-
ре. Функция всегда должна возвращать производителя и название модели, но при этом она
может получать произвольное количество именованных аргументов. Вызовите функцию
с передачей обязательной информации и еще двух пар «имя—значение» (например, цвет
и комплектация). Ваша функция должна работать для вызовов следующего вида:
car = make_car(‘subaru’, ‘outback’, color=’blue’, tow_package=True)
Выведите возвращаемый словарь и убедитесь в том, что вся информация была сохранена
правильно.
"""


def build_car(name, builder, **info):
    profile = {}
    profile['name'] = name
    profile['builder'] = builder
    for key, value in info.items():
        profile[key] = value
    return profile


car_profile = build_car('УАЗ', 'УАЗ', color='зеленый', top_package=False)
print(car_profile)
