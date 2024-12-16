'''
[ Predict your age ]

My grandfather always predicted how old people would get, and right before he passed away he revealed his secret!
In honor of my grandfather's memory we will write a function using his formula!
- Take a list of ages when each of your great-grandparent died.
- Multiply each number by itself.
- Add them all together.
- Take the square root of the result.
- Divide by two.

Example: predict_age(65, 60, 75, 55, 60, 63, 64, 45) == 86
Note: the result should be rounded down to the nearest integer.

Some random tests might fail due to a bug in the JavaScript implementation.
Simply resubmit if that happens to you.
'''


import math

def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    # Шаг 1: Возводим каждое значение возраста в квадрат
    squared_ages = [age_1 ** 2, age_2 ** 2, age_3 ** 2, age_4 ** 2, age_5 ** 2, age_6 ** 2, age_7 ** 2, age_8 ** 2]
    
    # Шаг 2: Суммируем все квадраты
    sum_of_squares = sum(squared_ages)
    
    # Шаг 3: Извлекаем квадратный корень из суммы
    square_root = math.sqrt(sum_of_squares)
    
    # Шаг 4: Делим на 2 и округляем в меньшую сторону
    result = math.floor(square_root / 2)
    
    return result

# Пример теста
# print(predict_age(65, 60, 75, 55, 60, 63, 64, 45))  # Должно вернуть 86


# TODO: Заметки
## Автор: Дуплей Максим Игоревич / Dupley Maxim Igorevich
## Дата: 16.12.2024