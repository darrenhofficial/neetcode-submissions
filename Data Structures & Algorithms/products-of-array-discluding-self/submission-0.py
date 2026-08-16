class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        output = [1]*N
        prefix = 1
        postfix = 1
        for i in range(N):
            output[i] = prefix
            prefix *= nums[i]
        for i in range(N-1,-1,-1):
            output[i] *= postfix
            postfix *= nums[i]
        return output
