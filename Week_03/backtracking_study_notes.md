## 回溯学习笔记

### 何为回溯
回溯（backtracking）采用试错的思想，它尝试分步的去解决一个问题。在分步解决问题的过程中，
当它通过尝试发现现有的分步答案不能得到有效的正确解答的时候，它将取消上一步甚至是上几步的计算，
在通过其它的可能的分步解答再次尝试寻找问题的答案。

回溯法将会不断的在每一层去尝试，每一层有不同的办法，一个一个的去试。

回溯法通常用最简单的递归方法来实现，在反复重复上述的步骤后可能出现两种情况：
* 找到一个可能存在的正确的答案
* 在尝试了所有的可能的分步方法后宣告该问题没有答案

在最坏的情况下，回溯法会导致一次复杂度为指数时间的计算。

回溯最典型的应用是在八皇后以及数独上面。

### 回溯的本质
回溯法将会不断的在每一层去尝试，每一层有不同的办法，一个一个的去试。回溯本质上就是递归的思想。

### 回溯代码模版
可以使用范型递归的模版
```python
def backtracking(level, param1, param2):
    # Recursion teminator
    if level > MAX:
        return
    # Process current logic
    process(level, data)

    # Drill down one level
    backtracking(level + 1, p1, p2)

    # Reverse state and cleanup
```