def isBinary(str):
    #code here
    for char in str:
        if char != '0' and char != '1':
            return 0
    return 1
