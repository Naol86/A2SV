class Solution:
    def __init__(self):
        self.order_dic = {}

    def check(self, word1, word2):
        leng = min(len(word1),len(word2))
        for i in range(leng):
            if self.order_dic[word1[i]] < self.order_dic[word2[i]]:
                return True
            elif self.order_dic[word1[i]] > self.order_dic[word2[i]]:
                return False
        if len(word1) > len(word2):
            return False
        return True

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) == 1:
            return True
        for i in range(len(order)):
            self.order_dic[order[i]] = i
        
        for i in range(len(words)-1):
            if not self.check(words[i], words[i+1]):
                return False
        return True

        
