from math import ceil
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = ceil(sum(piles) / h)    # Lower bound for k
        r = max(piles)              # Upper bound for k
        
        ans = r                     # Track the minimum valid speed found so far

        while l <= r:
            k = l + (r - l) // 2
            cand_h = 0
            
            for pile in piles:
                cand_h += ceil(pile / k)

            if cand_h <= h: 
                # This speed works! Save it, and try to find an even smaller speed
                ans = k
                r = k - 1
            else: 
                # Too slow, we must increase the speed
                l = k + 1
            
        return ans
