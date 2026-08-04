class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}

        for sc, tc in zip(s, t):
            count[sc] = count.get(sc, 0) + 1
            count[tc] = count.get(tc, 0) - 1

        return all(v == 0 for v in count.values())
