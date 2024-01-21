class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        leng = len(nums)
        lis = [0] * (leng + 1)
        for start, end in requests:
            lis[start] += 1
            lis[end+1] -= 1
        for i in range(1,leng+1):
            lis[i] = lis[i] + lis[i - 1]
        lis.pop()
        nums.sort(reverse=True)
        lis.sort(reverse=True)
        print(nums)
        print(lis)
        _sum = 0
        i = 0
        while i < leng and lis[i] > 0:
            _sum += (nums[i] * lis[i])
            i += 1
        return _sum % (10**9 + 7)