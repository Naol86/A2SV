class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        ans = float('inf')
        while left <= right:
            mid = left + (right - left) // 2
            # print(nums[mid])
            ans = min(ans, nums[mid])
            if nums[left] > nums[right] and nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        if ans == float('inf'):
            return -1
        return ans