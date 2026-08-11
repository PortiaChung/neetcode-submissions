class Solution:
    def exist(self, grid: List[List[str]], word: str) -> bool:
        m,n= len(grid), len(grid[0])

        def dfs(i,j,k):
            if grid[i][j]!= word[k]:
                return False
            if k == len(word)-1:
                return True
            
            grid[i][j] = ''
            for x,y in (i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j):
                if 0<=x<m and 0<=y<n and dfs(x,y,k+1):
                    return True
            grid[i][j] = word[k]
            return False
        

        for i in range(m):
            for j in range(n):
                if dfs(i,j,0):
                    return True
        return False

        