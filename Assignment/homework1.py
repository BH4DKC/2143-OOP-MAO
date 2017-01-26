"""
Name: Zhiqi Mao
Email: zhiqimao@qq.com
Assignment: Homework 1 - Lists and Dictionaries
Due: 31 Jan @ 11:00 a.m.
"""

"""
Part A:
a: 1 3
b: [1,5,4,2,6]
c: 5
d: True
e: [1,[5,1],4,2,6]
"""

## Part B:
def remove_all(el, lst):
    """
    Removes all instances of el from lst.
    Given: x = [3, 1, 2, 1, 5, 1, 1, 7]
    Usage: remove_all(1, x)
    Would result in: [3, 2, 5, 7]
    """
    for i in range(len(lst)):
        if lst[i] == el:
            lst.remove(lst[i])
