class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m,n = len(heights),len(heights[0])
        def search(path):
            def dfs(i,j):
                vis.add((i,j))
                for x,y in (i+1,j),(i-1,j),(i,j+1),(i,j-1):
                    if 0<=x<m and 0<=y<n and (x,y) not in vis and heights[x][y] >= heights[i][j]:
                        dfs(x,y)
            vis = set()
            for i,j in path:
                dfs(i,j)
            return vis
        pacific = [(0,j) for j in range(n)] + [(i,0) for i in range(1,m)]
        atlantic = [(m-1,j) for j in range(n)] + [(i,n-1) for i in range(m-1)]
        return list(search(pacific)&search(atlantic))

        