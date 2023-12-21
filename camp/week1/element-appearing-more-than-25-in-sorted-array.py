class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr) * 0.25
        dic = defaultdict(int)
        for i in arr:
            dic[i] += 1
            if dic[i] > n:
                return i