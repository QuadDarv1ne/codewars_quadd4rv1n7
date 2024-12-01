'''
[ Highest Scoring Word ]

Given a string of words, you need to find the highest scoring word.
Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
For example, the score of abad is 8 (1 + 2 + 1 + 4).
You need to return the highest scoring word as a string.
If two words score the same, return the word that appears earliest in the original string.
All letters will be lowercase and all inputs will be valid.
'''


def high(x):
    # Function to calculate the sum of letter values for a word
    def word_value(word):
        return sum(ord(c) - ord('a') + 1 for c in word)
    
    # Split the string into words
    words = x.split()
    
    # Find the word with the highest value
    return max(words, key=word_value)


# TODO: Заметки
## Автор: Дуплей Максим Игоревич / Dupley Maxim Igorevich
## Дата: 29.11.2024
