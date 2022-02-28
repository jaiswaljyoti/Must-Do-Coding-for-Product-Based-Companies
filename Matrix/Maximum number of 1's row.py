#User function Template for python3

class Solution:
    def maxOnes (self, Mat, N, M):
        # code here
        maxOne = 0
        row = 0
        for i in range(N):
            l = 0
            r = M-1
            while(l<=r):
                m = (l+r)//2
                if(Mat[i][m]==1):
                    r = m-1
                else:
                    l = m+1
            ones = M-r-1
            if(ones>maxOne):
                maxOne = ones
                row = i
                
        return row