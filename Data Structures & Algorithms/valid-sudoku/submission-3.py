class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import defaultdict
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        for rows_idx in range(len(board)):
            for cols_idx in range(len(board)):
                
                N = board[rows_idx][cols_idx]
                if N!=".":
                    
                    if N in rows[rows_idx] or N in cols[cols_idx] or N in boxes[rows_idx//3,cols_idx//3]:
                        return False
                    rows[rows_idx].add(N)
                    cols[cols_idx].add(N)
                    boxes[rows_idx//3,cols_idx//3].add(N)
        return True
