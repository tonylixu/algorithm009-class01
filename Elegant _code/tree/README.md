## Binary Tree

### Binary Tree Preorder Traversal
* [Leetcode link](https://leetcode.com/problems/binary-tree-preorder-traversal/)
* TreeNode definition:
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
```

* Recursive method
  * Time complexity: O(N)
  * Space complexity: O(N)
```python
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
        # res.append(root.val) --> InOrder
        if root.right:
            self.helper(root.right, res)
        # res.append(root.val) --> PostOrder
        return res
```

* Iterative method
  * Time complexity: O(N)
  * Space complexity: O(N)
```python
class SolutionTwo:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        NEW, VISITED = 0, 1
        res = []
        stack = [(NEW, root)]
        while stack:
            status, node = stack.pop()
            if not node: continue
            if status == NEW:
                # stack.append((VISITED, node)) --> PostOrder
                stack.append((NEW, node.right))
                # stack.append((VISITED, node)) --> InOrder
                stack.append((NEW, node.left))
                stack.append((VISITED, node))
            if status == VISITED:
                res.append(node.val)
        return res
```