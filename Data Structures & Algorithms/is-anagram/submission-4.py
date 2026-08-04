from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # we need a hashmap, as a set would remove dupes
        # we can use Counter
            return Counter(s) == Counter(t)
