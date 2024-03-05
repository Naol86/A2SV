class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1] # track where each element is small
        heights.append(-1)
        leng = len(heights)
        lis = [1] * leng
        for i in range(leng):
            while len(stack) > 1 and heights[stack[-1]] > heights[i]:
                poped = stack.pop()
                lis[poped] = i - stack[-1] - 1
            stack.append(i)
        # print(lis)
        # print(stack)
        _max = 0
        for i in range(leng - 1):
            _max = max(_max, lis[i] * heights[i])
        return _max