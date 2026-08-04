import typing
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # O(n) for both space and time, 1 stack, length n, 1 iteration trough whole list
        # We can't save all temps 
        n = len(temperatures)
        stack: List[List[int]] = []
        res = [0] * n
        # when we iterate fowards,
        for i,t in enumerate(temperatures):
            while stack and t>stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append([t,i])
        return res