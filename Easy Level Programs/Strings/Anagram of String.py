def remAnagram(str1,str2):
    temp = [0]*26
    for each in str1:
        temp[ord(each)-ord('a')]+=1
    for each in str2:
        temp[ord(each)-ord('a')]-=1
    res = 0
    for each in temp:
        res+=abs(each)
    return res
