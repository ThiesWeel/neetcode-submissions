class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        strt_node = dummy
        carry = 0
        
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            som = val1 + val2 + carry
            value = som % 10    # digit to store: 12 % 10 = 2
            carry = som // 10   # carry forward: 12 // 10 = 1
            
            dummy.next = ListNode(value)
            dummy = dummy.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
                
        return strt_node.next
