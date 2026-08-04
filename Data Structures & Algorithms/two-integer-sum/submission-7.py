class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # look for complement in hashmap: num = key, index = value 
        hashMap = {}

        for i, num in enumerate(nums): # ~ time O(n), space O(n)
            compl = target - num
            # check if complement in hashmap 
            if compl in hashMap: # ~ O(1)
                return [hashMap[compl], i]
            else: 
                hashMap[num] = i
            