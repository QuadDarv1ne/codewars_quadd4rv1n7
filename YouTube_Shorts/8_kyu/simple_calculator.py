'''
[ simple calculator ]

You are required to create a simple calculator that returns the result of addition, subtraction, multiplication or division of two numbers.

Your function will accept three arguments:
The first and second argument should be numbers.
The third argument should represent a sign indicating the operation to perform on these two numbers.
if the variables are not numbers or the sign does not belong to the list above a message "unknown value" must be returned.

Example:
calculator(1, 2, '+') => 3
calculator(1, 2, '$') # result will be "unknown value"
Good luck.
'''


def calculator(x, y, op):
    # Check if both x and y are numbers and if the operator is valid
    if isinstance(x, (int, float)) and isinstance(y, (int, float)):
        # Perform the operation based on the operator
        if op == '+':
            return x + y
        elif op == '-':
            return x - y
        elif op == '*':
            return x * y
        elif op == '/':
            if y != 0:  # Handle division by zero
                return x / y
            else:
                return "unknown value"  # Return unknown value for division by zero
        else:
            return "unknown value"  # If operator is not recognized
    else:
        return "unknown value"  # If either x or y is not a number


# TODO: Заметки
## Автор: Дуплей Максим Игоревич / Dupley Maxim Igorevich
## Дата: 30.11.2024
