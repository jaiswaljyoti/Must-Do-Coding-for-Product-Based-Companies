#User function Template for python3
class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr, n):
		# code here
        max_overall = arr[0]
        max_ending, min_ending = arr[0], arr[0]
        
        for i in range(1, n):
            tmp = max_ending
            max_ending = max({arr[i], arr[i]*max_ending, arr[i]*min_ending})
            min_ending = min({arr[i], arr[i]*tmp, arr[i]*min_ending})
            max_overall = max(max_overall, max_ending)
        
        return max_overall