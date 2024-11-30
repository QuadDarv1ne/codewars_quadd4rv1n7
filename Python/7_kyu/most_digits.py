'''
[ Most digits ]

Find the number with the most digits.
If two numbers in the argument array have the same number of digits, return the first one in the array.
'''


def find_longest(numbers):
    return max(numbers, key=lambda x: len(str(abs(x))))


# TODO: Заметки
## Автор: Дуплей Максим Игоревич / Dupley Maxim Igorevich
## Дата: 30.11.2024
