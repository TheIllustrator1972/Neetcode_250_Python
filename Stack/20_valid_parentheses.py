class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {']':'[','}':'{',')':'('}

        for char in s:
            if stack and char in "]})":
                if stack[-1] != closeToOpen[char]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(char)
        
        return len(stack) == 0
