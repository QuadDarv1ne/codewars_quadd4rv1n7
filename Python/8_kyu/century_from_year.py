'''
[ Century From Year ]

Introduction:
The first century spans from the year 1 up to and including the year 100, the second century - from the year 101 up to and including the year 200, etc.

Task:
Given a year, return the century it is in.

Examples:
1705 --> 18
1900 --> 19
1601 --> 17
2000 --> 20
2742 --> 28

Note: this kata uses strict construction as shown in the description and the examples, you can read more about it here
'''


def century(year):
    # If the year is divisible by 100, it's the century itself, else we add 1 to the result
    return (year + 99) // 100


# TODO: Заметки
## Автор: Дуплей Максим Игоревич / Dupley Maxim Igorevich
## Дата: 02.12.2024
