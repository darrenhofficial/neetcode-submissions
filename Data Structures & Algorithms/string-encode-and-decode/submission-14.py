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
            # index() 比 find() 稍快一些
            end_idx = s.index("#", start_idx)

            length = int(s[start_idx:end_idx])

            the_list.append(s[end_idx + 1 : end_idx + 1 + length])

            start_idx = end_idx + 1 + length

        return the_list
