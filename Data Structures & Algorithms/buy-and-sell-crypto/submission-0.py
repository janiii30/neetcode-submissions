class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<=1:
            return 0

        buy = 0
        profit = 0

        for sell in range(len(prices)):
            print(prices[buy],prices[sell],prices[sell]-prices[buy])
            profit = max(profit, prices[sell]-prices[buy])
            if prices[sell]>=prices[buy]:
                continue
            else:
                profit = max(profit, prices[sell]-prices[buy])
                buy = sell

        return profit