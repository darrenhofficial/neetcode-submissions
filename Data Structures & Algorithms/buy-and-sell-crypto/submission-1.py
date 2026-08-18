class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buying = prices[0]
        profit = 0
        for price in prices:
            if price< buying:
                buying = price
            elif price - buying > profit:
                profit = price - buying
        return profit


