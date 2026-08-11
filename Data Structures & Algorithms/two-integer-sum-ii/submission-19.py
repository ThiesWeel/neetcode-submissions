class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)

        left = 0
        right = n-1
        summ = numbers[left] + numbers[right]
        
        while summ != target:
            if summ - target < 0:
                left += 1
            else:
                right -= 1
            summ = numbers[left] + numbers[right]
        return [left+1,right+1]