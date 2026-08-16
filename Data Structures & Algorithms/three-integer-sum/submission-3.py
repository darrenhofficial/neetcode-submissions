class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        length = len(nums)
        output = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            L = i+1
            R = length - 1
            target = 0 - nums[i]
            while L < R:
                curr_sum = nums[L] + nums[R]
                if curr_sum < target:
                    L+=1
                elif curr_sum > target:
                    R-=1
                else:
                    output.append([nums[i], nums[L], nums[R]])
                    while L<R and nums[L] == nums[L+1]:
                        L+=1
                    while L<R and nums[R] == nums[R-1]:
                        R-=1
                    L+=1
                    R-=1

        return output
            
