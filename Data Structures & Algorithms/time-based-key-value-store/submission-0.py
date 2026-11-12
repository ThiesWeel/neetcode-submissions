from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        pairs = self.map[key]
        
        if not pairs:
            return ""
            
        l = 0 
        r = len(pairs) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if pairs[mid][0] == timestamp:
                return pairs[mid][1]
            elif pairs[mid][0] > timestamp: 
                r = mid - 1  # Clean jump left, excludes mid
            else: 
                l = mid + 1  # Clean jump right, excludes mid
            
        # If we exit the loop, an exact match wasn't found.
        # 'r' now points to the largest timestamp less than our target.
        if r >= 0:
            return pairs[r][1]
            
        return ""
