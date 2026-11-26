import heapq

class MedianFinder:
    def __init__(self):
        self.small = []  # Max-heap (negative vals values) [-4,-3,-2]
        self.large = []  # Min-heap [5,6]

    def addNum(self, num: int) -> None:
        # Push to max-heap, then move its largest element to min-heap
        heapq.heappush(self.small, -num)
        heapq.heappush(self.large, -heapq.heappop(self.small))

        # Keep sizes balanced (small can have at most 1 extra element)
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            median = -heapq.heappop(self.small)
            heapq.heappush(self.small,-median)
            return float(median)
        else:
            small_num = -heapq.heappop(self.small)
            large_num = heapq.heappop(self.large)
            # push 'm back
            heapq.heappush(self.small,-small_num)
            heapq.heappush(self.large,large_num)
            return (small_num + large_num) / 2.0
