## 递归学习笔记

### 何为递归
递归是解决问题的一种方法，它将问题不断的分成更小的子问题，直到子问题可以用普通的方法解决。在通常
情况下， 递归会使用一个不停调用自己的函数。尽管表面上看起来很普通， 但是递归可以帮助我们写出
非常优雅的解决方案。

### 递归的本质
* 递归的本质就是循环， 只不过是通过函数体来进行循环
  * 向下进入到不同的递归层，向上回到原来的递归层
  * 不能跳跃，必须一层一层的下或者回来，有对称性
  * 每一层的环境和local变量都是一份copy，但是参数和全局变量可以存在于不同的递归层


### 递归代码模版
 ```python
# Python recursive template
def recursion(level, param_1, param_2, ...):
    # Recursion terminator
    if level > MAX_LEVEL:
        process_result
        return

    # Process logic in current level
    process(level, data...)

    # Drill down
    recursion(level + 1, p1, ...)

    # Reverse the current level status if needed
```

### 递归简单题目
* 计算数字列表的和， 给定数字列表nums = [1, 3, 5, 7, 9, 10, 11]，用递归的办法求出nums的和。
```python
def calculate_sum(nums):
    """
    Calculate list of ints recursively
    :param nums: List of ints
    :return: Sum of ints
    Time complexity: O(N)
    Space complexity: O(N)

    >>> nums =[1, 3, 5, 7, 9, 10, 11]
    >>> print(calculate_sum(nums))
    46
    """
    # Recursion terminator
    if len(nums) == 1:
        return nums[0]
    # Process logic in current level
    #     - At each level, the sum = nums[0] + nums[1:]
    # Drill down to next level
    #     - We pass nums[1:] to the next level
    # No need to do cleanups
    #     - Nothing to do here
    return nums[0] + calculate_sum(nums[1:])
```
* Convert integer to str (base 2~16). For a given integer, return the base(n) string
representation. Base n is between 2 to 16
```python
def to_string(num, base):
    """
    Convert num to base string format
    
    Time complexity: O(log_base n)
    Space complexity: O(1)
    """
    convert_string = '0123456789ABCDEF'
    # Recursion terminator
    if num < base:
        return convert_string[num]
    # Process logic in current level
    #     - Append this level converted string
    # Drill down to next level
    #     - Call itself on num//base --> A little closer to solution
    # Cleanups
    #     - Nothing to do here
    return to_string(num//base, base) + convert_string[num%base]

stack = []
convert_string = '0123456789ABCDEF'
def to_string_stack(num, base):
    if num < base:
        stack.append(convert_string[num])
        return
    stack.append(convert_string[num%base])
    to_string_stack(num//base, base)
```