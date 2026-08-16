class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res += str(len(i))+"#"+i
        return res


    def decode(self, s: str) -> List[str]:
        res = []
        start = 0 
        while start < len(s):
            end = start
            while s[end] !="#":
                end +=1
            length = int(s[start:end])
            word = s[end+1:end+1+length]
            res.append(word)
            start = end+1+length 
        return res
