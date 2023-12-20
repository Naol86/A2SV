class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return True
        nums.append(10**5 + 2)
        check = True
        if nums[0] > nums[1]:
            check = False
            nums = nums[1:]
        i = 0
        while i < len(nums) - 2:
            if nums[i] > nums[i+1]:
                if not check:
                    return False
                check = False
                if nums[i] < nums[i+2]:
                    nums.pop(i+1)
                else:
                    nums.pop(i)
                i -= 1
                continue
            i+=1
        return True