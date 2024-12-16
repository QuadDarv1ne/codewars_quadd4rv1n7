'''
[ Binary to Text (ASCII) Conversion ]

Write a function that takes in a binary string and returns the equivalent decoded text (the text is ASCII encoded).
Each 8 bits on the binary string represent 1 character on the ASCII table.
The input string will always be a valid binary string.
Characters can be in the range from "00000000" to "11111111" (inclusive)

Note: In the case of an empty binary string your function should return an empty string.
'''


def binary_to_string(binary):
    # Если строка пустая, возвращаем пустую строку
    if not binary:
        return ""
    
    # Разбиваем бинарную строку на блоки по 8 бит
    n = 8
    characters = [binary[i:i+n] for i in range(0, len(binary), n)]
    
    # Преобразуем каждый блок в символ
    text = ''.join(chr(int(char, 2)) for char in characters)
    
    return text


# TODO: Заметки
## Автор: Дуплей Максим Игоревич / Dupley Maxim Igorevich
## Дата: 16.12.2024