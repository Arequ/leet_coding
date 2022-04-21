class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for i in range(len(prices)):
            diff = prices[i] - min_price
            if prices[i] < min_price:
                min_price = prices[i]
            elif diff > max_profit:
                max_profit = diff
        return max_profit
                