class Solution:
    def relationalOperators(self, A, B):
        # code here
        if A < B:
            print(str(A)+ " is less than " +str(B))
        elif A > B:
            print(str(A)+ " is greater than " +str(B))
        else:
            print(str(A)+ " is equal to " +str(B))
