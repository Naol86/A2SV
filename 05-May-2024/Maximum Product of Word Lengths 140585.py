# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        pro = []
        for word in words:
            _sum = 0
            bits = [0] * 26
            for i in word:
                temp = ord(i) - ord('a')
                if bits[temp] == 0:
                    _sum += 2 ** (temp)
                bits[temp] = 1
            pro.append((_sum, len(word)))

        _max = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if pro[i][0] | pro[j][0] == pro[i][0] + pro[j][0]:
                    _max = max(_max, pro[i][1] * pro[j][1])
        # print(pro)
        return _max
            