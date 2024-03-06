class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if len(weights) == k:
            return 0
        lis = []
        for i in range(1, len(weights)):
            lis.append(weights[i- 1] + weights[i])
        lis.sort()
        print(lis)
        ans = 0
        for i in range(1, k):
            ans += lis[-i] - lis[i - 1]
        return ans
