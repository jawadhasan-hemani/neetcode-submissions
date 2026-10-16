class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 #left.buy and right.sell
        maxP = 0
        # buy low, sell high
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r+=1

        return maxP