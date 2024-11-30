'''
[ Mumbling ]

This time no story, no theory.
The examples below show you how to write function accum.

Examples:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z.
'''


def accum(st):
    # Iterate over the string and create the necessary pattern for each character
    return '-'.join([(ch * (i + 1)).capitalize() for i, ch in enumerate(st)])


# TODO: Заметки
## Автор: Дуплей Максим Игоревич / Dupley Maxim Igorevich
## Дата: 30.11.2024
