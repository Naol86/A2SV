# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        _sum = 0
        leng = len(piles)
        for i in range(len(piles)):
            _sum += piles[i]
            piles[i] *= -1
        heapq.heapify(piles)
        # print(heapq.heappop(piles))
        while k > 0 and piles:
            num = heapq.heappop(piles)
            x = num//2
            heapq.heappush(piles, x)
            k -= 1
            _sum += (num - x)
            if _sum == leng:
                return _sum
        return _sum