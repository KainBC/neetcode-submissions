class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            returns
            
        num_islands = 0
        visited = set()

        def dfs(i,j):
            if (i < 0 or i >= len(grid) or 
                j < 0 or j >= len(grid[0]) or 
                grid[i][j] == "0" or 
                (i, j) in visited):
                return

            p = (i,j)
            visited.add((i,j))
            dfs(i+1, j)
            dfs(i, j+1)
            dfs(i-1, j)
            dfs(i, j-1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                p = (i,j)
                if grid[i][j] == "1" and p not in visited :
                    num_islands+=1
                    dfs(i, j)

        return num_islands