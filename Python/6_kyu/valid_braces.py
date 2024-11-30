'''
[ Valid Braces ]

Write a function that takes a string of braces, and determines if the order of the braces is valid.
It should return true if the string is valid, and false if it's invalid.
This Kata is similar to the Valid Parentheses Kata, but introduces new characters: brackets [], and curly braces {}.
Thanks to @arnedag for the idea!
All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: ()[]{}.

What is considered Valid ?
A string of braces is considered valid if all braces are matched with the correct brace.

Examples:
"(){}[]"   =>  True
"([{}])"   =>  True
"(}"       =>  False
"[(])"     =>  False
"[({})](]" =>  False
'''


def valid_braces(string):
    # Создаем словарь с парами открывающих и закрывающих скобок
    matching_braces = {')': '(', ']': '[', '}': '{'}
    stack = []

    for char in string:
        if char in matching_braces.values():  # Если это открывающая скобка
            stack.append(char)
        elif char in matching_braces.keys():  # Если это закрывающая скобка
            if stack and stack[-1] == matching_braces[char]:
                stack.pop()  # Убираем из стека, если последняя скобка совпадает
            else:
                return False  # Некорректная последовательность
    return len(stack) == 0  # Если стек пуст, скобки сбалансированы


# TODO: Заметки
## Автор: Дуплей Максим Игоревич / Dupley Maxim Igorevich
## Дата: 30.11.2024
