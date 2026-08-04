from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Time: O(m * n)
        Space: O(m * n)
        Where 'm' is len(strs) and 'n' is max string length.
        """
        res = defaultdict(list)
        
        for s in strs:
            count = [0] * 26
            
            for char in s:
                count[ord(char) - ord('a')] += 1 
            
            res[tuple(count)].append(s) 
            
        return list(res.values())