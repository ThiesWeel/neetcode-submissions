# Definition for singly-linked list.
# class LitNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        if not slow:
            return False
        while fast and fast.next: # fast did not reach end yet
            slow = slow.next
            fast = fast.next.next 
            if fast == slow:
                return True
        return False
