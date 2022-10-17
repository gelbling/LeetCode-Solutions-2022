# LeetCode 572

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root, subRoot) -> bool:
            
        if not subRoot:
            return True
        
        if not root:
            return False
        
        if self.matchTree(root, subRoot):
            return True
        
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
        
    def matchTree(self, node1, node2):

        if not node1 and not node2:
            return True

        if node1 and node2 and node1.val == node2.val:
            return (self.matchTree(node1.left,node2.left) and self.matchTree(node1.right,node2.right))
        else:
            return False