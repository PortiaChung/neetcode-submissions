class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # def dfs(i,j):
        #     if i < 0 or j < 0:
        #         return 0
        #     if i == 0 and j == 0:
        #         return 1
        #     return dfs(i-1,j) + dfs(i,j-1)
        # return dfs(m-1,n-1)

        f = [[0]*(n+1) for _ in range(m+1)]
        f[0][1] = 1
        for i in range(m):
            for j in range(n):
                f[i+1][j+1] = f[i+1][j]+f[i][j+1]
        return f[-1][-1]

        