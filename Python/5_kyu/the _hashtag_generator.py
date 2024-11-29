'''
[ The Hashtag Generator ]

The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:
It must start with a hashtag (#).
All words must have their first letter capitalized.
If the final result is longer than 140 chars it must return false.
If the input or the result is an empty string it must return false.

Examples:
" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false
'''


def generate_hashtag(s):
    # Убираем пробелы в начале и конце строки и разбиваем строку на слова
    words = s.strip().split()
    
    # Если строка пустая после удаления пробелов, возвращаем False
    if not words:
        return False
    
    # Создаем хэштег, объединяя слова с заглавными первыми буквами
    hashtag = '#' + ''.join(word.capitalize() for word in words)
    
    # Проверяем длину хэштега
    return hashtag if 1 < len(hashtag) <= 140 else False


# TODO: Заметки
## Автор: Дуплей Максим Игоревич / Dupley Maxim Igorevich
## Дата: 29.11.2024
