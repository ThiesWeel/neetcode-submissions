from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        fc = defaultdict(int) #freq. counter
        l = 0
        mssl = 0 #max sub string length
        for r in range(len(s)):
            fc[s[r]] += 1 # add 1 (or add to fc, key: val -> char:1)
            
            # check violation count, if violated, move l
            while sum(fc.values()) - max(fc.values()) > k:
                l += 1
                fc[s[l-1]] -= 1

            mssl = max(mssl, r - l + 1)

        return mssl