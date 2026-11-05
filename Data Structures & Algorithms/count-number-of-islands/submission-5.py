class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        path = set()

        def dfs(r, c):
            if r < 0 or r >= ROWS\
                or c < 0 or c >= COLS\
                or grid[r][c] == "0"\
                or (r, c) in path:
                return False

            path.add((r, c))
            res = (dfs(r + 1, c) or
                    dfs(r - 1, c) or
                    dfs(r, c + 1) or
                    dfs(r, c - 1))
            return res
            
        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in path:
                    dfs(r, c)
                    islands += 1

        return islands