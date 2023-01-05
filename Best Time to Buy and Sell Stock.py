class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min1=prices[0]
        profit=0
        for i in range(1,len(prices)):
            if prices[i]<min1:
                min1=prices[i]
            else:
                profit=max(profit,prices[i]-min1)
        return profit
        
