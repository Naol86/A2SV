# Problem: Minimum Number of Operations to Make Array XOR Equal to K - https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        x = nums[0]
        for i in nums[1:]:
            x ^= i
        # print(bin(k))
        # print(bin(x))
        count = 0
        while k > 0 or x > 0:
            if k & 1 != x & 1:
                count += 1
            k >>= 1
            x >>= 1
        return count