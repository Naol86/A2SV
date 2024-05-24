# Problem: Replace Words - https://leetcode.com/problems/replace-words/

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}

class Solution:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        cur = self.root
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]
        cur.is_end = True
    
    def search(self, word):
        cur = self.root
        temp = []
        for w in word:
            if cur.is_end:
                return ''.join(temp)
            if w not in cur.children:
                return word
            temp.append(w)
            cur = cur.children[w]
        return word

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        for word in dictionary:
            self.insert(word)
        ans = []
        for word in sentence.split():
            ans.append(self.search(word))
        return ' '.join(ans)