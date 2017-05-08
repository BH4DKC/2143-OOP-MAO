def checkDup(word):
    """
    @Function: checkDup
    @Description:
        check duplicates in a string, case-insensitive
    @Returns: no return, but outputs the number of character repeated and what they are.
    """
    word_list=list(str.lower(word)) #Since case-insensetive, lower every letter first, then convert to list
    letter=[]
    duplicate=[]
    for i in word_list:
        if i not in letter: # check if repeated
            letter.append(i)
        elif i not in duplicate: # if it is , add in duplicate list
            duplicate.append(i)
    if len(duplicate) == 0:
        print('No characters repeats more than once')
    else:
        print(len(duplicate), ' # repeat more than once, they are: ',duplicate)

    return
