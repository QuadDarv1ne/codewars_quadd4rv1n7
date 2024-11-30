'''
[ Consonant value ]

Given a lowercase string that has alphabetic characters only and no spaces, return the highest value of consonant substrings.
Consonants are any letters of the alphabet except "aeiou".
We shall assign the following values: a = 1, b = 2, c = 3, .... z = 26.

For example, for the word "zodiacs", let's cross out the vowels. We get: "z o d ia c"
"zodiac" -> 26

The consonant substrings are: "z", "d" and "c" with values "z" = 26, "di" = 4 and "c" = 3. The highest is 26.
"strength" -> 57

The consonant substrings are: "str" and "ngth" with values "str" = 19 + 20 + 18 = 57 and "ngth" = 14 + 7 + 20 + 8 = 49. The highest is 57.
For C: do not mutate input.
More examples in test cases. Good luck.
'''


def solve(s):
    max_value = 0
    current_value = 0
    consonants = "bcdfghjklmnpqrstvwxyz"  # Согласные буквы
    
    for char in s:
        if char in consonants:
            # Если символ согласный, добавляем его значение
            current_value += ord(char) - ord('a') + 1
        else:
            # Если символ гласный, проверяем и сбрасываем текущую подстроку
            max_value = max(max_value, current_value)
            current_value = 0
    
    # Для последней подстроки, если она закончилась на согласную
    max_value = max(max_value, current_value)
    
    return max_value


# TODO: Заметки
## Автор: Дуплей Максим Игоревич / Dupley Maxim Igorevich
## Дата: 30.11.2024
