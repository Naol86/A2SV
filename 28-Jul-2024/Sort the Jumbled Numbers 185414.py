# Problem: Sort the Jumbled Numbers - https://leetcode.com/problems/sort-the-jumbled-numbers/

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        """
        669, 007, 07
        """
        def change(number):
            x = []
            for i in str(number):
                x.append(str(mapping[int(i)]))
            return int(''.join(x))

        for i in range(len(nums)):
            nums[i] = [change(nums[i]), i, nums[i]]
        nums.sort()
        
        return [i[-1] for i in nums]
