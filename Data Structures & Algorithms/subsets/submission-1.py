class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # simple backtracking
        # for each number, we either add, or we do not add to the path
        n = len(nums)
        self.res = []
        def bt(path,idx):
            if idx == n:
                self.res.append(path)
                return None

            no_add = path
            add = path + [nums[idx]]
            
            bt(no_add,idx+1)
            bt(add,idx+1)
            return None
        bt([],0)
        return self.res