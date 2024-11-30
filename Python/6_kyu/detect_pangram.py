'''
[ Detect Pangram ]

A pangram is a sentence that contains every single letter of the alphabet at least once.
For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram.
Return True if it is, False if not.
Ignore numbers and punctuation.
'''


import string

def is_pangram(st):
    # Приводим строку к нижнему регистру
    st = st.lower()

    # Создаём набор всех букв алфавита
    alphabet_set = set(string.ascii_lowercase)

    # Фильтруем строку, оставляя только буквы и преобразуем её в множество
    st_set = set(c for c in st if c in alphabet_set)

    # Сравниваем множества: если они равны, то строка — панграмма
    return st_set == alphabet_set


# TODO: Заметки
## Автор: Дуплей Максим Игоревич / Dupley Maxim Igorevich
## Дата: 30.11.2024
