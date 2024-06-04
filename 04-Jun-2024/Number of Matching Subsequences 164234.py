# Problem: Number of Matching Subsequences - https://leetcode.com/problems/number-of-matching-subsequences/

class TrieNode:
    def __init__(self):
        self.children = {}

class Solution:
    def __init__(self):
        self.root = TrieNode()
        self.cache = {}
    def insert(self, word):
        cur = self.root
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]
    
    def search(self, word):
        if word in self.cache:
            return self.cache[word]
        cur = self.root
        i = 0
        while i < len(word) and cur:
            if not cur.children:
                self.cache[word] = 0
                return 0
            if word[i] in cur.children:
                i += 1
            for x in cur.children:
                cur = cur.children[x]
        if i == len(word):
            self.cache[word] = 1
            return 1
        self.cache[word] = 0
        return 0
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        ans = 0
        self.insert(s)
        for word in words:
            ans += self.search(word)
        return ans