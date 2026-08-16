class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() #O(n*log(n)) time

        res = []
        for i in range(len(nums)-1):
            sumVal = - nums[i]
            left = i + 1
            right = len(nums) - 1
            while (left != right):
                if(nums[left]+nums[right] == sumVal):
                    if [nums[i],nums[left],nums[right]] not in res: res.append([nums[i],nums[left],nums[right]])
                    right -= 1 
                    continue
                if(nums[left]+nums[right] > sumVal):
                    right -= 1
                else:
                    left += 1
        return res
