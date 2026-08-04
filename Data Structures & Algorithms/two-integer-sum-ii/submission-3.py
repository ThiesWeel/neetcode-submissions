class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # val: index dict, use associative mapping for quicker lookup
        dic = {val: i+1 for i, val in enumerate(numbers)}

        for val, i in dic.items():
            comp = target - val
            if comp in dic.keys():
                j = dic[comp]
                if j != i:
                    return sorted([i,j])