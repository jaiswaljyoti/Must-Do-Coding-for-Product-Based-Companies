class Solution:

	def findMaximum(self,arr, n):
		# code here
		low=0
		high=n-1
		mid = low+(high-low)//2
        while(low<high):
            
            if(arr[mid+1]>arr[mid]):
                low=mid+1
           
            else:
                high=mid
            mid = low+(high-low)//2
            
        return arr[mid]