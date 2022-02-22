#User function Template for python3

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    def minDepth(self, root):
        #Code here
        if not root:
            return  0
        leftLevel = self.minDepth(root.left)
        rightLevel = self.minDepth(root.right)
        if(root.left and root.right):
            return 1+min(leftLevel, rightLevel)
        elif(root.left):
            return 1+leftLevel
        else:
            return 1+rightLevel