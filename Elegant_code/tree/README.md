## Binary Tree

### Binary Tree Preorder Traversal
* [PreOrder](https://leetcode.com/problems/binary-tree-preorder-traversal/)
* [InOrder](https://leetcode.com/problems/binary-tree-inorder-traversal/)
* [PostOrder](https://leetcode.com/problems/binary-tree-postorder-traversal/)
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

### N-ary Tree Preorder Traversal
* [PreOrder](https://leetcode.com/problems/n-ary-tree-preorder-traversal/)
* [PostOrder](https://leetcode.com/problems/n-ary-tree-postorder-traversal/)
* TreeNode definition:
```python
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
```

* Recursive method
  * Time complexity: O(N)
  * Space complexity: O(2M) = O(M)
```python
class SolutionOne:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return None
        result = []
        result.append(root.val)
        for rem in root.children:
            result += self.preorder(rem)
        # result.append(root.val) --> PostOrder
        return result
```

* Iterative method
  * Time complexity: O(M), M is the number of nodes in N-ary tree.
  * Space complexity: O(M), worst case, there are only two levels in N-ary
  tree, when we pop the root out, we need to push all the M-1 nodes in.
```python
class SolutionTwo:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return None
        result = []
        nodes_stack = [root]
        while nodes_stack:
            node = nodes_stack.pop()
            result.append(node.val)
            nodes_stack += [child for child in node.children[::-1] if child]
        return result
        # return result[::-1] --> PostOrder
```

### Notes:
* [Good solution](https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/solution/yi-tao-quan-fa-shua-diao-nge-bian-li-shu-de-wen--3/)