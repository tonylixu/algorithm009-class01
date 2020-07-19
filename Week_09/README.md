# 学习笔记

## 动态规划

### 动态规划的复习
* 递归: 函数自己调用自己
```python
def recur(level, param):
    # Recursion terminator
    if level > MAX_LEVEL:
        return

    # Process current logic
    process(level, param)

    # Drill down to next level
    recur(level + 1, param)

    # Restore current status and cleanup
```

* 分治:分而治之， 用到递归
```python
def divide_conquer(problem, param1, param2, ...):
    # Recursion terminator
    if problem is None:
        print_result
        return

    # Prepare data
    data = prepare_data(problem)
    subproblems = split_problem(problem, data)

    # Conquer subproblems
    subresult1 = self.divide_conquer(subproblems[0], p1, ...)
    subresult2 = self.divide_conquer(subproblems[1], p1, ...)
    subresult3 = self.divide_conquer(subproblems[2], p1, ...)

    # Process and generate the final result
    result = process_result(subresult1, subresult2, subresult3, ...)

    # Revert the current level states
```
* 感触
  * 人肉递归低效，不推荐
  * 关键是找到最近最简的方法，将其拆解成可重复解决的问题
  * 数学归纳法思维
  * 本质: 寻找重复性 -> 计算机指令集

* 动态规划由分治引申，如果一个分治问题本身的话，它的子问题具有所谓的重叠或者
所谓的最优子结构的时候，我们就会发现可以去重或者淘汰次优解。在这种情况下，如果
分治的过程中每一步淘汰次优解的话，就变成了所谓的动态规划。

* 动态规划要点
  * Simplifying a complicated problem by breaking it down into simpler 
  sub-problems (In a recursive manner)
  * Divide and Conquer + Optimal substructure
  * 顺推形式: 动态递推
```python
def DP():
    dp = [][]  # Two dimensional
    for i in range(M):
        for j in range(N):
            dp[i][j] = _function(dp[i']j'])
    return dp[M][N]
```
* 经典题目
  * 爬楼梯
  * 硬币置换
  * 不同路径
  * 打家劫舍
  * 最小路径和
  * 股票买卖

### 进阶版的动态规划 (高级DP)
* 复杂度来源: 
  * 状态有更多的维度
  * 状态方程更加复杂
  * 本质还是内功，逻辑思维以及数学
