class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        the_set = set()
        L =0
        highest_count = 0
        for R in range(len(s)):
            while s[R] in the_set:
                the_set.remove(s[L])
                L+=1
            the_set.add(s[R])
            highest_count = max(highest_count,R-L+1)
        return highest_count
        