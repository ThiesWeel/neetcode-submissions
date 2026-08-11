class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_seq = 0
        
        for num in nums:
            if num - 1 not in nums:  
                # sequence start 
                length = 1
                while num + length in nums:
                    length += 1
                max_seq = max(max_seq, length)
        
        return max_seq