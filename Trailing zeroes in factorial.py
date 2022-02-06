#User function Template for python3

class Solution:
    def trailingZeroes(self, N):
    	#code here 
        zero=0
        i = 5
        while(i<=N):
            zero+=N//i
            i = i*5
        return zero