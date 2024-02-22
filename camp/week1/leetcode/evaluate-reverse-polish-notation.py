class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ans = 0
        oparend = {'-', '+', '*', '/'}
        for i in tokens:
            if i not in oparend:
                stack.append(int(i))
                continue
            a = stack.pop()
            b = stack.pop()
            if i == '+':
                ans = (a + b)
                stack.append(ans)
            elif i == '-':
                ans = (b - a)
                stack.append(ans)
            elif i == '*':
                ans = (a * b)
                stack.append(ans)
            elif i == '/':
                temp = b / a
                if temp >= 0:
                    stack.append(int(temp))
                else:
                    stack.append(ceil(temp))
        return stack[-1]