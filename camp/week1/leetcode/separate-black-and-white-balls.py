class Solution:
    def minimumSteps(self, s: str) -> int:
        count = 0
        size = 0
        for i in s:
            if i == "1":
                size += 1
            else:
                count += size
        return count