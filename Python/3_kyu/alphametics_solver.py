import re

def is_valid_solution(words, result, letter_to_digit):
    def word_to_number(word):
        return int("".join(letter_to_digit[letter] for letter in word))

    # Проверка ведущих нулей
    if any(letter_to_digit[word[0]] == '0' for word in words + [result]):
        return False

    # Проверка суммы
    total = sum(word_to_number(word) for word in words)
    return total == word_to_number(result)

def solve_recursive(words, result, unique_letters, used_digits, letter_to_digit):
    # Если все буквы уже распределены, проверяем решение
    if not unique_letters:
        return is_valid_solution(words, result, letter_to_digit)

    # Берём следующую букву для назначения
    letter = unique_letters[0]
    for digit in '0123456789':
        # Пропускаем уже использованные цифры
        if digit in used_digits:
            continue

        # Назначаем цифру букве
        letter_to_digit[letter] = digit
        used_digits.add(digit)

        # Рекурсивно решаем оставшуюся часть
        if solve_recursive(words, result, unique_letters[1:], used_digits, letter_to_digit):
            return True

        # Отмена назначения (backtracking)
        used_digits.remove(digit)
        del letter_to_digit[letter]

    return False

def alphametics(puzzle):
    # Парсим слова и результат
    words = re.findall(r'\b[A-Z]+\b', puzzle)
    result = words.pop()
    unique_letters = set(''.join(words + [result]))

    # Если слишком много уникальных букв
    if len(unique_letters) > 10:
        return "Too many unique letters, cannot solve"

    # Список уникальных букв для упорядоченного перебора
    unique_letters = list(unique_letters)

    # Инициализация словаря и множества использованных цифр
    letter_to_digit = {}
    used_digits = set()

    # Решение с помощью рекурсивного поиска
    if solve_recursive(words, result, unique_letters, used_digits, letter_to_digit):
        # Преобразуем слова и результат с заменой букв на цифры
        def translate(word):
            return "".join(letter_to_digit[letter] for letter in word)

        translated_words = [translate(word) for word in words]
        translated_result = translate(result)
        return f"{' + '.join(translated_words)} = {translated_result}"
    else:
        return "No solution found"

"""
Автор: Дуплей Максим Игоревич
TG: @quadd4rv1n7
Дата: 21.12.2024
"""
