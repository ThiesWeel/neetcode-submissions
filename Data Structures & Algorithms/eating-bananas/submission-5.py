from math import ceil
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def in_time(k):
            return sum(ceil(p / k) for p in piles) <= h

        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2
            if in_time(mid):
                right = mid
            else:
                left = mid + 1

        return left
