class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        rows, cols = len(board), len(board[0])

        seen = set()
        def dfs(i,j,w):
            if w == len(word):
                return True
                
            if (i < 0 or i >= rows or 
                j < 0 or j >= cols or 
                board[i][j] != word[w] or 
                (i, j) in seen):
                return False

            seen.add((i, j))

            for dr, dc in directions:
                if dfs(i + dr, j + dc, w + 1):
                    return True  
            
            seen.remove((i, j))
            
            return False

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r,c,0):
                        return True
        
        return False