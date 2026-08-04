class Solution:
    def isPalindrome(self, s: str) -> bool:
        fwd = []
        for ch in s:
            if ch.isalnum():
                fwd.append(ch.lower())

        return fwd == fwd[::-1]
