class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        _sum = sum(nums)
        leng = len(nums)
        _arth = (leng/2)*(1+leng)
        ans = _arth - _sum
        return int(ans)