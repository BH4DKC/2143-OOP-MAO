```Python

def dirReduc(direction):
    """
    @Function: dirReduc
    @Description:
        Reduce unnesseary information with a given list of directions
    @Returns: string with the reduced direction
    """
    final=[] # intial list of final direction
    for i in direction:
        if i == 'NORTH':
            if 'SOUTH' not in final:
                final.append(i)
            else:
                final.remove('SOUTH')
        if i == 'SOUTH':
            if 'NORTH' not in final:
                final.append(i)
            else:
                final.remove('NORTH')
        if i == 'EAST':
            if 'WEST' not in final:
                final.append(i)
            else:
                final.remove('WEST')
        if i == 'WEST':
            if 'EAST' not in final:
                final.append(i)
            else:
                final.remove('EAST')
    return final


print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH"]))


```
