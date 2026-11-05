class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # brute force, runing time is O(n^2)
        # profit = 0
        # for l in range(len(prices)-1):
        #     for r in range(l+1,len(prices)):
        #         profit = max(profit,prices[r]-prices[l])
        # return profit
        # optimize
        profit = 0
        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            # if there is no else then will calcaute the negative profit
            else:
                profit = max(profit, price - lowest)
        return profit  
        