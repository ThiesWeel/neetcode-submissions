class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)

        res = []
        for i, a in enumerate(nums):
            left = i+1
            print(left)
            print(nums)
            right = n-1
            while left < right:
                
                b = nums[left]
                c = nums[right]
                s = a + b + c
                if s > 0:
                    right -= 1
                elif s < 0:
                    left += 1
                elif s == 0:
                    res_i = [a,b,c]
                    if res_i not in res:
                        res.append([a,b,c])
                    left += 1
                    right -= 1
  

        return res

                

