from collections import deque

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # 1. Put all nodes after head into the deque in normal order
        dq = deque()
        curr = head.next
        while curr:
            dq.append(curr)
            curr = curr.next

        # 2. Alternate popping from the back (right) and front (left)
        curr = head
        take_from_back = True
        while dq:
            if take_from_back:
                curr.next = dq.pop()
            else:
                curr.next = dq.popleft()
            
            curr = curr.next
            take_from_back = not take_from_back

        # 3. Cut off the old pointer on the final node to prevent a cycle!
        curr.next = None
