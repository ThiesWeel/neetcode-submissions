class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        clean = []
        for c in s:
            if c.isalnum():
                clean.append(c)

        
        if clean[::-1] == clean:
            return True
        return False