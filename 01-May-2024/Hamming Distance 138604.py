# Problem: Hamming Distance - https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x ^= y
        count = 0
        while x > 0:
            if x & 1:
                count += 1
            x >>= 1
        return count