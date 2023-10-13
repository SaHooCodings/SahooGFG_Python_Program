def insert_dict(query, dict):
    
    # Your code here
    dict[query[1]] = query[2]
    
# deleting from dictionary
def del_dict(query, dict):
    
    # Your code here
    if(dict[query[1]]):
        del dict[query[1]]
        return True
    return False

# print marks of required name
def print_dict(key, dict):
    
    # Your code here
    if key in dict:
       print("Marks of {} is {}".format(key, dict[key]))
       return True
    else:
        return False
