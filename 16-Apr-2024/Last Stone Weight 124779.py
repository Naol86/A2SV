# Problem: Last Stone Weight - https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1
        heapq.heapify(stones)
        while stones:
            y = heapq.heappop(stones)
            if not stones:
                return -y
            x = heapq.heappop(stones)
            y -= x
            if y:
                heapq.heappush(stones, y)
        return 0