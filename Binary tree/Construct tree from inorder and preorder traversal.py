#User function Template for python3

'''
# Node class

class Node:
    def __init__(self,val):
        self.data = val
        self.right = None
        self.left = None

'''

class Solution:
    def buildtree(self, inorder, preorder, n):
        # code here
        # build tree and return root node
        if not inorder or not preorder:
            return None
        root = Node(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildtree(inorder[:mid], preorder[1:mid+1], mid)
        root.right = self.buildtree(inorder[mid+1:], preorder[mid+1:], n-mid)
        
        return root