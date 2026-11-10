from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        fcs = defaultdict(int)
        fct = defaultdict(int)

        for c in t:
            fct[c] += 1

        best_l, best_r = 0, -1   # empty window by default
        l = 0

        for r in range(len(s)):
            fcs[s[r]] += 1
            while all(fcs[k] >= v for k, v in fct.items()):  # window covers t
                if best_r == -1 or r - l < best_r - best_l:
                    best_l, best_r = l, r
                fcs[s[l]] -= 1
                l += 1

        return s[best_l:best_r + 1]