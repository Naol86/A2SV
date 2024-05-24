# Problem: Backspace String Compare
(Easy) - https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        T = []
        for i in t:
            if i == '#':
                if T:
                    T.pop()
            else:
                T.append(i)
        S = []
        for i in s:
            if i == '#':
                if S:
                    S.pop()
            else:
                S.append(i)
        return S == T