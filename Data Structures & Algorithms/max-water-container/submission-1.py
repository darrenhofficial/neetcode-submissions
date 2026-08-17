class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L = 0
        R = len(heights) -1
        area = 0
        while L < R:
            if heights[L]<heights[R]:
                curr_area = (R-L)*heights[L]
                L+=1
            else:
                curr_area = (R-L) * heights[R]
                R-=1
            if curr_area > area:
                area = curr_area
        return area
            
   

