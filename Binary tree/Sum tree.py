'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
# your task is to complete this function
# function should return True is Tree is SumTree else return False
class Solution:
    f = 1
    def solve(self, root):
        if(self.f==0 or root is None):
            return 0
        if(root.left==None and root.right==None):
            return root.data
        a = self.solve(root.left)
        b = self.solve(root.right)
        if(a+b!=root.data):
            self.f = 0
        return a+b+root.data
            
    def isSumTree(self,root):
        # Code here
        self.solve(root)
            
        return self.f