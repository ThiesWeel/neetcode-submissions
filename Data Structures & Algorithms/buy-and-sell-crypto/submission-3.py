class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        bp = 0
        for r in range(len(prices)):            
            if prices[l] > prices[r]:
                #new lower prices found
                l = r
            bp = max(bp, prices[r] - prices[l])
            
        return bp
        