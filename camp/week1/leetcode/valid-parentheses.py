class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hash_map = {')':'(', ']':'[', '}':'{'}  
        for i in s:
            if len(stack) < 1 or i not in hash_map:
                stack.append(i)
            elif hash_map[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
        if stack:
            return False
        return True