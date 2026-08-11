class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        m,n = len(grid), len(grid[0])
        q = deque()
        for i,row in enumerate(grid):
            for j,x in enumerate(row):
                if x == 0:
                    q.append((i,j))
        
        while q:
            i,j = q.popleft()
            for x,y in (i+1,j),(i-1,j),(i,j+1),(i,j-1):
                if 0<=x<m and 0<=y<n and grid[x][y]==INF:
                    grid[x][y] = grid[i][j]+1
                    q.append((x,y))
                    