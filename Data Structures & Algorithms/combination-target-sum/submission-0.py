class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        results = []
        
        def bt(path, total, idx):
            # Base case 1: Found a valid combination
            if total == target:
                results.append(path)
                return
            
            # Base case 2: Pruning (overshot target or ran out of numbers)
            if total > target or idx == n:
                return
            
            # Choice 1: Include nums[idx] (stay at idx to allow reuse)
            bt(path + [nums[idx]], total + nums[idx], idx)
            
            # Choice 2: Skip nums[idx] (move forward)
            bt(path, total, idx + 1)
            
        bt([], 0, 0)
        return results
