class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        nums = [0] + nums
        leng = len(nums)
        for i in range(1, leng):
            nums[i] = nums[i] + nums[i - 1]
        remi = nums[-1] % p
        if remi == 0:
            return 0
        _dict = {}
        ans = float('inf')
        for i in range(leng):
            temp = nums[i] % p
            if temp in _dict:
                ans = min(ans, i - _dict[temp])
            _dict[(remi + temp) % p] = i
        if ans == float('inf') or ans == leng - 1:
            return -1
        return ans
