#User function Template for python3


'''class Node: 
    # Constructor to create a new Node 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None'''


#Function to check whether a binary tree is balanced or not.
class Solution:
    isBalanaced = 1
    def height(self,root):
        if root == None :
            return 0
        lh = self.height(root.left)
        rh = self.height(root.right)
        if abs(lh-rh) > 1 :
            self.isBalanced = 0
        return max(lh,rh) + 1
    
    def isBalanced(self,root):
    
        #add code here
        self.height(root)
        return self.isBalanced