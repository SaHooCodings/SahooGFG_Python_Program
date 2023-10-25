class Solution:
    
    #Function to find the maximum occurring character in a string.
    def getMaxOccurringChar(self,s):
        
        #using hash table to store count of each character.
        occurences=[0 for i in range(256)]
        
        for char in s:
            occurences[ord(char)]+=1
            
        max_occurence=0
        character='~'
        
        #iterating over the hash table.
        for i in range(256):
            
            #we keep storing the maximum value in hash 
            #table and its corresponding character.
            if(occurences[i]>max_occurence):
                character=chr(i)
                max_occurence=occurences[i]
                
        #returning the character with maximum occurrences.
        return character
