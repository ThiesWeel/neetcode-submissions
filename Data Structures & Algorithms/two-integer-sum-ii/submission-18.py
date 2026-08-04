class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # probe from left and right
        n = len(numbers) -1
        i = 0
        j = n
            
        while True:
            # read left and right
            left = numbers[i]
            right = numbers[j]
            m = left + right - target
            print(m)
            if m > 0:
                j -= 1
            if m < 0:
                i += 1
            if m == 0:
                return [i+1,j+1]
            

