class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = [(-1, -1)]
        arr.append(0)
        answer = 0
        for index, val in enumerate(arr):
            while stack[-1][0] > val:
                answer += (stack[-1][1] - stack[-2][1]) * (index - stack[-1][1]) * stack[-1][0]
                stack.pop()
            stack.append((val, index))
        return answer % (10 ** 9 + 7)
