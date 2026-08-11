class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n = len(text1), len(text2)
        # def dfs(i,j):
        #     if i < 0 or j < 0:
        #         return 0
        #     if text1[i] == text2[j]:
        #         return dfs(i-1,j-1)+1
        #     else:
        #         return max(dfs(i-1,j),dfs(i,j-1))
        
        # return dfs(m-1,n-1)

        f = [[0]*(n+1) for _ in range(m+1)]
        for i,x in enumerate(text1):
            for j,y in enumerate(text2):
                f[i+1][j+1] = f[i][j]+1 if x == y else max(f[i][j+1],f[i+1][j])
        return f[-1][-1]



        