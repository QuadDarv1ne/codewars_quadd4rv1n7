'''
[ Simpler Interactive interpreter (or REPL) ]

You will create an interpreter which takes inputs described below and produces outputs, storing state in between each input.
This is a simplified version of the Simple Interactive Interpreter kata with functions removed, so if you have fun with this kata, check out its big brother to add functions into the mix.
If you're not sure where to start with this kata, check out ankr's Evaluate Mathematical Expression kata.

Note that the eval command has been disabled.

Concepts:
The interpreter will take inputs in the language described under the language header below.
This section will give an overview of the language constructs.

Variables:
Any identifier which is not a keyword will be treated as a variable.
If the identifier is on the left hand side of an assignment operator, the result of the right hand side will be stored in the variable.
If a variable occurs as part of an expression, the value held in the variable will be substituted when the expression is evaluated.
Variables are implicitly declared the first time they are assigned to.

Example: Initializing a variable to a constant value and using the variable in another expression (Each line starting with a '>' indicates a separate call to the input method of the interpreter, other lines represent output)

>x = 7
     7
>x + 6
    13

Referencing a non-existent variable will cause the interpreter to throw an error.
The interpreter should be able to continue accepting input even after throwing.

Example: Referencing a non-existent variable

>y + 7 - ERROR: Invalid identifier. No variable with name 'y' was found."

Assignments:
An assignment is an expression that has an identifier on left side of an = operator, and any expression on the right.
Such expressions should store the value of the right hand side in the specified variable and return the result.

Example: Assigning a constant to a variable

x = 7
    7
In this kata, all tests will contain only a single assignment. You do not need to consider chained or nested assignments.

Operator Precedence:
Operator precedence will follow the common order.
There is a table in the Language section below that explicitly states the operators and their relative precedence.

Name conflicts:
Because variables are declared implicitly, no naming conflicts are possible.
variable assignment will always overwrite any existing value.

Input:
Input will conform to the expression production in the grammar below.

Output:
Output for a valid expression will be the result of the expression.
Output for input consisting entirely of whitespace will be an empty string (null in case of Java).

All other cases will throw an error.

Language - Grammar:
This section specifies the grammar for the interpreter language in EBNF syntax

expression      ::= factor | expression operator expression
factor          ::= number | identifier | assignment | '(' expression ')'
assignment      ::= identifier '=' expression

operator        ::= '+' | '-' | '*' | '/' | '%'

identifier      ::= letter | '_' { identifier-char }
identifier-char ::= '_' | letter | digit

number          ::= { digit } [ '.' digit { digit } ]

letter          ::= 'a' | 'b' | ... | 'y' | 'z' | 'A' | 'B' | ... | 'Y' | 'Z'
digit           ::= '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'

Operator Precedence:
The following table lists the language's operators grouped in order of precedence.
Operators within each group have equal precedence.

Category	    Operators
Multiplicative	*, /, %
Additive	    +, -
Assignment	    =
'''


import re

def without_para(exp):
    """
    Вычисляет значение выражения без использования скобок.

    Args:
        exp (str): Выражение, содержащее числа и операторы (+, -, *, /, %).

    Returns:
        float: Результат вычисления выражения.

    Пример:
        >>> without_para("3 + 5 * 2")
        13.0
    """
    numbers = []
    ops = []
    exp = "".join(exp.split())
    i = 0
    while i < len(exp):
        num = ""
        while i < len(exp) and exp[i] not in "+-*/%":
            num += exp[i]
            i += 1
        numbers.append(num)
        if i != len(exp):
            ops.append(exp[i])
            i += 1
    # Обработка двойных минусов
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
                numbers.insert(j, -float(a))
            else:
                numbers.insert(j, float(a))
        j += 1
    while "*" in ops or "/" in ops or "%" in ops:
        count_star = find_index(ops, "*")
        count_div = find_index(ops, "/")
        count_mod = find_index(ops, "%")
        if count_star < count_div and count_star < count_mod:
            ops.pop(count_star)
            operand_a = numbers.pop(count_star)
            operand_b = numbers.pop(count_star)
            numbers.insert(count_star, float(operand_a) * float(operand_b))
        elif count_div < count_star and count_div < count_mod:
            ops.pop(count_div)
            operand_a = numbers.pop(count_div)
            operand_b = numbers.pop(count_div)
            numbers.insert(count_div, float(operand_a) / float(operand_b))
        else:
            ops.pop(count_mod)
            operand_a = numbers.pop(count_mod)
            operand_b = numbers.pop(count_mod)
            numbers.insert(count_mod, float(operand_a) % float(operand_b))
    while "+" in ops or "-" in ops:
        count_plus = find_index(ops, "+")
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
    """
    Находит индекс первого вхождения оператора в списке.

    Args:
        l (list): Список операторов.
        op (str): Оператор, который нужно найти.

    Returns:
        int: Индекс оператора, либо 10000, если оператор не найден.

    Пример:
        >>> find_index(['+', '-', '*'], '*')
        2
    """
    for i in range(len(l)):
        if l[i] == op:
            return i
    return 10000


