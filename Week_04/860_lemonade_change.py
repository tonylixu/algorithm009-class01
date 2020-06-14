"""
Leetcode: https://leetcode.com/problems/lemonade-change/
When a customer gives us a $20, we only have two choices:
1. Return three $5s
2. Return one $10 and one $5

Obviously second option is better than the first option. The more $5 you have, the more flexibility you have. Since
the bills are multiples of each other, which makes greedy algorithm possible.
"""


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        return self.greedy(bills)

    def greedy(self, bills):
        """
        Time complexity: O(N)
        Space complexity: O(1)
        """
        fives = tens = 0
        for b in bills:
            if b == 5:
                fives += 1
            elif b == 10:
                fives, tens = fives - 1, tens + 1
            elif tens > 0:
                fives, tens = fives - 1, tens - 1
            else:
                fives -= 3
            if fives < 0:
                return False
        return True
