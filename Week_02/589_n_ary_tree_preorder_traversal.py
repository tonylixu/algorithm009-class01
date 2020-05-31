"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class SolutionOne:
    def preorder(self, root: 'Node') -> List[int]:
        # Recursive method
        # 1. End condition: node is None
        # 2. What the current layer do? : Append current level root val, and call next layer
        # 3. Return the list of all the value
        # Code starts here
        if root is None:
            return None
        result = []
        result.append(root.val)
        for rem in root.children:
            result += self.preorder(rem)
        return result


class SolutionTwo:
    def preorder(self, root: 'Node') -> List[int]:
        # Iterative method
        # we use a nodes stack to save new "root" node dynamically
        # since each pop is from the top of the stack,
        # we insert nodes in the reversed order
        # 1. Check if root is None
        # 2. Insert root into stack
        # 3. Keep poping stack and adding into stack, until all the nodes are visited
        # 4. Return result
        #
        # Time complexity: O(N)
        # Space complexity: O(3n) = O(N)
        if root is None:
            return None
        result = []
        nodes_stack = [root]
        while nodes_stack:
            node = nodes_stack.pop()
            result.append(node.val)
            nodes_stack += [child for child in node.children[::-1] if child]
        return result
