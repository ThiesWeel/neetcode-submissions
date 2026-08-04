class Solution:
    def isValid(self, s: str) -> bool:
        open_set = {'(', '{', '['}
        comp_dict = {')': '(', '}': '{', ']': '['}

        mem = []
        for ch in s:
            if ch in open_set:
                mem.append(ch)
            else:
                if not mem or mem[-1] != comp_dict[ch]:
                    return False
                mem.pop()   # ✅ THIS WAS MISSING

        return not mem
