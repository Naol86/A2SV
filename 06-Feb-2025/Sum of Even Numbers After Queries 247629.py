# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        _sum = 0
        for num in nums:
            if (num % 2) == 0:
                _sum += num
        ans = []
        for val, index in queries:
            temp = nums[index]
            nums[index] += val
            if nums[index] % 2 == 0:
                _sum += nums[index]
            if not temp % 2:
                _sum -= temp
            ans.append(_sum)
        return ans