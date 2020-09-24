class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        max_profit = 0
        buy_price = max(prices)
        for price in prices:
            buy_price = min(buy_price, price)
            max_profit = max(price - buy_price, max_profit)
            
        return max_profit