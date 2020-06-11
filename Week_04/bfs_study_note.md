### 广度优先搜索 (BFS - Breadth first search)
* 示例代码
```python
def bfs(graph, start, end):
    queue = []
    queue.append([start])
    visited.add(start)

    while queue:
        node = queue.pop()
        visited.add(node)
        
        process(node)
        nodes = generate_related_nodes(node)
        queue.push(nodes)

    # Other processing work
    ...
```