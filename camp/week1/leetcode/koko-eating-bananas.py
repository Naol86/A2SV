class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = -float('inf')
        for i in piles:
            # left = min(left, i)
            right = max(right, i)
        # print(left, right)
        def find(i, cap, hour):
            # print(hour)
            if hour < 0:
                return False
            if i == len(piles):
                return True
            if piles[i] % cap == 0:
                return find(i + 1, cap, hour - piles[i] // cap)
            take = piles[i] // cap + 1
            return find(i + 1, cap, hour - take)
            
        ans = right
        while left <= right:
            mid = left + (right - left) // 2
            if find(0, mid, h):
                # print(mid)
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans