class Solution:
    def isPalindrome(self, s: str) -> bool:
        filter_s = ""
        for element in s:
            if element.isalnum():
                filter_s += element.lower()
        print(filter_s)
        L = 0
        R = len(filter_s)-1
        while L<R:
            if filter_s[L] != filter_s[R]:
                return False
            L +=1
            R -=1
        return True
