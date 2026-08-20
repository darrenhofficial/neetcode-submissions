class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26 
        L = 0
        max_freq = 0

        for R in range(len(s)):
            
            idx = ord(s[R]) - 65  # 65 ASCII of 'A' is 65
            count[idx] += 1

            if count[idx] > max_freq:
                max_freq = count[idx]

            if (R - L + 1) - max_freq > k:
                count[ord(s[L]) - 65] -= 1
                L += 1

        return len(s) - L
