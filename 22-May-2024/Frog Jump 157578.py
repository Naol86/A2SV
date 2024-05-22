# Problem: Frog Jump - https://leetcode.com/problems/frog-jump/

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        _set = set(stones)
        dp = defaultdict(set)
        dp[0].add(0)
        for stone in stones:
            for dis in dp[stone]:
                if dis > 0 and stone + dis in _set:
                    dp[stone + dis].add(dis)
                if dis > 1 and stone + dis - 1 in _set:
                    dp[stone + dis - 1].add(dis - 1)
                if stone + dis + 1 in _set:
                    dp[stone + dis + 1].add(dis + 1)
        return True if dp[stones[-1]] else False