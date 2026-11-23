import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        euclid_dist = [(coor[0]**2+coor[1]**2, coor) for coor in points]
        heapq.heapify(euclid_dist) # sorts on first item of tuples
        res = heapq.nsmallest(k,euclid_dist)
        print(res)
        return [tpl[1] for tpl in res]