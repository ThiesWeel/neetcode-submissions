class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        hashMap = {} # This is what will consume O(n) space

        for i, num in enumerate(nums):
            compl = target - num
            
            # Dictionary lookup is average O(1) time
            if compl in hashMap: 
                return [hashMap[compl], i]
            else: 
                hashMap[num] = i