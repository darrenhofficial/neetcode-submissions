class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        for i in range(len(prices)):
            L = 0
            R = len(prices) -1-i
            while L<R:
                diff = prices[R] - prices[L]
                if diff > profit:
                    profit = diff
                L+=1
        return profit
