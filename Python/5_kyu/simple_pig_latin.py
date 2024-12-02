'''
[ Simple Pig Latin ]

Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway
'''


def pig_it(text):
    words = text.split()
    result = []
    for word in words:
        if word.isalpha():  # Check if the word contains only alphabetic characters
            result.append(word[1:] + word[0] + "ay")
        else:  # If it's punctuation, leave it untouched
            result.append(word)
    return " ".join(result)


# TODO: Заметки
## Автор: Дуплей Максим Игоревич / Dupley Maxim Igorevich
## Дата: 02.12.2024
