'''
[ Calculate average ]

Write a function which calculates the average of the numbers in a given array.

Note: Empty arrays should return 0.
'''


def find_average(numbers):
    # Check if the array is empty
    if len(numbers) == 0:
        return 0
    # Calculate the average by dividing the sum by the length of the array
    return sum(numbers) / len(numbers)


# TODO: Заметки
## Автор: Дуплей Максим Игоревич / Dupley Maxim Igorevich
## Дата: 30.11.2024
