'''
[ Stop gninnipS My sdroW! ]

Write a function that takes in a string of one or more words, and returns the same string, but with all words that have five or more letters reversed (Just like the name of this Kata).
Strings passed in will consist of only letters and spaces.
Spaces will be included only when more than one word is present.

Examples:
"Hey fellow warriors"  --> "Hey wollef sroirraw" 
"This is a test        --> "This is a test" 
"This is another test" --> "This is rehtona test"
'''


def spin_words(sentence):
    # Разделяем строку на отдельные слова
    words = sentence.split()
    
    # Проходим по каждому слову и разворачиваем его, если его длина 5 или больше
    for i in range(len(words)):
        if len(words[i]) >= 5:
            words[i] = words[i][::-1]  # Разворачиваем слово
    
    # Объединяем слова обратно в строку и возвращаем результат
    return ' '.join(words)


# TODO: Заметки
## Автор: Дуплей Максим Игоревич / Dupley Maxim Igorevich
## Дата: 02.12.2024
