'''
[ Triple trouble ]

Write a function

triple_double(num1, num2)
which takes numbers num1 and num2 and returns 1 if there is a straight triple of a number at any place in num1 and also a straight double of the same number in num2.

If this isn't the case, return 0

Examples:
triple_double(451999277, 41177722899) == 1
# num1 has straight triple 999s and num2 has straight double 99s

triple_double(1222345, 12345) == 0
# num1 has straight triple 2s but num2 has only a single 2

triple_double(12345, 12345) == 0

triple_double(666789, 12345667) == 1
'''


def triple_double(num1, num2):
    # Преобразуем числа в строки для удобства
    str_num1 = str(num1)
    str_num2 = str(num2)
    
    # Проходим по всем цифрам в num1, ищем тройки одинаковых цифр
    for digit in range(10):
        digit = str(digit)
        if digit * 3 in str_num1 and digit * 2 in str_num2:
            return 1
    
    # Если не нашли, возвращаем 0
    return 0


# TODO: Заметки
## Автор: Дуплей Максим Игоревич / Dupley Maxim Igorevich
## Дата: 30.11.2024
