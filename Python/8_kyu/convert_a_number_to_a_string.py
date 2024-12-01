'''
[ Convert a Number to a String ]

We need a function that can transform a number (integer) into a string.
What ways of achieving this do you know ?

Examples (input --> output):
123  --> "123"
999  --> "999"
-100 --> "-100"
'''

# Using str()
def number_to_string(num):
    return str(num)

# Using format()
def number_to_string(num):
    return "{}".format(num)

# Using f-strings (available from Python 3.6)
def number_to_string(num):
    return f"{num}"

# Using repr()
def number_to_string(num):
    return repr(num)


# TODO: Заметки
## Автор: Дуплей Максим Игоревич / Dupley Maxim Igorevich
## Дата: 30.11.2024
