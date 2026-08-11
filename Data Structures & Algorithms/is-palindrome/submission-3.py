class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        clean = ''.join(c for c in s if c.isalnum())

        if clean[::-1] == clean:
            return True
        return False