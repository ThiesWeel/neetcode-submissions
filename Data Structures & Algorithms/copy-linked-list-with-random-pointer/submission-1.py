class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Map None -> None to handle null .next and .random pointers cleanly
        old_to_copy = {None: None}

        # Pass 1: Create a detached copy of every node
        curr = head
        while curr:
            old_to_copy[curr] = Node(curr.val)
            curr = curr.next

        # Pass 2: Connect .next and .random pointers on the copied nodes
        curr = head
        while curr:
            copy = old_to_copy[curr]
            copy.next = old_to_copy[curr.next]
            copy.random = old_to_copy[curr.random]
            curr = curr.next

        return old_to_copy[head]