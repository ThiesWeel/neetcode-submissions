class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        
        block_list = [[], [], [], [], [], [], [], [], [], ] 
        col_list   = [[], [], [], [], [], [], [], [], [], ]
        row_list   = [[], [], [], [], [], [], [], [], [], ]
        
        for j, row in enumerate(board):
            for i, el in enumerate(row):
                if el == '.':
                    continue
                row_list[j].append(el)
        
                col_list[i].append(el)
                block_num = (j // 3)*3 + (i) // 3
                block_list[block_num].append(el)
        
        for sublist in block_list:
            if len(sublist) != len(set(sublist)):
        
                return False
        
        for sublist in col_list:
            if len(sublist) != len(set(sublist)):
        
                return False
                
        for sublist in row_list:
            if len(sublist) != len(set(sublist)):
        
                return False
        return True

