class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 1. Handle empty list edge cases
        if not list1: return list2
        if not list2: return list1

        def recursion(alpha, beta):
            # Base cases: one list ran out
            if not beta:
                return
            if not alpha.next:
                alpha.next = beta
                return

            if alpha.next.val >= beta.val:
                nxt1 = alpha.next
                nxt2 = beta.next     # Save the rest of beta before rewiring
                
                alpha.next = beta    # Insert beta right after alpha
                beta.next = nxt1     # Connect beta to the rest of alpha
                
                recursion(beta, nxt2) # Move forward: beta is now the new 'alpha'
            else:
                recursion(alpha.next, beta)

        # 2. Pick the smaller head to anchor the list
        if list1.val <= list2.val:
            recursion(list1, list2)
            return list1
        else:
            recursion(list2, list1)
            return list2
