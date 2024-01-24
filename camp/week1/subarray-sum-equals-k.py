class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        table = defaultdict(int)
        prefixSum = 0
        table[prefixSum] += 1
        ans = 0
        for i in nums:
            prefixSum += i
            if (prefixSum - k) in table:
                ans += table[prefixSum - k]
            table[prefixSum] += 1
        return ans