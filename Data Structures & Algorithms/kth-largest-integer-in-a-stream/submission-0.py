import heapq
from typing import List

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        # 1. Keep the k largest elements (nlargest returns descending order)
        self.scoreboard = heapq.nlargest(k, nums)
        # 2. Convert back into a valid min-heap so index 0 is the smallest
        heapq.heapify(self.scoreboard)

    def add(self, val: int) -> int:
        # Case 1: Fewer than k elements so far
        if len(self.scoreboard) < self.k:
            heapq.heappush(self.scoreboard, val)
        # Case 2: Heap is full, and new value beats the current k-th largest
        elif val > self.scoreboard[0]:
            heapq.heappushpop(self.scoreboard, val)
            
        return self.scoreboard[0]
