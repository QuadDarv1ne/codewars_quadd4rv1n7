'''
[ Simple frequency sort ]

In this kata, you will sort elements in an array by decreasing frequency of elements.
If two elements have the same frequency, sort them by increasing value.

solve([2,3,5,3,7,9,5,3,7]) = [3,3,3,5,5,7,7,2,9]
-- We sort by highest frequency to lowest frequency.
-- If two elements have same frequency, we sort by increasing value.
More examples in test cases.

Good luck.
'''


from collections import Counter

def solve(arr):
    # Step 1: Count the frequency of each element in the array
    freq = Counter(arr)
    
    # Step 2: Sort the array using a custom key
    # First by frequency in descending order, then by value in ascending order
    sorted_arr = sorted(arr, key=lambda x: (-freq[x], x))
    
    return sorted_arr


# TODO: Заметки
## Автор: Дуплей Максим Игоревич / Dupley Maxim Igorevich
## Дата: 30.11.2024
