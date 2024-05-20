# Problem: Combination Sum IV - https://leetcode.com/problems/combination-sum-iv/description/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # cache = {}
        # def cal(left):
        #     if left == 0:
        #         return 1
        #     if left < 0:
        #         return 0
        #     if left in cache:
        #         return cache[left]
        #     temp = 0
        #     for num in nums:
        #         temp += cal(left - num)
        #     cache[left] = temp
        #     return temp
        # ans = cal(target)
        # # print(cache)
        # return ans
        dp = [0] * (target + 1)
        dp[0] = 1
        for amount in range(1,target+1):
            temp = 0
            for num in nums:
                if num <= amount:
                    temp += dp[amount - num]
            dp[amount] = temp
        return dp[-1]