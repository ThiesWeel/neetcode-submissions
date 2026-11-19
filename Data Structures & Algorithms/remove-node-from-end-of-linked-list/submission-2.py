class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = fast = dummy

        # 1. Create a gap of n nodes between slow and fast
        for _ in range(n + 1):
            fast = fast.next

        # 2. Slide the window until fast hits the end
        while fast:
            slow = slow.next
            fast = fast.next

        # 3. slow is now right before the target node—bypass it
        slow.next = slow.next.next

        return dummy.next
