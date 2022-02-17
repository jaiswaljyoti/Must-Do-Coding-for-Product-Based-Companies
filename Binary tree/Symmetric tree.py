#User function Template for python3

class Solution:
    # return true/false denoting whether the tree is Symmetric or not
    def isSame(self, root1, root2):
        if(root1==None and root2==None):
            return True
        if(root1==None or root2==None):
            return False
        if(root1.data!=root2.data):
            return False
        l = self.isSame(root1.left, root2.right)
        r = self.isSame(root1.left, root2.right)
        
        return l and r
        
    def isSymmetric(self, root):
        # Your Code Here
        if(root==None):
            return True
        ans = self.isSame(root.left, root.right)
        
        return ans