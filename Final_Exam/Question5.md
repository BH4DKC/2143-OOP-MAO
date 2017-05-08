```python
def findBreak(sequence):
  """
  @Function: findBreak
  @Description: find the first number that is not consecutive with in the list
  @Returns: the first number that is not consecutive, if there is one. If not, return 'None'
  """
  x=sequence[0]      #set compare variable
  for i in sequence:
    if i == x:       #check consecutivity
      x += 1         #set expected value for the next number
    else:
      return(i)      # return inconsecutive number
      
  return 'None'

print(findBreak([1,2,3,4,5]))
```
