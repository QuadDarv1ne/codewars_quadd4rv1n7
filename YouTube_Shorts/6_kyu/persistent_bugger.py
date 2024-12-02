'''
[ . Persistent Bugger . ]

Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.

For example (Input --> Output):
39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit, there are 3 multiplications)
999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2, there are 4 multiplications)
4 --> 0 (because 4 is already a one-digit number, there is no multiplication)
'''


def persistence(num):
    count = 0
    while num >= 10:  # Continue until the number is a single digit
        num = multiply_digits(num)
        count += 1
    return count

def multiply_digits(n):
    result = 1
    while n > 0:
        result *= n % 10
        n //= 10
    return result


# TODO: Заметки
## Автор: Дуплей Максим Игоревич / Dupley Maxim Igorevich
## Дата: 29.11.2024
