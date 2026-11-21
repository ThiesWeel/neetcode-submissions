# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = ListNode()
        res_head = res
        min_heap = []
        
        
        # init heapq
        # Push (value, list_index, node_reference)
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, i, node))

        # start loop, needs to run untill all ListNodes are at there end, which means the heapq is empty
        while len(min_heap) > 0:
            # Pop the smallest node and unpack all 3 values at once
            val, i, smallest_node = heapq.heappop(min_heap)
            res.next = smallest_node
            res = res.next
            
            

            # now we add move to next node for the ListNode at index i in lists
            if lists[i].next:
                lists[i] = lists[i].next
                heapq.heappush(min_heap, (lists[i].val, i, lists[i]))



        return res_head.next
        