class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L = 0
        R = len(heights) -1
        area = 0
        while L < R:
            loc_min = min(heights[L],heights[R])
            curr_area = (R-L) * loc_min
            if area < curr_area:
                area = curr_area
                
            if loc_min == heights[L]:
                L+=1
            else:
                R-=1
        return area
            
   

