# Problem: Single Number II - https://leetcode.com/problems/single-number-ii/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = [0] * 33
        for num in nums:
            if num < 0:
                ans[-1] += 1
                num = -num
            for i in range(num.bit_length()):
                if num & 1:
                    ans[i] += 1
                num >>= 1
        # print(ans)
        temp = 0
        for i in range(32):
            if ans[i] % 3:
                temp += 2 ** i
        if ans[-1] % 3:
            temp *= -1 
        return temp
        