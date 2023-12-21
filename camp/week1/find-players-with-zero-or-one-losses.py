from collections import defaultdict
# from collections import SortedSet
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        dic = defaultdict(int)
        for i, j in matches:
            dic[j] += 1
            dic[i]
        left = []
        right = []
        for i, j in dic.items():
            if j == 0:
                left.append(i)
            elif j == 1:
                right.append(i)
        left.sort()
        right.sort()
        return [left, right]