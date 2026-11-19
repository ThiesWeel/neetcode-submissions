# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        if not slow:
            return False
        while slow.next: # slow did not reach end yet
            slow = slow.next
            try:
                fast = fast.next.next
            except:
                return False

            if fast == slow:
                return True
        return False
