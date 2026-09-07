class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        the_dict = {}
        for idx,num in enumerate(nums):
            remaining = target - num
            if remaining in the_dict:
                return [the_dict[remaining],idx]
            else:
                the_dict[num] = idx