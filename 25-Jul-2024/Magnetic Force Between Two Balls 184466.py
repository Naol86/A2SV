# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        # print(position)
        def check(mid):
            i = 0
            x = position[i]
            k = m - 1
            while i < len(position) - 1 and k > 0:
                 index = bisect.bisect_right(position, position[i] + mid - 1)
                 if index != len(position):
                    k -= 1
                 i = index
            return k == 0
        
        left = 1
        right = position[-1] - position[0]
        ans = 0

        while left <= right:
            mid = left + (right - left)//2
            if check(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans