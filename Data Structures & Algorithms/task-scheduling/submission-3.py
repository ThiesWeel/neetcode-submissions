from collections import deque, Counter
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        heap = [-cnt for cnt in counts.values()]
        heapq.heapify(heap)
        
        cooldown = deque()  # Stores (available_time, neg_count)
        time = 0
        
        while heap or cooldown:
            time += 1
            
            # 1. Run the most frequent available task
            if heap:
                cnt = heapq.heappop(heap) + 1
                if cnt < 0:
                    cooldown.append((time + n, cnt))
            
            # 2. If the oldest cooling task is ready for the next tick, move it back to heap
            if cooldown and cooldown[0][0] == time:
                heapq.heappush(heap, cooldown.popleft()[1])
                
        return time
