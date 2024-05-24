# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None for i in range(26)]

class Solution:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        cur = self.root
        for w in word:
            if not cur.children[ord(w) - ord('a')]:
                cur.children[ord(w) - ord('a')] = TrieNode()
            cur = cur.children[ord(w) - ord('a')]
            
        cur.is_end = True

    def longestWord(self, words: List[str]) -> str:
        for word in words:
            self.insert(word)
        cur = self.root
        temp = []
        ans = ['']
        def dfs(cur):
            if not cur:
                return
            for i in range(26):
                if cur.children[i] and cur.children[i].is_end:
                    temp.append(chr(ord('a') + i))
                    if len(ans[0]) <= len(temp):
                        s = ''.join(temp)
                        if len(ans[0]) == len(temp):
                            ans[0] = min(ans[0], s)
                        else:
                            ans[0] = s
                    dfs(cur.children[i])
                    temp.pop()

        dfs(cur)

        return ans[0]

        