class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        if k == len(nums):
            return max(nums)
        if k == 1:
            return sum(nums)
        prefix = [nums[0]]
        left = nums[0]
        right = nums[0]
        for i in range(1, len(nums)):
            left = max(left, nums[i])
            prefix.append(prefix[-1] + nums[i])
        right = prefix[-1]
        # print(prefix)

        def partition(mid, pre, subs):
            r = bisect.bisect_right(prefix, mid + pre)
            if r == len(prefix):
                return 1
            return 1 + partition(mid, prefix[r - 1] + pre - subs, prefix[r - 1])

        _min = float('inf')
        while left <= right:
            mid = left + (right - left) // 2
            x = partition(mid, 0, 0)
            # print(x, mid)
            if x <= k:
                _min = min(_min, mid)
                right = mid - 1
            else:
                left = mid + 1
        return _min