class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        path = set()

        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c):
            path.add((r, c))

            for dr, dc in direction:
                nr, nc = r + dr, c + dc

                if nr >= 0 and nr < ROWS and\
                    nc >= 0 and nc < COLS and\
                    grid[nr][nc] == "1" and\
                    (nr, nc) not in path:
                    dfs(nr, nc)

            
        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in path:
                    dfs(r, c)
                    islands += 1

        return islands