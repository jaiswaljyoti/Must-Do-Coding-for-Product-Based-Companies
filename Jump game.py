class Solution:
    def canReach(self, A, N):
        # code here 
        jump = A[0]
        for i in range(N):
            if(jump>=i):
                jump = max(jump,i+A[i])
                
        if(jump>=N-1):
            return 1
        else:
            return 0