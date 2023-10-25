class Solution:
    
    #Function to split the given string into alphabets, numbers, and special characters.
    def splitString(ob, S): 
        result = [] 
        alpha = "" 
        num = "" 
        special = "" 
        
        #iterating over the string character by character.
        for i in range(len(S)): 
            #if character is an alphabet, add it to alpha.
            if((S[i] >= 'A' and S[i] <= 'Z') or
                (S[i] >= 'a' and S[i] <= 'z')): 
                alpha += S[i] 
            
            #if character is a digit, add it to num.
            elif (S[i].isdigit()): 
                num = num+ S[i] 
            
            #if character is a special character, add it to special.
            else: 
                special += S[i] 

        #appending alpha, num, and special to the result list.
        result.append(alpha) 
        result.append(num ) 
        result.append(special) 
        return result
