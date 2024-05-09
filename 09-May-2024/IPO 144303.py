# Problem: IPO - https://leetcode.com/problems/ipo/

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        lis = []
        for i in range(len(capital)):
            lis.append((capital[i], -profits[i]))
        lis.sort()
        heap = []
        i = 0
        while k > 0:
            while i < len(lis) and lis[i][0] <= w:
                heapq.heappush(heap, lis[i][1])
                i += 1
            if heap:
                pop = heapq.heappop(heap)
                w -= pop
            k -= 1
        return w