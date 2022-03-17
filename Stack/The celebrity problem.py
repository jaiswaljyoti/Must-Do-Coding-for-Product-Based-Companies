#User function Template for python3

class Solution:
    
    #Function to find if there is a celebrity in the party or not.
    def celebrity(self, M, n):
        # code here 
        count=0
        l=[]
        for i,j in enumerate(M):
            if 1 in j:
                count+=1
            else:
                l.append(i)
        if count>0 and len(l)>0:
            return(l[0])
        return(-1)