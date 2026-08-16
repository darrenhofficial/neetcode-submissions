class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set =set(nums)
        start  = []
        output =0
        for i in nums_set:
            if i-1 not in nums_set:
                start = i
                count = 1
                while start + 1 in nums_set :
                    start +=1
                    count +=1
                output = max(output,count)
        return output