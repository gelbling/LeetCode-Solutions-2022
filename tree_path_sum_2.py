# LeetCode 113

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root, targetSum: int):
        
        totalSum = 0
        currPath = []
        totalPaths = []
        
        self.helperFindPath(root, totalSum, targetSum, currPath, totalPaths)
        
        return totalPaths
        
    def helperFindPath(self, node, totalSum, targetSum, currPath, totalPaths):
        
        if not node:
            return
        
        totalSum += node.val
        currPath.append(node.val)
        
        if not node.left and not node.right and totalSum == targetSum:
            totalPaths.append(currPath.copy())
            currPath.pop()
            return
        elif not node.left and not node.right:
            currPath.pop()
            return
        
        if node.left:
            self.helperFindPath(node.left, totalSum, targetSum, currPath, totalPaths)
        if node.right:
            self.helperFindPath(node.right, totalSum, targetSum, currPath, totalPaths)   
        
        currPath.pop()        
        