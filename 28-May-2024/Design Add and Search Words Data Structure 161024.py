# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]
        cur.is_end = True

    def find(self, cur, j):
        for x in cur.children:
            temp = self.search_na(cur.children[x], j + 1)
            if temp:
                return True
        return False
    def search_na(self, cur, j):
        word = self.word
        for i in range(j, len(word)):
            if not cur:
                return False
            w = word[i]
            if w == '.':
                return self.find(cur, i)
            if w not in cur.children:
                return False
            cur = cur.children[w]
        if cur.is_end:
            return True
        return False
    
    def search(self, word: str) -> bool:
        self.word = word
        cur = self.root
        return self.search_na(cur, 0)




        

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)