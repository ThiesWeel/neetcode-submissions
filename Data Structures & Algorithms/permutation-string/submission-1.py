from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        fc1 = defaultdict(int)
        for c in s1:
            fc1[c] += 1

        fc2 = defaultdict(int)
        l = 0
        for r in range(len(s2)):
            fc2[s2[r]] += 1

            if r - l + 1 > len(s1):        # window too long: drop the left char
                fc2[s2[l]] -= 1
                if fc2[s2[l]] == 0:
                    del fc2[s2[l]]         # remove zero counts so == works
                l += 1

            if fc1 == fc2:
                return True
        return False