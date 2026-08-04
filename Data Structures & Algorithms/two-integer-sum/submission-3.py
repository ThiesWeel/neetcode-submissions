class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            # iterate over all elements
            complement =  target - num # get complement, and check if in set
            if complement in set(nums):
                j = nums.index(complement) # ~ O(n)
                if i != j: 
                    return sorted([i,j]) # ~ O(1)

