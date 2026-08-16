class Solution:

    def encode(self, strs: List[str]) -> str:
        # 用普通字符串连接代替 f-string 格式化，在 Python 解释器中开销更小
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        the_list = []
        start_idx = 0
        n = len(s)

        while start_idx < n:
            # index() 比 find() 稍快一些
            end_idx = s.index("#", start_idx)

            length = int(s[start_idx:end_idx])

            the_list.append(s[end_idx + 1 : end_idx + 1 + length])

            start_idx = end_idx + 1 + length

        return the_list