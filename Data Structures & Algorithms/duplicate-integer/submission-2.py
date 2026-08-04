class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # we iterate once over the list
        seen = set()
        for num in nums: # time O(n)
            if num in seen: # time O(1)
                return True
            
            seen.add(num)
            
        return False