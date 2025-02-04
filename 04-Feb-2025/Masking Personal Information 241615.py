# Problem: Masking Personal Information - https://leetcode.com/problems/masking-personal-information/description/?envType=problem-list-v2&envId=string

class Solution:
    def maskPII(self, s: str) -> str:
        s = s.lower()
        s = s.split('@')
        if len(s) > 1:
            return f"{s[0][0]}*****{s[0][-1]}@{s[-1]}"
        temp = []
        for charcter in s[0]:
            if charcter.isnumeric():
                temp.append(charcter)
        s = ''.join(temp)
        if len(s) == 10:
            return f"***-***-{s[-4:]}"
        if len(s) == 11:
            return f"+*-***-***-{s[-4:]}"
        if len(s) == 12:
            return f"+**-***-***-{s[-4:]}"
        if len(s) == 13:
            return f"+***-***-***-{s[-4:]}"
