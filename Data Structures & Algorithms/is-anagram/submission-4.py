class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sdirt = {}
        tdirt = {}
        for i in s:
            sdirt[i] = sdirt.get(i,0) + 1
        for i in t:
            tdirt[i] = tdirt.get(i,0) + 1 
        return sdirt == tdirt