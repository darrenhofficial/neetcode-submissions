class Solution:
    def isValid(self, s: str) -> bool:
        open_stack = []
        closetoopen ={")":"(","]":"[","}":"{"}
        for char in s:
            if char in closetoopen:
                if open_stack and open_stack[-1] == closetoopen[char]:
                    open_stack.pop()
                else:
                    return False
            else:
                open_stack.append(char)
        return len(open_stack) ==0