from collections import Counter
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = Counter(arr1)
        ans = []
        for i in arr2:
            ans += [i] * count[i]
            count[i] = 0
        temp = []
        for i in count:
            if count[i] != 0:
                temp += [i] * count[i]
        temp.sort()
        return ans + temp