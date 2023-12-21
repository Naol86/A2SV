class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        _sum = 0
        for i in nums:
            if i % 2 == 0:
                _sum += i
        ans = []
        for i in queries:
            if nums[i[1]] % 2 == 0:
                _sum -= nums[i[1]]
                nums[i[1]] += i[0]
            else:
                nums[i[1]] += i[0]
            
            if nums[i[1]] % 2 == 0:
                _sum += nums[i[1]]
            ans.append(_sum)
        return ans