def with_para(exp):
    """
    Вычисляет значение выражения с учетом скобок.

    Args:
        exp (str): Выражение, содержащее числа, операторы и скобки.

    Returns:
        float: Результат вычисления выражения.

    Пример:
        >>> with_para("(3 + 5) * 2")
        16.0
    """
    if "(" not in exp:
        return without_para(exp)
    else:
        exp = "".join(exp.split())
        start = exp.find("(")
        i = start + 1
        opener_count = 1
        while opener_count != 0:
            if exp[i] == ")":
                opener_count -= 1
                i += 1
            elif exp[i] == "(":
                opener_count += 1
                i += 1
            else:
                i += 1
        a = with_para(exp[start + 1:i - 1])
        return with_para(exp[:start] + str(a) + exp[i:])


def tokenize(expression):
    """
    Токенизирует данное выражение в список токенов.
    """
    regex = re.compile(r"\s*(=>|[-+*/%=()]+|[A-Za-z_][A-Za-z0-9_]*|[0-9]*\.?[0-9]+)\s*")
    tokens = regex.findall(expression)
    return [s for s in tokens if not s.isspace()]

def calc(expression):
    """
    Вычисляет выражение без использования переменных и функций.
    """
    return eval(expression)

class Interpreter:
    def __init__(self):
        self.vars = {}
        self.functions = {}

    def input(self, expression):
        if expression.strip() == "":
            return ""

        tokens = tokenize(expression)

        try:
            if "=" in tokens:
                return self._handle_assignment(tokens)
            elif "fn" in tokens:
                return self._handle_function_definition(tokens)
            elif tokens[0] in self.vars:
                return self.vars[tokens[0]]
            else:
                return self._evaluate_expression(tokens)
        except Exception as e:
            return f"Error: {e}"

    def _handle_assignment(self, tokens):
        var_names = []
        i = 0
        while i < len(tokens):
            if tokens[i] == "=":
                var_names.append(tokens[i - 1])
            i += 1
        
        value_tokens = tokens[i + 1:]
        value = self._evaluate_expression(value_tokens)

        for var in var_names:
            self.vars[var] = value

        return value

    def _evaluate_expression(self, tokens):
        expression = []
        for token in tokens:
            if token in self.vars:
                expression.append(str(self.vars[token]))
            else:
                expression.append(token)

        try:
            return eval("".join(expression))
        except NameError as e:
            raise ValueError(f"Неопределенная переменная: {e}")
        except Exception as e:
            raise ValueError(f"Некорректное выражение: {e}")

    def _handle_function_definition(self, tokens):
        fn_name = tokens[1]
        if fn_name in self.vars:
            raise ValueError(f"Конфликт: переменная '{fn_name}' уже существует")

        args = []
        i = 2
        while tokens[i] != "=>":
            args.append(tokens[i])
            i += 1
        
        body = tokens[i + 1:]
        self.functions[fn_name] = (args, body)
        return None

    def _evaluate_function(self, fn_name, args):
        if fn_name not in self.functions:
            raise ValueError(f"Неопределенная функция: {fn_name}")

        fn_args, fn_body = self.functions[fn_name]

        if len(fn_args) != len(args):
            raise ValueError(f"Функция '{fn_name}' ожидает {len(fn_args)} аргументов, но получено {len(args)}")

        local_vars = dict(zip(fn_args, args))
        expression = "".join(fn_body)
        return eval(expression, {}, local_vars)


# TODO: Заметки
## Автор: Дуплей Максим Игоревич / Dupley Maxim Igorevich
## Дата: 02.12.2024
