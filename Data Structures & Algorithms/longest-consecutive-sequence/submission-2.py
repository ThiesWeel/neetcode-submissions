class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_count = 0
        print(nums)
        nums = set(nums)
        print(nums)
        while nums:
            x_0 = next(iter(nums))
            print(x_0)
            seen = {x_0}
            
            x_up = x_0
            while x_up+1 in nums:
                seen.add(x_up+1)
                x_up +=1
          
            x_down = x_0
            while x_down-1 in nums:
                seen.add(x_down-1)
                x_down -= 1

            count = len(seen)
            if count > max_count:
                max_count = count 
            nums -= seen
        return max_count
        
        