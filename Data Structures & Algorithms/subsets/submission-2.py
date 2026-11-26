class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # simple backtracking
        # for each number, we either add, or we do not add to the path
        n = len(nums)
        self.res = []
        def bt(path,idx):
            if idx == n:
                self.res.append(path)
                return 
            bt(path,idx+1)
            bt(path + [nums[idx]],idx+1)
            return 
        bt([],0)
        return self.res