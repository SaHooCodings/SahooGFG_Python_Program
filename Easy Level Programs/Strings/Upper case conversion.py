class Solution:
    def transform(self, s):
        # code here
        strp = s.split(" ")
        strngs = ""
        for i in range(len(strp)):
            strngs += strp[i][0].upper()
            strngs += strp[i][1:]
            strngs += " "
        return strngs
