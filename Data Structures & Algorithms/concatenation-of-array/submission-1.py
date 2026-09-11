class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        following = nums
        ans = following + nums
        return ans