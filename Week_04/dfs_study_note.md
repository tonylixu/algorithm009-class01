### 深度优先搜索 (DFS - Depth first search)
* 深度优先搜索，也被称为深度优先遍历，最直观的例子就是走迷宫。假设你站在迷宫的某个岔路口，
然后想找到出口。你随意选择一个岔路口来走，走着走着发现走不通的时候，你就回退到上一个岔路口，
重新选择一条路继续走，直到最终找到出口。这种走法就是一种深度优先搜索策略。
* 深度优先搜索用的是一种非常著名的算法思想， 称之为"回溯"思想。
* 深度优先搜索算法消耗内存的主要是visited、prev 数组和递归调用栈。
visited、prev 数组的大小跟顶点的个数 V 成正比，递归调用栈的最大深度不会超过顶点的个数，
所以总的空间复杂度就是 O(V)。
* 深度优先搜索和广度优先搜索简单粗暴，没有什么优化，所以通常也被称为暴力搜索算法。所以DFS
和BFS通常适用于状态空间不大的搜索。
* 示例代码
```python
# Binary tree
def dfs(node):
    if node in visited:
        # Already visited
        return

    visited.add(node)

    # Process current node
    # ... # logic here
    dfs(node.left)
    dfs(node.right)
```
```python
# N-ary tree
visited = set()

def dfs(node, visited):
    if node in visited:
        return

    visited.add(node)
    # Process current node here.
    ...
    for next_node in node.children():
        if not next_node in visited:
            dfs(next_node, visited)
```
```python
# Stack

def dfs(tree):
    if not tree:
        return []
    visited, stack = [], [tree.root]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
        
        process(node)
        nodes = generate_related_nodes(node)
        stack.push(nodes)

    # Other processing work
    ...
```
