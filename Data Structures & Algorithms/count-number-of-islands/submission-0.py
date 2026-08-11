class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid), len(grid[0])

        def dfs(i,j):
            if i < 0 or i>=m or j< 0 or j>=n or grid[i][j]!= '1':
                return 0   
            grid[i][j] = '2'
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
            
            return 1

        res = 0
        for i,row in enumerate(grid):
            for j,x in enumerate(row):
                if x == '1':
                    res += dfs(i,j)
        return res
            
            
        