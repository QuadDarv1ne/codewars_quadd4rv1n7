'''
[ Find the unique number ]

There is an array with some numbers.
All numbers are equal except for one.
Try to find it.

findUniq([ 1, 1, 1, 2, 1, 1 ]) === 2
findUniq([ 0, 0, 0.55, 0, 0 ]) === 0.55

It’s guaranteed that array contains at least 3 numbers.
The tests contain some very huge arrays, so think about performance.
'''


def find_uniq(arr):
    # Если первые два элемента разные, то уникальное число - это либо arr[0], либо arr[1]
    if arr[0] != arr[1]:
        # Сравниваем с третьим элементом, чтобы понять, какое число уникальное
        return arr[2] if arr[2] == arr[0] else arr[0]
    
    # Если первые два элемента одинаковы, то уникальное число отличается от arr[0]
    return next(num for num in arr if num != arr[0])


# TODO: Заметки
## Автор: Дуплей Максим Игоревич / Dupley Maxim Igorevich
## Дата: 30.11.2024
