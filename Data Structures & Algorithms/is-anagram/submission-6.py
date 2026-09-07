class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict
        if len(s)!=len(t):
            return False
        s_dict , t_dict = defaultdict(int) , defaultdict(int)
        for i in range(len(s)):
            s_dict[s[i]] +=1
            t_dict[t[i]] +=1
        for key in s_dict:
            if s_dict[key] != t_dict[key]:
                return False
        return True