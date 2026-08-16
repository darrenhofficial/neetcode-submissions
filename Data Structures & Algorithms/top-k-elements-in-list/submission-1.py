from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_freq = defaultdict(int)
        output = []
        for i in nums:
            nums_freq[i] +=1 
        j = 0
        while j <k:
            the_adding  = max(nums_freq,key = nums_freq.get)
            output.append(the_adding)
            nums_freq.pop(the_adding)
            j+=1
        return output