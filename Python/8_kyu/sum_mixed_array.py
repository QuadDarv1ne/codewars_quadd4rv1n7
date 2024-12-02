'''
[ Sum Mixed Array ]

Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.
Return your answer as a number.
'''


def sum_mix(arr):
    # Convert all elements to integers and return the sum
    return sum(int(x) for x in arr)


# TODO: Заметки
## Автор: Дуплей Максим Игоревич / Dupley Maxim Igorevich
## Дата: 02.12.2024
