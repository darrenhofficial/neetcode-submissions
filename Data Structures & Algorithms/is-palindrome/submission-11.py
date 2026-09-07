class Solution:
    def isPalindrome(self, s: str) -> bool:
        pal = []
        for i in s:
            if i.isalnum():
                pal.append(i.lower())
        return pal == pal[::-1]
