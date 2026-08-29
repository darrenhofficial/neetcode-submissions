class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        upper = max(piles)
        res = upper
        lower =1
        while lower <= upper:
            mid = (lower + upper) //2
            loc_count = 0
            hr = 0
            for p in piles:
                hr += math.ceil(p/mid)
            if hr <=h:
                res = mid
                upper = mid -1
            else:
                lower = mid +1
        return res