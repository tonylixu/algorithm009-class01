# Good tutorial:
# https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/solution/xiong-mao-shua-ti-python3-xian-xu-zhao-gen-hua-fen/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        Time complexity: O(N)
        Space complexity: O(N)
        """
        if not preorder or not inorder:
            return None
        # Construct root node
        root = TreeNode(preorder[0])
        # For preorder:
        # left subtree: [1 : 1+idx]
        # right subtree: [1+idx : ]
        # For inorder:
        # left subtree: [:idx] right subtree: [idx+1:]
        idx = inorder.index(root.val)
        # Construct left sub tree
        root.left = self.buildTree(preorder[1:1+idx], inorder[:idx])
        root.right = self.buildTree(preorder[1+idx:], inorder[idx+1:])
        return root

# Improved version
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        Time complexity: O(N)
        Space complexity: O(N)
        """
        if inorder:
            idx = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[idx])
            # Construct left sub tree
            root.left = self.buildTree(preorder, inorder[:idx])
            root.right = self.buildTree(preorder, inorder[idx+1:])
            return root