class Solution:
    def isValid(self, s: str) -> bool:
        # we must iterate trough s
        # every open, we add to list
        # every close we check last item, if equal to complement
        # we pop from the list
        # this would be O(n) time and space
        # edge cases: 
        # 1. closer first: check from list, if complement not last item, return False
        # 2.
        open_set = {'(','{','['}
        comp_dict = {')':'(','}':'{',']':'['}

        mem = [0]
        for ch in s:
            # new open ch, append to mem
            if ch in open_set:
                mem.append(ch)
            # no open, so must be close ch
            else:
                # find compl., open ch 
                open_ch = comp_dict[ch]
                # if last added item equal to open ch,. remove from mem
                if mem[-1] == open_ch:
                    mem = mem[0:-1]
                # if both not ture we have:
                # an close ch that is not after its dedicated open ch
                # and we are still able to nest bracket duo's in eachother
                else:
                    return False
        # make sure everything is closed!
        if len(mem) == 1:
            return True
        else:
            return False
                

            