'''
[ Counting sheep ]

Consider an array/list of sheep where some sheep may be missing from their place.
We need a function that counts the number of sheep present in the array (true means present).

For example:
[True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]

The correct answer would be 17.

Hint: Don't forget to check for bad values like null/undefined.
'''


def count_sheeps(sheep):
    # Фильтруем все значения, которые не являются True или False
    return sum(1 for s in sheep if isinstance(s, bool) and s)


# TODO: Заметки
## Автор: Дуплей Максим Игоревич / Dupley Maxim Igorevich
## Дата: 30.11.2024
