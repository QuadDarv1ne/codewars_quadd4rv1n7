'''
[ Huffman Encoding ]

Motivation:
Natural language texts often have a very high frequency of certain letters, in German for example, almost every 5th letter is an E, but only every 500th is a Q.
It would then be clever to choose a very small representation for E.
This is exactly what the Huffman compression is about, choosing the length of the representation based on the frequencies of the symbol in the text.

Algorithm:
Let's assume we want to encode the word "aaaabcc", then we calculate the frequencies of the letters in the text:

Symbol	Frequency
  a	        4
  b	        1
  c	        2

Now we choose a smaller representation the more often it occurs, to minimize the overall space needed.

The algorithm uses a tree for encoding and decoding:
  .
 / \
a   .
   / \
   b  c

Usually we choose 0 for the left branch and 1 for the right branch (but it might also be swapped).
By traversing from the root to the symbol leaf, we want to encode, we get the matching representation.
To decode a sequence of binary digits into a symbol, we start from the root and just follow the path in the same way, until we reach a symbol.

Considering the above tree, we would encode a with 0, b with 10 and c with 11.
Therefore encoding "aaaabcc" will result in 0000101111.
(Note: As you can see the encoding is not optimal, since the code for b and c have same length, but that is topic of another data compression Kata.)

Tree construction:
To build the tree, we turn each symbol into a leaf and sort them by their frequency.
In every step, we remove 2 trees with the smallest frequency and put them under a node.
This node gets reinserted and has the sum of the frequencies of both trees as new frequency.
We are finished, when there is only 1 tree left.
(Hint: Maybe you can do it without sorting in every step ?)

Goal:
Write functions frequencies, encode and decode.
Bits are represented as strings of "0" (zero) and "1" (one).

Note: Frequency lists with just one or less elements should get rejected.
(Because then there is no information we could encode, but the length).
If you get a frequency list with one or less elements, return null/None/Nothing, depending on your language.
'''


def frequencies(s):
    """
    Вычисляет частоты символов в строке.

    Args:
        s (str): Входная строка.

    Returns:
        list: Список пар (символ, частота).

    Пример:
        >>> frequencies("aabbbc")
        [('a', 2), ('b', 3), ('c', 1)]
    """
    dct = {x: s.count(x) for x in s}
    return [(x, dct[x]) for x in dct]


def encode(freqs, s):
    """
    Кодирует строку с использованием алгоритма Хаффмана.

    Args:
        freqs (list): Список частот символов в формате [(символ, частота)].
        s (str): Входная строка.

    Returns:
        str: Закодированная строка в виде битовой строки, либо None, если частот меньше двух.

    Пример:
        >>> encode([('a', 2), ('b', 3), ('c', 1)], "aab")
        '0010'
    """
    my_freq = list(freqs)
    if len(my_freq) <= 1:
        return None
    tree_sim, res = get_tree(my_freq), ""
    for i in s:
        res += tree_sim[i]
    return res


def decode(freqs, bits):
    """
    Декодирует битовую строку обратно в текст с использованием алгоритма Хаффмана.

    Args:
        freqs (list): Список частот символов в формате [(символ, частота)].
        bits (str): Битовая строка для декодирования.

    Returns:
        str: Декодированная строка, либо None, если частот меньше двух.

    Пример:
        >>> decode([('a', 2), ('b', 3), ('c', 1)], '0010')
        'aab'
    """
    my_freq = list(freqs)
    if len(my_freq) <= 1:
        return None
    tree_sim = get_tree(my_freq)
    tree_sim = {tree_sim[x]: x for x in tree_sim}
    i, res = 0, ""
    while i < len(bits):
        char = ""
        while i < len(bits) and char not in tree_sim:
            char, i = char + bits[i], i + 1
        res += tree_sim[char]
    return res


def get_tree(my_freq):
    """
    Создает бинарное дерево кодирования Хаффмана и возвращает словарь кодов.

    Args:
        my_freq (list): Список частот символов в формате [(символ, частота)].

    Returns:
        dict: Словарь кодов символов, где ключ — символ, значение — его код.

    Пример:
        >>> get_tree([('a', 2), ('b', 3), ('c', 1)])
        {'c': '00', 'a': '01', 'b': '1'}
    """
    tree_sim = {}
    while len(my_freq) > 1:
        my_freq.sort(key=lambda x: x[1], reverse=True)
        a, b = my_freq.pop(), my_freq.pop()
        s_a, s_b = a[0], b[0]
        my_freq.append((s_a + s_b, a[1] + b[1]))
        for i in s_a:
            tree_sim[i] = "0" + tree_sim.get(i, "")
        for j in s_b:
            tree_sim[j] = "1" + tree_sim.get(j, "")
    return tree_sim


# TODO: Заметки
## Автор: Дуплей Максим Игоревич / Dupley Maxim Igorevich
## Дата: 02.12.2024
