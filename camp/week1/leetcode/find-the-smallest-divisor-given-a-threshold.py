class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def _sum(div):
            x = 0
            for num in nums:
                x += ceil(num / div)
            return x
        left = 1
        right = max(nums)
        ans = right
        while left <= right:
            mid = left + (right - left) // 2
            if _sum(mid) <= threshold:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans