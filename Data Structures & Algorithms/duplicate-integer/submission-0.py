class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == len(set(nums)):
            # we contain only unique elements
            # no values appear more than once
            return False
        else:
            return True