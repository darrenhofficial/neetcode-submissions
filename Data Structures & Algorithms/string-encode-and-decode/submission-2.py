class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for i in strs:
            string += str(len(i)) + "#" + i
        
        return string
    def decode(self, s: str) -> List[str]:
        the_list = []
        start_idx = 0
        while start_idx < len(s):
            end_idx = start_idx
            while s[end_idx]!= "#":
                end_idx +=1
            length = int(s[start_idx:end_idx])
            the_list.append(s[end_idx + 1: end_idx + 1 + length])
            start_idx = length+ 1 + end_idx
        return the_list