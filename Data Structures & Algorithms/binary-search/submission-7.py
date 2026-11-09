class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def nested_bin_s(l, r):
            mid = l + (r-l)//2
            cand = nums[mid]
            print(mid, cand, target)

            if cand == target:
                return mid
            if l > r:
                return -1

            if cand > target: #look left
                return nested_bin_s(l, mid-1)
            elif cand < target: #look right
                return nested_bin_s(mid+1, r)

        res = nested_bin_s(0, len(nums)-1)
        return res