from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        while l < r:
            mid = l + (r - l) // 2
            
            # If mid element is greater than the rightmost element,
            # the minimum MUST be somewhere to the right of mid.
            if nums[mid] > nums[r]:
                l = mid + 1
            # Otherwise, mid could be the minimum, or the minimum is to the left.
            else:
                r = mid
                
        # Loop terminates precisely when l == r, pointing exactly at the minimum element.
        return nums[l]

