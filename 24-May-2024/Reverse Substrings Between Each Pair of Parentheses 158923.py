# Problem: Reverse Substrings Between Each Pair of Parentheses - https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/

class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for i in s:
            if i != ')':
                stack.append(i)
                continue
            temp = []
            while stack[-1] != '(':
                temp.append(stack.pop())
            stack.pop()
            stack.extend(temp)
        return ''.join(stack)