class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        spaces = [0] + spaces + [3 * (10**5) + 10]
        ans = ""
        for i in range(len(spaces)-1):
            ans += s[spaces[i]:spaces[i+1]] + " "
        return ans.rstrip()
            