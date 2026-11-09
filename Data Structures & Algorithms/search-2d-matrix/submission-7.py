class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nums = [el for row in matrix for el in row] # O(N)
        
        l = 0
        r = len(nums) - 1

        #iterative approach
        while l<r+1:
            mid = l + (r-l)//2
            cand = nums[mid]
            print(cand)
            if cand == target:
                return True
            elif cand < target:
                l = mid+1
            elif cand > target:
                r = mid-1
        
        return False
            
        
