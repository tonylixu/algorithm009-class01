## 学习笔记

### 理论收获
* [深度优先搜索 (Depth-first-search) 学习笔记](./dfs_study_note.md)


* 广度优先搜索 (Breadth-first-search)
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