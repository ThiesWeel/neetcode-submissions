from collections import defaultdict
from typing import List
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f_dict = defaultdict(int)
        for num in nums: # ~O(n)
            f_dict[num] += 1

        # get k keys with largest frequencies
        return heapq.nlargest(k, f_dict.keys(), key=f_dict.get) # ~O(n log k)
