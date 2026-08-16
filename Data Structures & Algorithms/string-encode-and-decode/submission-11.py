class Solution:

    def encode(self, strs: List[str]) -> str:
        parts = []
        for s in strs:
            parts.append(f"{len(s)}#{s}")
        return "".join(parts)


    def decode(self, s: str) -> List[str]:
        the_list = []
        start_idx = 0
        n = len(s)

        while start_idx < n:
            # 用内置的 .find() 代替手写 while 循环寻找 '#'，C底层执行极快
            end_idx = s.find("#", start_idx)

            length = int(s[start_idx:end_idx])

            # 截取单词
            the_list.append(s[end_idx + 1 : end_idx + 1 + length])

            # 跳到下一个单词的数字开头
            start_idx = end_idx + 1 + length

        return the_list