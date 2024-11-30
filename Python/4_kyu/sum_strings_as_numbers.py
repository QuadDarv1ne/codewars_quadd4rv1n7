'''
[ Sum Strings as Numbers ]

Given the string representations of two integers, return the string representation of the sum of those integers.

For example: sumStrings('1','2') // => '3'

A string representation of an integer will contain no characters besides the ten numerals "0" to "9".
I have removed the use of BigInteger and BigDecimal in java.
Python: your solution need to work with huge numbers (about a milion digits), converting to int will not work.
'''


def sum_strings(a, b):
    # Если обе строки пустые, возвращаем '0'
    if not a and not b:
        return '0'
    
    # Если одна строка пустая, возвращаем другую строку
    if not a:
        return b
    if not b:
        return a
    
    # Инициализация индексов для обеих строк, которые будут идти с конца
    i, j = len(a) - 1, len(b) - 1
    carry = 0  # Перенос
    result = []  # Список для хранения результата
    
    # Процесс сложения
    while i >= 0 or j >= 0 or carry:
        # Получаем текущие цифры из обеих строк или 0, если строка уже завершена
        digit_a = int(a[i]) if i >= 0 else 0
        digit_b = int(b[j]) if j >= 0 else 0
        
        # Сложение цифр с учетом переноса
        total = digit_a + digit_b + carry
        
        # Новый перенос
        carry = total // 10
        
        # Добавляем цифру в результат
        result.append(str(total % 10))
        
        # Сдвигаем индексы
        i -= 1
        j -= 1
    
    # Результат в списке, нужно перевернуть, так как мы добавляли цифры справа налево
    result_str = ''.join(result[::-1])
    
    # Удаляем ведущие нули
    return result_str.lstrip('0') or '0'  # если строка пуста, возвращаем '0'


# TODO: Заметки
## Автор: Дуплей Максим Игоревич / Dupley Maxim Igorevich
## Дата: 30.11.2024
