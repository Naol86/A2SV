from collections import Counter
class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        numbers = defaultdict(set)
        dont_care = set([])
        leng = len(fronts)
        for i in range(leng):
            if fronts[i] not in dont_care:
                numbers[fronts[i]].add(i)
        # for i in range(leng):
            if backs[i] in dont_care:
                continue
            elif backs[i] in numbers:
                if i in numbers[backs[i]]:
                    dont_care.add(backs[i])
                    numbers.pop(backs[i])
            else:
                numbers[backs[i]].add(i)
        lis = list(numbers.keys())
        if len(lis) == 0:
            return 0
        lis.sort()
        # print(lis)
        return lis[0]