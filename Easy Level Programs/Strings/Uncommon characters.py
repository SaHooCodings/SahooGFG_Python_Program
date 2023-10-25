class Solution:

    #Function to find uncommon characters between two strings.
    def UncommonChars(self,A, B):
        res = ''

        #creating a list to keep track of presence of characters.
        present = [0] * 26

        #iterating over first string and marking presence of each character.
        for e in A:
            present[ord(e) - ord('a')] = 1

        #iterating over second string and updating presence list accordingly.
        for e in B:
            if present[ord(e) - ord('a')] == 1 or present[ord(e) - ord('a')] ==-1:
                present[ord(e) - ord('a')] = -1  
            else:
                present[ord(e) - ord('a')] = 2

        res = ''

        #iterating over the presence list to get the uncommon characters.
        for i, e in enumerate(present):
            if e == 1 or e==2:
                res += chr(i + ord('a'))
                
        #returning the result.
        if res:
            return res
        else:
            return -1
