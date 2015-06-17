from lab04 import *

# Q9
def reverse_iter(lst):
    """Returns the reverse of the given list.

    >>> reverse_iter([1, 2, 3, 4])
    [4, 3, 2, 1]
    """
    "*** YOUR CODE HERE ***"
    r = []
    for i in lst:
        r = [i] + r 
    return r

# Q10
def mergesort(seq):
    """Mergesort algorithm.

    >>> mergesort([4, 2, 5, 2, 1])
    [1, 2, 2, 4, 5]
    >>> mergesort([])     # sorting an empty list
    []
    >>> mergesort([1])   # sorting a one-element list
    [1]
    """
    "*** YOUR CODE HERE ***"
    l1 = len(seq)//2
    if l1 == 0:
        return seq
    l2 = len(seq)-l1

    l11 = seq[0:l1]
    l12 = seq[l2-1:len(seq)]

    for i in range(0,l1):
        for j in range(i+1,l1):
            if l11[i] > l11[j]:
                t = l11[i]
                l11[i] = l11[j]
                l11[j] = t
    for i in range(0,l2):
        for j in range(i+1,l2):
            if l12[i] > l12[j]:
                t = l12[i]
                l12[i] = l12[j]
                l12[j] = t
    l = merge(l11,l12)
    return l

# Q11
def coords(fn, seq, lower, upper):
    """
    >>> seq = [-4, -2, 0, 1, 3]
    >>> fn = lambda x: x**2
    >>> coords(fn, seq, 1, 9)
    [[-2, 4], [1, 1], [3, 9]]
    """ 
    "*** YOUR CODE HERE **S*"
    return [[i,fn(i)] for i in seq if fn(i) <=upper and fn(i) >= lower]

# Q12
def deck(suits, numbers):
    """Creates a deck of cards (a list of 2-element lists) with the given
    suits and numbers. Each element in the returned list should be of the form
    [suit, number].

    >>> deck(['S', 'C'], [1, 2, 3])
    [['S', 1], ['S', 2], ['S', 3], ['C', 1], ['C', 2], ['C', 3]]
    >>> deck(['S', 'C'], [3, 2, 1])
    [['S', 3], ['S', 2], ['S', 1], ['C', 3], ['C', 2], ['C', 1]]
    >>> deck([], [3, 2, 1])
    []
    >>> deck(['S', 'C'], [])
    []
    """
    "*** YOUR CODE HERE ***" 
    d = []
    for i in suits:
        for j in numbers:
            d = d + [[i,j]]
    return d


# Q13
def add_matrices(x, y):
    """
    >>> matrix1 = [[1, 3],
    ...            [2, 0]]
    >>> matrix2 = [[-3, 0],
    ...            [1, 2]]
    >>> add_matrices(matrix1, matrix2)
    [[-2, 3], [3, 2]]
    """
    "*** YOUR CODE HERE ***"
    return [[i[0]+j[0],i[1]+j[1]] for i in x 
                                    for j in y ] 

