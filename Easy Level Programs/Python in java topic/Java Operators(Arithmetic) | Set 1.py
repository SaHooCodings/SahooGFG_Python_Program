import math
class Solution:
	def FindRoots(self, A, B, C):
		# Code here
        r = (B*B)-4*A*C
        if r<0:
            return [-1.0]
        r = math.sqrt(r)
        x = (-B+r)/(2*A)
        y = (-B-r)/(2*A)
        
        if x>y:
            x,y = y,x
        return [x,y]
