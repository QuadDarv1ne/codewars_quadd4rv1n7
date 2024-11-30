'''
[ Duplicate Encoder ]

The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string.
Ignore capitalization when determining if a character is a duplicate.

Examples:
"din"     => "((("
"recede"  => "()()()"
"Success" => ")())())"
"(( @"    => "))((" 

Notes:
Assertion messages may be unclear about what they display in some languages.
If you read "...It Should encode XXX", the "XXX" is the expected result, not the input.
'''


from collections import Counter

def duplicate_encode(word):
    # Normalize to lowercase
    word_lower = word.lower()
    
    # Count occurrences of each character
    char_count = Counter(word_lower)
    
    # Build the result string based on the character frequencies
    return ''.join('(' if char_count[char] == 1 else ')' for char in word_lower)


# TODO: Заметки
## Автор: Дуплей Максим Игоревич / Dupley Maxim Igorevich
## Дата: 30.11.2024
