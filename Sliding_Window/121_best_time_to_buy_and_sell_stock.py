# Brute Force
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                buy = prices[i]
                sell = max(prices[i + 1: len(prices)])

                if sell - buy > maxProfit:
                    maxProfit = sell - buy

        
        return maxProfit

# Two pointer
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        maxProfit = 0
        while r < len(prices):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                maxProfit = max(profit, maxProfit)
            else:
              # This is important as we found a value that was less than the previous one
                l = r
            r += 1
        return maxProfit
