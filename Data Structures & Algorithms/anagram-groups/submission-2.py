from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # defaultdict(list) automatically creates an empty list if a key doesn't exist yet!
        # This perfectly handles your idea of giving the value an empty list.
        res = defaultdict(list)
        for s in strs:
            # Create an array of 26 zeros to represent 'a' through 'z'
            count = [0]*26

            for char in s:
                # ord() gets the ASCII value.
                count[ord(char)-ord('a')] += 1
            
            res[tuple(count)].append(s)
            # Convert the list to a tuple so it can be used as a dictionary key
            
        # .values() returns all the grouped lists
        return list(res.values())