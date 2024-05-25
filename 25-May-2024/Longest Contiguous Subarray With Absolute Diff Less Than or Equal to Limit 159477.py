# Problem: Longest Contiguous Subarray With Absolute Diff Less Than or Equal to Limit - https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        _max = 0
        min_stack = deque()
        max_stack = deque()
        queue = deque()
        i = 0
        while i < len(nums):
            while min_stack and min_stack[-1] > nums[i]:
                min_stack.pop()
            min_stack.append(nums[i])
            while max_stack and max_stack[-1] < nums[i]:
                max_stack.pop()
            max_stack.append(nums[i])
            while (max_stack and min_stack) and not (max_stack[0] - min_stack[0] <= limit):
                x = queue.popleft()
                if x == max_stack[0]:
                    max_stack.popleft()
                if x == min_stack[0]:
                    min_stack.popleft()
            queue.append(nums[i])
            i += 1
            _max = max(_max, len(queue))
        return _max