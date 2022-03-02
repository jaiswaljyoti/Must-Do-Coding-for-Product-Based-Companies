#User function Template for python3

class Solution:
    def solve(self, a, n, k):
        ans = 0
        for i in range(n):
            x = a[i]
            low = i+1
            high = n-1
            while(low<high):
                s = x+a[low]+a[high]
                if(s>k):
                    high-=1
                else:
                    ans+=high-low
                    low+=1
        return ans
        
    def countTriplets(self, Arr, N, L, R):
        # code here
        Arr.sort()
        return self.solve(Arr, N, R)-self.solve(Arr,N,L-1)