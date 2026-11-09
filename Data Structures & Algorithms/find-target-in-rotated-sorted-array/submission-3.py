class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r: # we will point at target, so we will stop at l = r 
            mid = l + (r-l)//2 # biased to l
            print(mid)
            if nums[mid] == target:
                return mid
            
            if nums[l] <= nums[mid]: # l-side is sorted
                if nums[l] <= target < nums[mid]: # target in sorted l-side
                    r = mid - 1
                else: # target not in sorted l-side
                    l = mid + 1

            else: # r-side is sorted
                if nums[r] >= target > nums[mid]: # target in sorted r-side
                    l = mid + 1
                else: # target not in sorted r-side
                    r = mid - 1

            


        return -1