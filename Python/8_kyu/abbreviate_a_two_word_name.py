'''
[ Abbreviate a Two Word Name ]

Write a function to convert a name into initials.
This kata strictly takes two words with one space in between them.
The output should be two capital letters with a dot separating them.

It should look like this:
Sam Harris => S.H
patrick feeney => P.F
'''


def abbrev_name(name):
    # Split the name into two words
    first, last = name.split()
    # Take the first letter of each word, convert to uppercase, and join with a dot
    return f"{first[0].upper()}.{last[0].upper()}"


# TODO: Заметки
## Автор: Дуплей Максим Игоревич / Dupley Maxim Igorevich
## Дата: 30.11.2024
