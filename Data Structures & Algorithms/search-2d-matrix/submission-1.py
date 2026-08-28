class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row , col = len(matrix),len(matrix[0])
        L ,R = 0, (row * col) -1
        while L<=R:
            mid = (L+R)//2
            loc = matrix[mid //col][mid%col]
            if loc == target:
                return True
            elif loc < target:
                L = mid +1
            else :
                R = mid -1
        return False
                    
