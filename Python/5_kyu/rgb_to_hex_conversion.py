'''
[ RGB To Hex Conversion ]

The rgb function is incomplete.
Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned.
Valid decimal values for RGB are 0 - 255.
Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

Examples (input --> output):
255, 255, 255 --> "FFFFFF"
255, 255, 300 --> "FFFFFF"
0, 0, 0       --> "000000"
148, 0, 211   --> "9400D3"
'''


def rgb(r, g, b):
    # Ограничиваем значения для каждого цвета диапазоном от 0 до 255
    # Если значение меньше 0, то оно будет заменено на 0, если больше 255, то на 255.
    r = max(0, min(255, r))
    g = max(0, min(255, g))
    b = max(0, min(255, b))

    # Преобразуем каждый компонент в шестнадцатеричное представление
    # '{:02X}' - форматирует число в строку с двумя символами в верхнем регистре
    # Если число меньше 16 (например, 5), то оно будет представлено как '05'
    return '{:02X}{:02X}{:02X}'.format(r, g, b)


# TODO: Заметки
## Автор: Дуплей Максим Игоревич / Dupley Maxim Igorevich
## Дата: 30.11.2024
