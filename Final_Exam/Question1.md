```Python

def dirReduc(direction):
    final=[]
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




```
