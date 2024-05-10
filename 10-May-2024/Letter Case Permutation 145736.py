# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        letters = []
        for i in range(len(s)):
            if s[i].isalpha():
                letters.append(s[i].lower())
            else:
                letters.append(s[i])
        # print(letters)
        visited = [0]
        for i in range(len(s)):
            if not s[i].isalpha():
                visited[0] += (1<<i)
        # print(visited)
        ans = [''.join(letters)]
        def back_tracking(i):
            if i > len(s):
                return
            for j in range(i, len(s)):
                if visited[0] & (1<<j):
                    continue
                visited[0] ^= (1<<j)
                letters[j] = letters[j].upper()
                ans.append(''.join(letters))
                back_tracking(j + 1)
                letters[j] = letters[j].lower()
                visited[0] ^= (1<<j)
        back_tracking(0)
        return ans