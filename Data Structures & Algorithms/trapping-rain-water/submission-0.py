class Solution:
    def trap(self, height: List[int]) -> int:
        L , R = 0, len(height) - 1
        maxL , maxR =  height[L], height[R]
        volume = 0
        while L < R:
            if maxL<maxR:
                L+=1
                maxL =max(maxL,height[L])
                diff = maxL - height[L]
                if diff>0:
                    volume +=diff
            else:
                R-=1
                maxR = max(maxR,height[R])
                diff = maxR - height[R]
                if diff >0:
                    volume +=diff
        return volume
