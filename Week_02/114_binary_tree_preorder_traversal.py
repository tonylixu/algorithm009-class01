# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class SolutionOne:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        return self.helper(root, res)

    def helper(self, root, res):
        if not root:
            return []
        res.append(root.val)
        if root.left:
            self.helper(root.left, res)
        if root.right:
            self.helper(root.right, res)
        return res


class SolutionTwo:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        curr = root
        while stack or curr:
            while curr:
                res.append(curr.val)
                stack.append(curr)
                curr = curr.left
            top = stack.pop()
            curr = top.right
        return res


class SolutionThree:
    """Status lopp solution"""
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        NEW, VISITED = 0, 1
        res = []
        stack = [(NEW, root)]
        while stack:
            status, node = stack.pop()
            if not node: continue
            if status == NEW:
                stack.append((NEW, node.right))
                stack.append((NEW, node.left))
                stack.append((VISITED, node))
            if status == VISITED:
                res.append(node.val)
        return res