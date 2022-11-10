# LeetCode 94


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root):
        
        if not root:
            return []
        
        inOrder = []
        self.inOrderTraversal(root,inOrder)
        
        return inOrder
    
    def inOrderTraversal(self, node, inOrder):
        
        if not node:
            return
        
        self.inOrderTraversal(node.left, inOrder)
        inOrder.append(node.val)
        self.inOrderTraversal(node.right, inOrder)