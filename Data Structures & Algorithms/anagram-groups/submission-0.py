from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            # build frequency signature
            freq = [0] * 26
            for ch in s:
                freq[ord(ch) - ord('a')] += 1

            signature = tuple(freq)   # hashable key
            groups[signature].append(s)

        return list(groups.values())
