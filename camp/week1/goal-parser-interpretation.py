class Solution:
    def interpret(self, command: str) -> str:
        ans = ""
        i = 0
        while i < len(command):
            if command[i] == "(" and command[i+1] == 'a':
                ans += "al"
                i += 4
            elif command[i] == '(':
                ans += 'o'
                i+=2
            else:
                ans += command[i]
                i += 1
        return ans
