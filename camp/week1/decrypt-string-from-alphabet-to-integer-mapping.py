class Solution:
    def freqAlphabets(self, s: str) -> str:
        ans = ""
        i = 0
        leng = len(s)
        while i + 2 < leng:
            if s[i+2] == "#":
                ans += chr(ord('a') + int(s[i:i+2]) - 1)
                i += 3
            else:
                ans += chr(ord('a') + int(s[i]) - 1)
                i+=1
        while i < leng:
            ans += chr(ord('a') + int(s[i]) - 1)
            i+=1
        return ans