class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        the_map = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in the_map:
                return[the_map[diff],idx]
            the_map[num] = idx
            
