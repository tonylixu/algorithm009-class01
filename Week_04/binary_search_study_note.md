### 二分查找(Binary search)
* 定义：二分查找（Binary Search）算法，也叫折半查找算法. 二分查找是一种非常简单易懂的快速查找算法，它针对
的是一个有序的数据集合，查找思想类似于分治。每次都通过跟区间的中间元素对比，将待查找的区间缩小为之前的一半，
直到找到要查找的元素，或者区间被缩小为 0。
* 二分查找的前提：
  * 目标函数单调性 （单调递增或者递减）
  * 存在上下界
  * 能够通过索引访问
* 二分查找是一种非常高效的查找算法, 它的算法复杂度为O(logn)。

### 二分查找适用的场景
* 如果要处理的数据量很小，完全没有必要用二分查找，顺序遍历就足够了。比如我们在一个大小为 10 的数组中
查找一个元素，不管用二分查找还是顺序遍历，查找速度都差不多。只有数据量比较大的时候，
二分查找的优势才会比较明显。
* 最后，数据量太大也不适合二分查找。二分查找的底层需要依赖数组这种数据结构，而数组为了支持随机访问的特性，
要求内存空间连续，对内存的要求比较苛刻。


### 实战题目
* 半有序数组
  * [Python solution](./half_sorted.py)
* [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)
  * [Python solution](./33_search_in_rotated_sorted_array.py)
* [122. Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/)
  * [Python solution](./122_best_time_to_buy_and_sell_stock_ii.py)
  
### 代码模版
```python
left, right = 0, len(array) - 1
while left <= right:
    mid = (left + right)//2
    if array[mid] == target:
        # Find the target
        break or return result
    elif array[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
```