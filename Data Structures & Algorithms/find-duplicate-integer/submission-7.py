class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1: find a meeting point inside the cycle
        slow = nums[0]
        fast = nums[nums[0]]
        while fast != slow:
            slow = nums[slow]
            fast = nums[nums[fast]]

        # Phase 2: one pointer from the start, one from the meeting point
        slow2 = 0
        while fast != slow2:
            fast = nums[fast]
            slow2 = nums[slow2]

        return fast