#User function Template for python3

# class Node:
#     def __init__(self, val):
#         self.data = val
#         self.left = None
#         self.right = None

# return the Kth largest element in the given BST rooted at 'root'
class Solution:
    def kthLargest(self,root, k):
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.right
            root = stack.pop()
            k-=1
            if k==0:
                return root.data
            root = root.left