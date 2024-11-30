'''
[ Reverse FizzBuzz ]

FizzBuzz is often one of the first programming puzzles people learn. Now undo it with reverse FizzBuzz.
Write a function that accepts a string, which will always be a valid section of FizzBuzz.
Your function must return an array that contains the numbers in order to generate the given section of FizzBuzz.

Notes:
If the sequence can appear multiple times within FizzBuzz, return the numbers that generate the first instance of that sequence.
All numbers in the sequence will be greater than zero.
You will never receive an empty sequence.

Examples:
reverse_fizzbuzz("1 2 Fizz 4 Buzz")        -->  [1, 2, 3, 4, 5]
reverse_fizzbuzz("Fizz 688 689 FizzBuzz")  -->  [687, 688, 689, 690]
reverse_fizzbuzz("Fizz Buzz")              -->  [9, 10]
'''


def reverse_fizzbuzz(sequence):
    # Разбиваем строку на слова
    parts = sequence.split()
    
    # Ищем последовательность чисел
    result = []
    num = 1  # Начинаем с первого числа FizzBuzz
    
    for part in parts:
        # Находим следующее число для каждого элемента последовательности
        while True:
            if part == "Fizz" and num % 3 == 0 and num % 5 != 0:
                result.append(num)
                break
            elif part == "Buzz" and num % 5 == 0 and num % 3 != 0:
                result.append(num)
                break
            elif part == "FizzBuzz" and num % 3 == 0 and num % 5 == 0:
                result.append(num)
                break
            elif part.isdigit() and int(part) == num:
                result.append(num)
                break
            num += 1  # Переходим к следующему числу
    
    return result


# TODO: Заметки
## Автор: Дуплей Максим Игоревич / Dupley Maxim Igorevich
## Дата: 30.11.2024
