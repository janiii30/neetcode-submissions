class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()
        minutes, fresh = 0, 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh +=1

        while fresh> 0 and q:
            l = len(q)

            for i in range(l):
                r,c = q.popleft()

                for dr, dc in directions:
                    row, col = r+dr, c+dc
                    if(row in range(rows) and col in range(cols) and grid[row][col]==1):
                        grid[row][col] = 2
                        fresh -= 1
                        q.append((row,col))

            minutes +=1


        return minutes if fresh == 0 else -1

