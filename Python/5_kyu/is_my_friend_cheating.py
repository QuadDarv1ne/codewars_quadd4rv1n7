'''
[ Is my friend cheating ? ]

A friend of mine takes the sequence of all numbers from 1 to n (where n > 0).
Within that sequence, he chooses two numbers, a and b.
He says that the product of a and b should be equal to the sum of all numbers in the sequence, excluding a and b.
Given a number n, could you tell me the numbers he excluded from the sequence?
The function takes the parameter: n (n is always strictly greater than 0) and returns an array or a string (depending on the language) of the form:

[(a, b), ...] or [[a, b], ...] or {{a, b}, ...} or or [{a, b}, ...]
with all (a, b) which are the possible removed numbers in the sequence 1 to n.

[(a, b), ...] or [[a, b], ...] or {{a, b}, ...} or ... will be sorted in increasing order of the "a".

It happens that there are several possible (a, b).
The function returns an empty array (or an empty string) if no possible numbers are found which will prove that my friend has not told the truth (Go: in this case return nil).

Examples:
removNb(26) should return [(15, 21), (21, 15)]
or
removNb(26) should return { {15, 21}, {21, 15} }
or
removeNb(26) should return [[15, 21], [21, 15]]
or
removNb(26) should return [ {15, 21}, {21, 15} ]
or
removNb(26) should return "15 21, 21 15"
or in C: removNb(26) should return {{15, 21}{21, 15}} tested by way of strings.
Function removNb should return a pointer to an allocated array of Pair pointers, each one also allocated. 

Note:
See examples of returns for each language in "RUN SAMPLE TESTS"
'''


def remov_nb(n):
    # Calculate the sum of all numbers from 1 to n
    S = n * (n + 1) // 2
    
    result = []
    
    # Iterate over all possible values of a and b
    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):  # Ensure a < b
            if a * b == S - a - b:
                result.append((a, b))
                result.append((b, a))  # Add the reversed pair (b, a)
    
    return result


# TODO: Заметки
## Автор: Дуплей Максим Игоревич / Dupley Maxim Igorevich
## Дата: 30.11.2024
