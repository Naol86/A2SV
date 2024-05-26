# Problem: Flood Fill - https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        def inbound(row,col):
            return (0 <= row and row < len(image) ) and (0<=col and col < len(image[0]))
        visited = set()
        def dfs(row,col,prev_color):
            if not inbound(row,col) or image[row][col] != prev_color:
                return 
            image[row][col] = color
            visited.add((row,col))
            for r,c in directions:
                new_row,new_col = row+r,col+c
                if not (new_row,new_col) in visited:
                    dfs(new_row,new_col,prev_color)
        pre = image[sr][sc]
        dfs(sr,sc,pre)
        return image