class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        _min = nums[0]
        
        for num in nums[1:]:
            while stack and stack[-1][0] <= num:
                stack.pop()
            if stack and stack[-1][0] > num and stack[-1][1] < num:
                return True
            stack.append((num, _min))
            _min = min(_min, num)
        return False