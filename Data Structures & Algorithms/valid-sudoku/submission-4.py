class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # we neede to make lists for each row, col, and sqaire
        # ~O(n) space
        rows = [set() for _ in range(9)] 
        cols = [set() for _ in range(9)]
        sqrs = [set() for _ in range(9)]
        
        # ~O(n^2) time
        for j, row in enumerate(board): # j is row index
            for i, num in enumerate(row): # i is col index

                if num == '.': # skip loop if not a number
                    continue 

                # for row, col, sqr, if in set already, return False, else we add.
                if num in rows[j]:                    
                    return False
                rows[j].add(num) 

                if num in cols[i]:
                    print('cols')
                    return False
                cols[i].add(num)

                # indexing in western reading order
                k = 3*(j // 3) + (i // 3)  
                if num in sqrs[k]:
                    print('sqrs')
                    return False
                sqrs[k].add(num)

        return True
