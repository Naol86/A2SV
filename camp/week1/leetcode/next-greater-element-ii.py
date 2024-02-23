class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = [-1] * len(nums)
        i = 0
        stack = []
        count = 0
        leng = len(ans)
        while i < 2 * leng:
            if not stack:
                stack.append(i%leng)
            else:
                while stack and nums[stack[-1]] < nums[i%leng]:
                    x = stack.pop()
                    ans[x] = nums[i%leng]
                stack.append(i%leng)
            i += 1
        # print(count)
        return ans