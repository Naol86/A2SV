class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open = 0
        count = 0
        for i in s:
            if i == "(":
                open += 1
            else:
                if open > 0:
                    open -= 1
                else:
                    count += 1
        return count + open