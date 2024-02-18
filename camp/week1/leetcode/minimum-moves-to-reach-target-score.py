class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count = 0
        while maxDoubles > 0 and target > 1:
            if target % 2 != 0:
                count += 1
            target //= 2
            maxDoubles -= 1
            count += 1
        return count + target - 1