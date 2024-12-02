'''
[ Highest and Lowest ]

In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

Examples:
- high_and_low("1 2 3 4 5") # return "5 1"
- high_and_low("1 2 -3 4 5") # return "5 -3"
- high_and_low("1 9 3 4 -5") # return "9 -5"

Notes:
All numbers are valid Int32, no need to validate them.
There will always be at least one number in the input string.
Output string must be two numbers separated by a single space, and highest number is first.
'''


def high_and_low(numbers):
    # Разделяем входную строку на список чисел и преобразуем каждое значение в целое число
    num_list = list(map(int, numbers.split()))
    
    # Находим максимальное значение в списке
    highest = max(num_list)
    
    # Находим минимальное значение в списке
    lowest = min(num_list)
    
    # Возвращаем результат в виде строки: сначала максимальное число, затем минимальное
    return f"{highest} {lowest}"


# TODO: Заметки
## Автор: Дуплей Максим Игоревич / Dupley Maxim Igorevich
## Дата: 02.12.2024
