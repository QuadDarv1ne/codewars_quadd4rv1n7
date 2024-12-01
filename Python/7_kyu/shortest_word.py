'''
[ Shortest Word ]

Simple, given a string of words, return the length of the shortest word(s).
String will never be empty and you do not need to account for different data types.
'''


def find_short(s):
    # Разделяем строку на слова и находим минимальную длину
    return min(len(word) for word in s.split())


# TODO: Заметки
## Автор: Дуплей Максим Игоревич / Dupley Maxim Igorevich
## Дата: 01.12.2024
