import math
from functools import reduce

def list_position(word):
    """Возвращает позицию анаграммы слова в списке"""
    if len(word) == 1:
        return 1

    unique_words = sorted(list(set(word)))
    freq_letters = [word.count(letter) for letter in unique_words]
    # Общее количество возможных комбинаций
    total_combinations = math.factorial(len(word)) // reduce(lambda x, y: x * y, [math.factorial(freq) for freq in freq_letters])

    increment = [0] + [freq * total_combinations // len(word) for freq in freq_letters[:-1]]
    increment = [sum(increment[:i + 1]) for i in range(len(increment))]
    
    return increment[unique_words.index(word[0])] + list_position(word[1:])

"""
Автор: Дуплей Максим Игоревич
TG: @quadd4rv1n7
Дата: 21.12.2024
"""
