class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
            Given a list of prices, the max profit comes from day sub gains:
        For example: [1, 8, 9 , 100]
        It is easy to tell the maximum profit is 100 - 1 = 99, but also, as long as
        the next day price is higher than todays, the incremental profit will eventually addup.
        (8-1) + (9-8) + (100-9) = 99

        Time complexity: O(N)
        Space complexity: O(1)
        """
        return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))
