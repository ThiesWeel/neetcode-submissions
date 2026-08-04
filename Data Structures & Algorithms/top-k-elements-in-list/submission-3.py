from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Time: O(N)
        Space: O(N)
        Where N is the length of nums.
        BUCKET SORT, use HEAP whenever k<<N 
        """
        count = {}
        # Create an array of empty lists. 
        # Size is len(nums) + 1 because a number can appear at most len(nums) times.
        freq = [[] for i in range(len(nums) + 1)]
        
        # 1. Count how many times each number appears
        for num in nums:
            count[num] = count.get(num, 0) + 1
            
        # 2. Put numbers into the "bucket" matching their frequency
        # Example: If '3' appears 4 times, freq[4].append(3)
        for num, c in count.items():
            freq[c].append(num)
            
        # 3. Read the buckets backwards (from highest frequency to lowest)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                # Stop once we have exactly k elements
                if len(res) == k:
                    return res