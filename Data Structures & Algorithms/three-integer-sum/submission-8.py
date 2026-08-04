class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)

        res = []
        a_last = None
        for i, a in enumerate(nums):
            if a_last  == a:
                continue
            a_last = a
            left = i+1

            right = n-1
            
            b_last = None
            c_last = None
            while left < right:
                if b_last:
                    b_last = b
                    c_last = c

                b = nums[left]
                c = nums[right]


                s = a + b + c

                if b_last == b:
                    s = 1
                if c_last == c:
                    s = -1
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

                

