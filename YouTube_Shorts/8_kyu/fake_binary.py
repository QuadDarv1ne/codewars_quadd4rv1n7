'''
[ Fake Binary ]

Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'.
Return the resulting string.

Note: input will never be an empty string
'''


def fake_bin(x):
    return ''.join('0' if int(i) < 5 else '1' for i in x)


# TODO: Заметки
## Автор: Дуплей Максим Игоревич / Dupley Maxim Igorevich
## Дата: 30.11.2024
