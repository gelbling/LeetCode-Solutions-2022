# LeetCode 112

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
        
        totalSum = 0
        
        return self.helperDFS(root,totalSum,targetSum)
        
    def helperDFS(self, node, totalSum, targetSum):
        
        if not node:
            return False
        
        totalSum += node.val
        
        if not node.right and not node.left and totalSum == targetSum:
            return True
        
        return self.helperDFS(node.left,totalSum,targetSum) or self.helperDFS(node.right,totalSum,targetSum)