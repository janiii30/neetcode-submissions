class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        islands = 0
        rows = len(grid)
        columns = len(grid[0])

        def dfs(i,j):
            if i<0 or i>=rows or j<0 or j>=columns or grid[i][j]=="0":
                return

            grid[i][j] = "0"
            for dr,dc in directions:
                dfs(i+dr,j+dc)

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == "1":
                    dfs(r,c)
                    islands += 1

        return islands