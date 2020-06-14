### 广度优先搜索 (BFS - Breadth first search)
* 广度优先搜索，通俗的理解就是，地毯式层层推进，从起始顶点开始，依次往外遍历。
广度优先搜索需要借助队列来实现，遍历得到的路径就是，起始顶点到终止顶点的最短路径。
* 广度优先搜索的时间复杂度是 O(V+E)，其中，V 表示顶点的个数，E 表示边的个数。
当然，对于一个连通图来说，也就是说一个图中的所有顶点都是连通的，E 肯定要大于等于 V-1，
所以，广度优先搜索的时间复杂度也可以简写为 O(E)。
* 广度优先搜索的空间消耗主要在几个辅助变量 visited 数组、queue 队列、prev 
数组上。这三个存储空间的大小都不会超过顶点的个数，所以空间复杂度是 O(V).
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