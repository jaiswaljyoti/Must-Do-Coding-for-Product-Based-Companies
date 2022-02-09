class Solution:
    #Function to count the number of possible triangles.
    def findNumberOfTriangles(self, arr, n):
        #code here
        arr.sort()
        count = 0
        for i in range(n-1,1,-1):
            l = 0
            r = i-1
           
            while(l < r):
                if(arr[l] + arr[r] > arr[i]):
                    count+=r-l
                    r-=1
                else:
                    l+=1
                
        return count