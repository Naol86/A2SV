# Problem: Search Suggestions System - https://leetcode.com/problems/search-suggestions-system/

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False

class Solution:
    def __init__(self):
        self.root = TrieNode()
        self.pos = []
        self.place = self.root

    def insert(self, word):
        cur = self.root
        for w in word:
            index = ord(w) - ord('a')
            if not cur.children[index]:
                cur.children[index] = TrieNode()
            cur = cur.children[index]
        cur.is_end = True

    def search(self, w):
        if self.place and self.place.children[ord(w) - ord('a')]:
            self.place = self.place.children[ord(w) - ord('a')]
            self.pos.append(w)
        else:
            self.place = None
        temp = self.pos.copy()
        ans = []
        cur = self.place
        def find(cur):
            if len(ans) == 3 or not cur:
                return
            if cur.is_end:
                ans.append(''.join(temp))
                # return
            for i in range(26):
                if cur.children[i]:
                    temp.append(chr(ord('a') + i))
                    find(cur.children[i])
                    temp.pop()
        find(cur)
        return ans

    
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        for word in products:
            self.insert(word)
        ans = []
        for s in searchWord:
            ans.append(self.search(s))
        return ans
        