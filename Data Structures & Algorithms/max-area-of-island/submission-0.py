class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])

        def dfs(i,j):
            if i < 0 or i>=m or j< 0 or j>=n or grid[i][j]!= 1:
                return 0
            area = 1
            grid[i][j]=2
            area += dfs(i+1,j)+dfs(i-1,j)+dfs(i,j+1)+dfs(i,j-1)
            return area 

        res = 0
        for i,row in enumerate(grid):
            for j,x in enumerate(row):
                res = max(res,dfs(i,j))
        return res
        