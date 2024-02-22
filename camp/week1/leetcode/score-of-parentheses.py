class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for i in s:
            if i == '(':
                stack.append('(')
            else:
                if stack[-1] == '(':
                    stack.pop()
                    if stack[-1] not in ('(', ')'):
                        stack[-1] += 1
                    else:
                        stack.append(1)
                else:
                    a = stack.pop() * 2
                    stack.pop()
                    if stack[-1] not in ('(', ')'):
                        stack[-1] += a
                    else:
                        stack.append(a)
        return stack[-1]