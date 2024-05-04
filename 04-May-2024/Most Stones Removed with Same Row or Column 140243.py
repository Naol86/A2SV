# Problem: Most Stones Removed with Same Row or Column - https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        row_parent = defaultdict(int)
        row_size = defaultdict(int)

        def find(x):
            if x not in row_parent:
                row_parent[x] = x
                row_size[x] += 1
            if x == row_parent[x]:
                return x
            row_parent[x] = find(row_parent[x])
            return row_parent[x]
        
        def union(x, y):
            par_x = find(x)
            par_y = find(y)
            if par_x != par_y:
                if row_size[par_x] > row_size[par_y]:
                    row_parent[par_y] = par_x
                    row_size[par_x] += row_size[par_y]
                else:
                    row_parent[par_x] = par_y
                    row_size[par_y] += row_size[par_x]
        
        # union rows
        for row, col in stones:
            if row in row_parent:
                union(row, row_parent[row])
            else:
                find(row)
        
        # the second union with colomun
        col_parent = defaultdict(int)
        for row, col in stones:
            if col in col_parent:
                union(row, col_parent[col])
            col_parent[col] = find(row)
        
        count_par = set()
        for row, col in stones:
            count_par.add(find(row))
        
        # print(row_parent)
        
        return len(stones) - len(count_par)