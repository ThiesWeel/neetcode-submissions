class Solution:
    def encode(self, strs: List[str]) -> str:
        """
        We need Type-Length-Value encoding, [len][del][str]
        """
        res = ""
        for s in strs: 
            res += str(len(s)) + '#' + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            # 1. Scan forward to find the delimiter '#'
            while s[j] != '#':
                j += 1
            
            # 2. Extract the length (everything from i up to j)
            length = int(s[i:j])
            
            # 3. Slice the actual string out
            # It starts right after the '#' (j + 1) and goes for 'length' characters
            parsed_string = s[j + 1 : j + 1 + length]
            res.append(parsed_string)
            
            # 4. Jump i forward to the start of the next chunk
            i = j + 1 + length
            
        return res