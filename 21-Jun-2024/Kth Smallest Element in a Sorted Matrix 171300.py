# Problem: Kth Smallest Element in a Sorted Matrix - https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        heapq.heapify(heap)
        n = len(matrix)
        count = 0
        for i in range(n):
            for j in range(n):
                if count < k:
                    heapq.heappush(heap,-matrix[i][j])
                    count += 1
                elif heap[0] < - matrix[i][j]:
                    # print(heap)
                    heapq.heappop(heap)
                    heapq.heappush(heap, -matrix[i][j])
        return heap[0] * -1