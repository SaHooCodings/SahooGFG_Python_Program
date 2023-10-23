def pair_sum(dict, N, arr, sum):
    
    # Your code here
    # Hint: You can use 'in' to find if any key is in dict
    for i in arr:
        if (sum-i) in dict:
            if(sum-i == i):
                if(dict[i] > 1):
                    return True
            else:
                return True
    return False
