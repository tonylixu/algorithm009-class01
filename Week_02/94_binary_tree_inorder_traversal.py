# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class SolutionOne:
    """Recursive traverse"""
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        return self.helper(root, result)

    def helper(self, root, result):
        if not root:
            return []
        if root.left:
            self.helper(root.left, result)
        result.append(root.val)
        if root.right:
            self.helper(root.right, result)
        return result


class SolutionTwo:
    """Loop traverse"""
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []    # To store result
        stack = []  # Stack to keep root node
        curr = root # Current node
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left   # Traverse to left till the leaf
            top = stack.pop()
            res.append(top.val)
            curr = top.right       # Move on to the right node

