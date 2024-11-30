'''
[ String ends with ? ]

Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

Examples:
solution('abc', 'bc') # returns true
solution('abc', 'd') # returns false
'''


def solution(text, ending):
    # Проверяем, заканчивается ли строка `text` на подстроку `ending`
    return text.endswith(ending)


# TODO: Заметки
## Автор: Дуплей Максим Игоревич / Dupley Maxim Igorevich
## Дата: 30.11.2024
