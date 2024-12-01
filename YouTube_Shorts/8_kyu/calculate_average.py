'''
[ Calculate average ]

Write a function which calculates the average of the numbers in a given array.

Note: Empty arrays should return 0.
'''


def find_average(numbers):
    # Проверка, пуст ли список
    if len(numbers) == 0:
        return 0  # Если список пустой, возвращаем 0
    
    # Вычисление среднего арифметического
    # Сначала суммируем все элементы списка, затем делим на количество элементов
    return sum(numbers) / len(numbers)

# TODO: Заметки
## Автор: Дуплей Максим Игоревич / Dupley Maxim Igorevich
## Дата: 30.11.2024
