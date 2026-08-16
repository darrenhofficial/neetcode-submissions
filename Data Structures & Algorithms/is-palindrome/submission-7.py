class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1=""
        for i in s:
            if  i.isnumeric() or i.isalpha():
                s1+=i
        s1=s1.upper()
        d=0
        u=len(s1)-1
        while d<u:
            if s1[d] != s1[u]:
                return False
            d+=1
            u=u-1
        return True