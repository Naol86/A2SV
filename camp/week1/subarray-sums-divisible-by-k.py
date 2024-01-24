class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        table = defaultdict(int)
        prefixSum = 0
        table[prefixSum] += 1
        ans = 0
        for i in nums:
            prefixSum += i
            ans += table[prefixSum % k]
            table[prefixSum % k] += 1
        return ans
            