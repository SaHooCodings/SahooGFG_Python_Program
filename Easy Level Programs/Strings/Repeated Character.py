class Solution:
    def firstRep(self, s):
        # creating an empty dictionary to store the frequency of each character
        dicti={}

        # iterating over the string
        for i in s:
            # checking if the character is already present in the dictionary
            if i in dicti:
                # if yes, increment its frequency by 1
                dicti[i]+=1
            else:
                # if not, add the character to the dictionary with frequency 1
                dicti[i]=1

        # iterating over the string again
        for i in s:
            # checking if the frequency of the character is greater than 1
            if dicti[i]>1:
                # if yes, return the character
                return i
          
        # if no repeated characters found, return -1
        return -1
