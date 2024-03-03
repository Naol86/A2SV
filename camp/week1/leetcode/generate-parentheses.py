class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        temp = ['(']
        def helper(open, close):
            if close == 0:
                ans.append(''.join(temp))
                return
            if open > 0:
                temp.append('(')
                helper(open - 1, close)
                temp.pop()

                if open < close:

                    temp.append(')')
                    helper(open, close - 1)
                    temp.pop()

            else:
                temp.append(')')
                helper(open, close - 1)
                temp.pop()
        helper(n - 1, n)
        return ans