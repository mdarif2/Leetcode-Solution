class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit=0
        n=len(prices)
        for i in range(1,len(prices)):
            
            if prices[i]>prices[i-1]:
                maxprofit+=prices[i]-prices[i-1]
            i+=1
        return maxprofit        
        
