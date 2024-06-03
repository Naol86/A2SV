# Problem: Array With Elements Not Equal to Average of Neighbors - https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = []
        left = 0
        right = len(nums) - 1
        while left <= right:
            if left == right:
                ans.append(nums[left])
                break
            ans.append(nums[left])
            ans.append(nums[right])
            left += 1
            right -= 1
        return ans