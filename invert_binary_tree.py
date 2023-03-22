# LeetCode 226


# Time Complexity: O(n)
# Space ''       : O(1)
class Solution:
    def invertTree(self, root):

        # base case
        if not root:
            return

        # swap children
        rightTree = root.right
        root.right = root.left
        root.left = rightTree

        # hit all nodes
        self.invertTree(root.right)
        self.invertTree(root.left)

        return root
