class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min = len(word1) if len(word1) <len(word2) else len(word2)
        count = 0
        ans = ""
        while min > count:
            ans += word1[count]
            ans += word2[count]
            count+=1
        ans += word1[count:]
        ans += word2[count:]
        return ans