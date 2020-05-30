# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # Return 0 when tree is empth
        if root is None:
            return 0
        # max depth of root.left and root.right
        left_max = self.maxDepth(root.left)
        right_max = self.maxDepth(root.right)
        # Return the max left/right depth + 1
        return max(left_max, right_max) + 1