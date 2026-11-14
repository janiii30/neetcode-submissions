class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        rows, cols = len(grid), len(grid[0])
        max_area = 0


        def dfs(i,j):
            global max_area
            if i<0 or i>=rows or j<0 or j>=cols or grid[i][j]==0:
                return 0

            grid[i][j]=0
            area = 1
            for dr, dc in directions:
                area += dfs(i + dr, j + dc)
            return area


        for r in range(rows):
            for c in range(cols):
                max_area = max(max_area,dfs(r,c))

        return max_area