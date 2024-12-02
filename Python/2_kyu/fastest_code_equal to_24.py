'''
[ Fastest Code : Equal to 24 ]

This is the Performance version of simple version.
If your code runs more than 7000ms, please optimize your code or try the simple version.

Task:
A game I played when I was young: Draw 4 cards from playing cards, use + - * / and () to make the final results equal to 24.
You will coding in function equalTo24. Function accept 4 parameters a b c d(4 numbers), value range is 1-100.
The result is a string such as "2*2*2*3" ,(4+2)*(5-1);
If it is not possible to calculate the 24, please return "It's not possible"
All four cards are to be used, only use three or two cards are incorrect;
Use a card twice or more is incorrect too.

You just need to return one correct solution, don't need to find out all the possibilities.

The different between "challenge version" and "simple version":
1) a,b,c,d range:  In "challenge version" it is 1-100, 
                   In "simple version" it is 1-13.
2) "challenge version" has 1000 random testcases,
   "simple version" only has 20 random testcases.

Some examples:
equalTo24(1,2,3,4) //can return "(1+3)*(2+4)" or "1*2*3*4"
equalTo24(2,3,4,5) //can return "(5+3-2)*4" or "(3+4+5)*2"
equalTo24(3,4,5,6) //can return "(3-4+5)*6"
equalTo24(1,1,1,1) //should return "It's not possible"
equalTo24(13,13,13,13) //should return "It's not possible"
'''


from itertools import permutations, combinations_with_replacement, chain
import time
import random


def apply_ops(ops, nums):
    i, j, k = ops
    a, b, c, d = [float(n) for n in nums]
    A, B, C, D = nums
    opmap = {'+': float.__add__,
             '-': float.__sub__,
             '*': float.__mul__,
             '/': float.__truediv__}
    strf = (A, i, B, j, C, k, D)

    try:
        if opmap[j](opmap[i](a, b), opmap[k](c, d)) == 24:
            return "({}{}{}){}({}{}{})".format(*strf)
    except ZeroDivisionError:
        pass
    try:
        if opmap[k](opmap[j](opmap[i](a, b), c), d) == 24:
            return "(({}{}{}){}{}){}{}".format(*strf)
    except ZeroDivisionError:
        pass
    try:
        if opmap[k](opmap[i](a, opmap[j](b, c)), d) == 24:
            return "({}{}({}{}{})){}{}".format(*strf)
    except ZeroDivisionError:
        pass
    try:
        if opmap[i](a, opmap[k](opmap[j](b, c), d)) == 24:
            return "{}{}(({}{}{}){}{})".format(*strf)
    except ZeroDivisionError:
        pass
    try:
        if opmap[i](a, opmap[j](b, opmap[k](c, d))) == 24:
            return "{}{}({}{}({}{}{}))".format(*strf)
    except ZeroDivisionError:
        pass


def permute_ops(ops='+-*/'):
    y = [permutations(x) for x in combinations_with_replacement(ops, 3)]
    return chain.from_iterable(y)


op_perms = set(permute_ops())


def equal_to_24(*case):
    case_perms = permutations(case)
    for case_i in case_perms:
        for op in op_perms:
            result = apply_ops(op, case_i)
            if result:
                return result
    return "It's not possible!"


random.seed(42)
if __name__ == "__main__":
    # Set up test tuples:
    #   17,160 as the complete set of permutations for 4 playing cards
    #   5,000 random ints
    z = permutations(range(1, 14), 4)
    zl = list(z)
    rl = [(random.randint(1, 100),
           random.randint(1, 100),
           random.randint(1, 100),
           random.randint(1, 100))
          for ri in range(5000)]

    results_52 = {}
    start = time.time()
    for zi in zl:
        results_52[zi] = equal_to_24(*zi)

    results_rand = {}
    for ri in rl:
        results_rand[ri] = equal_to_24(*ri)

    performance = time.time() - start
    print(performance)


# TODO: Заметки
## Автор: Дуплей Максим Игоревич / Dupley Maxim Igorevich
## Дата: 30.11.2024
