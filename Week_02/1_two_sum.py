def double_loop(n, t):
    """Calculate all the possible combinations with a double loop
    Then compare the sum with target, if equal, return

    Time complexity: O(n)
    Space complextity: n

    """
    for i in range(len(n) - 1):
        for j in range(i + 1, len(n)):
            if n[i] + n[j] == t:
                return [i, j]


def hashmap_method1(n, t):
    """Use a hashmap to keep the value (key) <-> index(value) pair. The key of the hashmap
    would be target - nums[i], and index will be i. For example, for list [2, 7, 11, 15], and
    target 9, the hashmap will look like: {7:0, 2:1, -2:2, -6:3}. When we iterate the nums list,
    if there is a solution, the target-nums[i] would be already captured in the hashmap.

    For example, nums[0] = 2, and target - nums[0] = 7, so hashmap is {7:0}, then when
    we move to nums[1] which is 7, the hashmap would already have key 7, which means there is
    a solution.
    """
    d = {}
    for i in range(len(n)):
        if n[i] in d:
            return [d[n[i]], i]
        d[t - n[i]] = i


def hashmap_method2(n, t):
    """Use hashmap to record each element in n, then check if t-n in the
    hashmap

    Time complexity: O(n)
    Space complexity: O(2n) = O(n)
    """
    d = {v: k for k, v in enumerate(n)}
    for i in range(len(n)):
        j = d.get(t - n[i], 0)
        if j != 0 and i != j:
            return [i, j]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return hashmap_method1(nums, target)