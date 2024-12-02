'''
[ Evaluate mathematical expression ]

Instructions:
Given a mathematical expression as a string you must return the result as a number.

Numbers:
Number may be both whole numbers and/or decimal numbers.
The same goes for the returned result.

Operators:
You need to support the following mathematical operators:
1. Multiplication *
2. Division / (as floating point division)
3. Addition +
4. Subtraction -

Operators are always evaluated from left-to-right, and * and / must be evaluated before + and -.

Parentheses:
You need to support multiple levels of nested parentheses, ex. (2 / (2 + 3.33) * 4) - -6

Whitespace:
There may or may not be whitespace between numbers and operators.

An addition to this rule is that the minus sign (-) used for negating numbers and parentheses will never be separated by whitespace.
I.e all of the following are valid expressions.

1-1    // 0
1 -1   // 0
1- 1   // 0
1 - 1  // 0
1- -1  // 2
1 - -1 // 2
1--1   // 2
6 + -(4)   // 2
6 + -( -4) // 10

And the following are invalid expressions
1 - - 1    // Invalid
1- - 1     // Invalid
6 + - (4)  // Invalid
6 + -(- 4) // Invalid

Validation:
You do not need to worry about validation - you will only receive valid mathematical expressions following the above rules.

Restricted APIs:
NOTE: eval and exec are disallowed in your solution.
'''


def without_para(exp):
    numbers = []
    ops = []
    exp = "".join(exp.split())
    i = 0
    while i < len(exp):
        num = ""
        while i < len(exp) and exp[i] not in "+-*/":
            num += exp[i]
            i+=1
        numbers.append(num)
        if i != len(exp):
            ops.append(exp[i])
            i+=1
    #Complete double minuses
    j = 0
    while j < len(numbers):
        if numbers[j] == "":
            numbers.pop(j)
            a = numbers.pop(j)
            ops.pop(j)
            minus = True
            while a == "":
                minus = not minus
                a = numbers.pop(j)
                ops.pop(j)
            if minus:
                numbers.insert(j,-float(a))
            else:
                numbers.insert(j, float(a))
        j+=1
    #Finish * and /
    while "*" in ops or "/" in ops:
        count_star = find_index(ops,"*")
        count_div = find_index(ops, "/")
        if count_star < count_div:
            ops.pop(count_star)
            operand_a = numbers.pop(count_star)
            operand_b = numbers.pop(count_star)
            numbers.insert(count_star, float(operand_a) * float(operand_b))
        else:
            ops.pop(count_div)
            operand_a = numbers.pop(count_div)
            operand_b = numbers.pop(count_div)
            numbers.insert(count_div, float(operand_a) / float(operand_b))

    while "+" in ops or "-" in ops:
        count_plus = find_index(ops,"+")
        count_minus = find_index(ops, "-")
        if count_plus < count_minus:
            ops.pop(count_plus)
            operand_a = numbers.pop(count_plus)
            operand_b = numbers.pop(count_plus)
            numbers.insert(count_plus, float(operand_a) + float(operand_b))
        else:
            ops.pop(count_minus)
            operand_a = numbers.pop(count_minus)
            operand_b = numbers.pop(count_minus)
            numbers.insert(count_minus, float(operand_a) - float(operand_b))
    return float(numbers[0])

def find_index(l, op):
    for i in range(len(l)):
        if l[i] == op:
            return i
    return 10000

def with_para(exp):
    if "(" not in exp:
        return without_para(exp)
    else:
        exp = "".join(exp.split())
        start = exp.find("(")
        i = start + 1
        opener_count = 1
        while opener_count != 0:
            if exp[i] == ")":
                opener_count -=1
                i +=1
            elif exp[i] == "(":
                opener_count += 1
                i +=1
            else:
                i +=1
        a = with_para(exp[start+1:i-1])
        return with_para(exp[:start] + str(a) + exp[i:])

def calc(exp):
    return with_para(exp)


# TODO: Заметки
## Автор: Дуплей Максим Игоревич / Dupley Maxim Igorevich
## Дата: 02.12.2024
