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

# Part B:
def remove_all(el, lst):
    """
    Removes all instances of el from lst.
    Given: x = [3, 1, 2, 1, 5, 1, 1, 7]
    Usage: remove_all(1, x)
    Would result in: [3, 2, 5, 7]
    """
    i = 0
    number = len(lst)
    while i<number:
      if lst[i]==el:
        lst.remove(lst[i])
        i=i-1
        number=number-1
      i = i+1

# Part C:
def add_this_many(x, y, lst):
  """ Adds y to the end of lst the number of times x occurs in lst. 
  Given: lst = [1, 2, 4, 2, 1]
  Usage: add_this_many(1, 5, lst)
  Results in: [1, 2, 4, 2, 1, 5, 5]
  """
  for i in range(len(lst)):
    if lst[i] == x:
      lst.append(y)
      
"""
Part D:
a: [3,1,4,2]
b: [3, 1, 4, 2, 5, 3]
c: [1, 2, 3]
d: [3, 1, 4, 2, 5, 3]
e: []
f: [1, 4, 2]
g: [3, 5, 2, 4, 1, 3]
"""

# Part E:
def reverse(lst):
  """ Reverses lst in place. 
  Given: x = [3, 2, 4, 5, 1] 
  Usage: reverse(x)
  Results: [1, 5, 4, 2, 3]
  """  
  for i in range(len(lst)):
   c=lst.pop()
   lst.insert(i,c)

# Part F:
def rotate(lst, k):
  """ Return a new list, with the same elements of lst, rotated to the right k.
  Given: x = [1, 2, 3, 4, 5]
  Usage: rotate(x, 3)
  Results: [3, 4, 5, 1, 2]
  """
  for i in range(k):
    c=lst.pop()
    lst.insert(0,c)

"""
Part H:
a: False
b: 4
c: False
d: {('eli manning', 'giants'): 2, 'joe montana': 4, 'peyton manning': 1, 'tom brady': 3, 'joe flacco': 1}
e: {('eli manning', 'giants'): 2, 'tom brady': 3, 3: 'cat', 'peyton manning': 1, 'joe montana': 4, 'joe flacco': 1}
f: {('eli manning', 'giants'): 5, 'tom brady': 3, 3: 'cat', 'peyton manning': 1, 'joe montana': 4, 'joe flacco': 1}
g:{('eli manning', 'giants'): 5, 'tom brady': 3, 3: 'cat', ('steelers', '49ers'): 11, 'peyton manning': 1, 'joe montana': 4, 'joe flacco': 1}
"""

#Part I:
def replace_all(d, x, y):
  """Replaces all values of x with y. 
  Given: d = {1: {2:3, 3:4}, 2:{4:4, 5:3}} 
  Usage: replace_all(d,3,1)
  Results: {1: {2: 1, 3: 4}, 2: {4: 4, 5: 1}} 
  """
  for key,val in d.items():
    if type(val)==type(dict()):
      replace_all(val, x, y)
    else:
      if val==x:
        d[key]=y

  
#Part J:
def rm(d, x):
  """Removes all pairs with value x. 
  Given:  d = {1:2, 2:3, 3:2, 4:3}
  Usage:  rm(d,2)
  Results: {2:3, 4:3}
  """
  delete=dict()
  for key,val in d.items():
    if val == x:
      delete[key]=val
  for key,val in delete.items():
    del d[key]
