'''
[ Smallest unused ID ]

Hey awesome programmer.
You've got much data to manage and of course you use zero-based and non-negative ID's to make each data item unique.
Therefore you need a method, which returns the smallest unused ID for your next new data item...

Note: The given array of used IDs may be unsorted.
For test reasons there may be duplicate IDs, but you don't have to find or remove them!
Go on and code some pure awesomeness.
'''


def next_id(arr):
    ids = set(arr)  # Convert to a set to remove duplicates
    i = 0
    while i in ids:  # Check for the smallest unused ID
        i += 1
    return i


# TODO: Заметки
## Автор: Дуплей Максим Игоревич / Dupley Maxim Igorevich
## Дата: 01.12.2024
