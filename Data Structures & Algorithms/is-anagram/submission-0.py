class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if sorted(s) == sorted(t):
            # ordered and then compare
            # if equal to each other, same character with the same freq. in both strings
            return True

        else:
            return False