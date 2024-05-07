# Problem: Single Number III - https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num
        # print(xor,bin(xor))
        i = 0
        while xor != 0:
            if xor & 1:
                break
            i += 1
            xor >>= 1
        # print(i)
        ans = [0,0]
        for num in nums:
            if num & (1<<i):
                ans[1] ^= num
            else:
                ans[0] ^= num
        return ans