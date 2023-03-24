# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root):
        
        nodes = []
        
        q = []
        q.append(root)
        
        while q:
            level = []
            for i in range(len(q)):
                node = q.pop(0)
                if node:
                    level.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            
            if level:
                nodes.append(level)
                    
        return nodes
            