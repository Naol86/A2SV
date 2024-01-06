class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = float('inf')
        leng = len(nums)
        for i in range(leng):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = leng - 1
            while left < right:
                temp = nums[i] + nums[left] + nums[right]
                ans = temp if abs(target - temp) < abs(ans-target) else ans
                # print(nums[i],nums[left],nums[right],ans)
                if nums[i] + nums[left] + nums[right] > target:
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < target:
                    left += 1
                else:
                    # ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        return ans