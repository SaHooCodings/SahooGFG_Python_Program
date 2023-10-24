from collections import defaultdict

#Function to check if a1 is a subset of a2.
def isSubset( a1, a2, n, m):
    #creating two dictionaries to store the frequency of each element in a1 and a2.
    dic1 = defaultdict(lambda:0)
    dic2 = defaultdict(lambda:0)
    
    #iterating over a1 and updating the frequency in dic1.
    for i in a1:
        dic1[i] += 1
    
    #iterating over a2 and updating the frequency in dic2.
    for i in a2:
        dic2[i] += 1
    
    #iterating over dic2 and checking if the frequency of each element in dic1 is greater or equal to dic2.
    #If not, then a1 is not a subset of a2, so return "No".
    for i in dic2:
        if dic1[i] < dic2[i]:
            return "No"
    
    #If all elements in dic2 have a frequency less than or equal to that in dic1, then a1 is a subset of a2, so return "Yes".
    return "Yes"
