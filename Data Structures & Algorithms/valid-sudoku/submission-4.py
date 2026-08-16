class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 用 9x9 的布尔数组记录每行、每列、每个九宫格中数字 1-9 是否出现过
        rows = [[False] * 9 for _ in range(9)]
        cols = [[False] * 9 for _ in range(9)]
        boxes = [[False] * 9 for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue

                num = int(val) - 1  # 转为 0-8 的索引
                b = (r // 3) * 3 + (c // 3)  # 九宫格索引 0-8

                # 如果之前已经出现过，直接返回 False
                if rows[r][num] or cols[c][num] or boxes[b][num]:
                    return False

                # 标记为已出现
                rows[r][num] = True
                cols[c][num] = True
                boxes[b][num] = True

        return True