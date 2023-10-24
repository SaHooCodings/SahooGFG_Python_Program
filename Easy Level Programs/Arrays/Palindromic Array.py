def PalinArray(arr ,n):
    # Code here
    for i in arr:
        if str(i) != str(i)[::-1]:
            return False
    return True
