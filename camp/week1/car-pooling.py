class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        _max = -float('inf')
        for i, j, k in trips:
            if i > capacity:
                return False
            _max = max(_max, k)
        lis = [0] * (_max + 2)
        for i, j, k in trips:
            lis[j] += i
            lis[k] -= i
        for i in range(1,_max+1):
            lis[i] = lis[i] + lis[i - 1]
            if lis[i] > capacity:
                return False
        return True