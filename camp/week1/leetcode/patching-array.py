class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        count = 0
        nums.append(n)
        comp = 1
        i = 0
        while i < len(nums) and nums[i] <= n:
            if nums[i] <= comp:
                comp += nums[i]
                i += 1
            else:
                comp += comp
                count += 1
        while comp <= n:
            comp += comp
            count += 1
        return count
