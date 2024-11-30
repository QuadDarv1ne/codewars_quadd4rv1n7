'''
[ Sum by Factors ]

Given an array of positive or negative integers I= [i1,..,in] you have to produce a sorted array P of the form [ [p, sum of all ij of I for which p is a prime factor (p positive) of ij] ...]
P will be sorted by increasing order of the prime numbers.
The final result has to be given as a string in Java, C#, C, C++ and as an array of arrays in other languages.

Example:
I = [12, 15] # result = [[2, 12], [3, 27], [5, 15]]
[2, 3, 5] is the list of all prime factors of the elements of I, hence the result.

Notes:
It can happen that a sum is 0 if some numbers are negative.
Example: I = [15, 30, -45] 5 divides 15, 30 and (-45) so 5 appears in the result, the sum of the numbers for which 5 is a factor is 0 so we have [5, 0] in the result amongst others.

In Fortran - as in any other language - the returned string is not permitted to contain any redundant trailing whitespace: you can use dynamically allocated character strings.
'''


import math

# Функция для нахождения всех простых делителей числа
def prime_factors(n):
    factors = set()
    # Обработка 2 отдельно, чтобы избежать четных чисел
    while n % 2 == 0:
        factors.add(2)
        n //= 2
    # Обработка нечетных чисел начиная с 3
    for i in range(3, int(math.sqrt(abs(n))) + 1, 2):
        while n % i == 0:
            factors.add(i)
            n //= i
    # Если n все еще больше 2, то это простое число
    if abs(n) > 2:
        factors.add(abs(n))
    return factors

# Функция для суммирования чисел по простым делителям
def sum_for_list(lst):
    prime_sums = {}
    
    # Для каждого числа в списке находим его простые делители
    for num in lst:
        factors = prime_factors(num)
        for factor in factors:
            if factor not in prime_sums:
                prime_sums[factor] = 0
            prime_sums[factor] += num
    
    # Преобразуем словарь в отсортированный список списков
    result = [[prime, prime_sums[prime]] for prime in sorted(prime_sums)]
    
    return result


# TODO: Заметки
## Автор: Дуплей Максим Игоревич / Dupley Maxim Igorevich
## Дата: 30.11.2024
