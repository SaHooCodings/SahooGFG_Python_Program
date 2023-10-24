def minAnd2ndMin( a, n):
    #code here
    # O(N) just 2 pointers and traversing the list
    min_ele = min(a)
    second_min_ele = max(a)
    for i in range(n):
        if a[i]<second_min_ele and a[i]>min_ele:
            second_min_ele = a[i]
    if min_ele!=second_min_ele:
        return [min_ele,second_min_ele]
    return [-1,-1]
