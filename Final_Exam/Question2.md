```python
def tickets(given):
    """
        @Function: tickets
        @Description:
            with a given list of number of money paid, determine if there is enough change to give to the customer
            after purchasing a 25 dollar tickets
        @Returns: string 'Yes' or 'No' indicates if enough change can be give back
        """
    twentyfive = 0 # initial bill counts
    fifty = 0
    for i in given:
        if i == 50: # Stocking bills as cashier recieves money
            fifty += 1
        elif i == 25:
            twentyfive += 1
        change = i-25
        while change >= 50 and fifty > 0: # give 50 dollar change back first
            change -= 50
            fifty -= 1
        while change >= 25 and twentyfive > 0: # then give 25 dollar change
            change -= 25
            twentyfive -= 1
        if change != 0: # if money left over at the end, then returns "No' string for not able to give change back
            return('NO')
    return ('YES')

```
