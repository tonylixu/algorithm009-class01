## 分治学习笔记

### 何为分治
分而治之（Divide and Conquer）的思想。分而治之，我们通常简称为分治。它的思想就是，将一个复杂的问题，
分解成两个甚至多个规模相同或类似的子问题，然后对这些子问题再进一步细分，直到最后的子问题变得很简单，很容易就能被求解出来，
这样这个复杂的问题就求解出来了。

### 分治的本质
* 分治的本质


### 分治代码模版
```python
def divide_conquer(problem, param1, param2, ...):
    # Recursion terminatior:
    if problem is None:
        print_result
        return

    # Prepare data
    data = prepare_data(problem)
    subproblems = split_problem(problem, data)

    # conquer subproblems
    subresult1 = self.divide_conquer(subproblems[0], p1, ...)
    subresult2 = self.divide_conquer( subproblems[1], p1, ...)
    subresult3 = self.divide_conquer(subproblems[2], p1, ...)

    # process and generate the final result
    result = process_result(subresult1, subresult2, subresult3, ...)

    # revert the current level states
```

### 分治题目
* Calculate power(x, n) (https://leetcode.com/problems/powx-n/)
```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
            total = x^n is equivalent to total = x^(2/n); total * total
        Time complexity: O(logN)
        Space complexity: O(1)
        """
        def split_pow(x, n):
            if n == 0:
                return 1
            half = split_pow(x, n>>1)
            return half * half * x if n & 1 else half * half
        total = split_pow(x, abs(n))
        return 1/total if n < 0 else total

```