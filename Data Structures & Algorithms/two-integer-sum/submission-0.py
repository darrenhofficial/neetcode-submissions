class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        the_map = {}
        for i in range(len(nums)):
            the_map[nums[i]] = i
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in the_map and idx != the_map[diff]:
                return [idx, the_map[diff]]
            
