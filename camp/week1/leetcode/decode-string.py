class Solution:
    def decodeString(self, s: str) -> str:
        indices = []
        opens = 0
        closes = 0
        n = len(s)
        for i in range(n):
            if s[i] == ']':
                closes += 1
                if opens == closes:
                    indices.append(i)
            elif s[i] == '[':
                opens += 1
        def solve(substr):
            if substr.count("]") == 0:
                return substr
            m = len(substr)
            i = 0
            alpha = []
            dig = ['0']
            while i < m and substr[i].isalpha():
                alpha.append(substr[i])
                i += 1
            while substr[i].isdigit():
                dig.append(substr[i])
                i += 1
            #print(dig, alpha)
            return "".join(alpha) + int("".join(dig))* self.decodeString(substr[i+1:-1])
        #print(solve("ab3[d3[aa]]"))
        ans = []
        prev = 0
        for i in indices:
            substr = solve(s[prev:i+1])
            ans.append(substr)
            prev = i+1
        ans.append(solve(s[prev:]))
        return "".join(ans)
            