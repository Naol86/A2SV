# Problem: Maximum XOR for Each Query - https://leetcode.com/problems/maximum-xor-for-each-query/

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        pre = nums[0]
        ans = [pre ^ ((1<<maximumBit) - 1)]
        for i in range(1, len(nums)):
            pre = pre ^ nums[i]
            ans.append(pre ^ ((1<<maximumBit) - 1))
        return ans[::-1]