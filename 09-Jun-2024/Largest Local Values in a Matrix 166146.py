# Problem: Largest Local Values in a Matrix - https://leetcode.com/problems/largest-local-values-in-a-matrix/

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        ans = [[0] * (len(grid) - 2) for _ in range(len(grid) - 2)]
        counter = defaultdict(int)
        heap = []
        def right(i, j):
            for k in range(3):
                counter[grid[i+k][j]] -= 1
                if counter[grid[i+k][j]] == 0:
                    counter.pop(grid[i+k][j])
                    heap.remove(grid[i+k][j])
                if grid[i+k][j+3] not in counter:
                    heap.append(grid[i+k][j+3])
                counter[grid[i+k][j+3]] += 1
            ans[i][j+1] = max(heap)
        p = 0
        for i in range(len(grid) - 2):
            counter = defaultdict(int)
            heap = []
            for z in range(3):
                for j in range(3):
                    if grid[z+i][j] not in counter:
                        heap.append(grid[z+i][j])
                    counter[grid[z+i][j]] += 1
            ans[i][0] = max(heap)
            for j in range(len(grid) - 3):
                right(i, j)
        return ans