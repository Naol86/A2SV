class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for i in range(left, right + 1):
            for j,k in ranges:
                if i >= j and i <= k:
                    break
            else:
                return False
        return True