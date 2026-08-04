class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # we iterate once over the list
        hashMap = {}
        for num in nums: # time O(n)
            if num in hashMap: # time O(1)
                return True
            
            hashMap[num] = True # space O(n)
        return False