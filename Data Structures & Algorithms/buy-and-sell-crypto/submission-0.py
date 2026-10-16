class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit = sell - buy
        res = [0] * len(prices)
        max_profit = 0

        for i, buy in enumerate(prices):
            for j, sell in enumerate(prices):
                if j > i:
                    profit = sell - buy
                    if profit > res[i]:
                        res[i] = profit

        for profit in res:
            if profit > max_profit:
                max_profit = profit

        return max_profit
