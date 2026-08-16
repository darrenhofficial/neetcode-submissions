class Solution:

    def encode(self, strs: List[str]) -> str:
        parts = []
        for s in strs:
            parts.append(f"{len(s)}#{s}")
        return "".join(parts)


    def decode(self, s: str) -> List[str]:
        res = []
        start = 0
        while start < len(s):
            end = start
            while s[end] != "#":
                end += 1

            length = int(s[start:end])
            word = s[end + 1 : end + 1 + length]
            res.append(word)

        # 核心修改：指针跳到下一个数字的开头
            start = end + 1 + length
        return res