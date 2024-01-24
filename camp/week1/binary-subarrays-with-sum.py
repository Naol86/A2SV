class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        table = defaultdict(int)
        prefixSum = 0
        table[prefixSum] += 1
        ans = 0
        for i in nums:
            prefixSum += i
            ans += table[prefixSum - goal]
            table[prefixSum] += 1
        return ans