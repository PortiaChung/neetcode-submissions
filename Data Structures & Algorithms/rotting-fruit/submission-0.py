class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        for i,row in enumerate(grid):
            for j,x in enumerate(row):
                if x == 2:
                    q.append((i,j))
                elif x == 1:
                    fresh +=1
        time = 0
        while q and fresh:
            time +=1
            for _ in range(len(q)):
                i,j = q.popleft()
                for x,y in (i+1,j),(i-1,j),(i,j+1),(i,j-1):
                    if 0<=x<m and 0<=y<n and grid[x][y]==1:
                        q.append((x,y))
                        grid[x][y]=2
                        fresh -=1
        return time if fresh == 0 else -1




                

        