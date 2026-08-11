class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m,n = len(board), len(board[0])
        q = deque()
        for i in range(m):
            for j in range(n):
                if (i==0 or i==m-1 or j==0 or j==n-1) and board[i][j]=='O':
                    board[i][j]='1'
                    q.append((i,j))
        
        while q:
            i,j = q.popleft()
            for x,y in (i+1,j),(i-1,j),(i,j+1),(i,j-1):
                if 0<=x<m and 0<=y<n and board[x][y]=='O':
                    board[x][y]='1'
                    q.append((x,y))
        

        for i in range(m):
            for j in range(n):
                if board[i][j]=='O':
                    board[i][j]='X'
                elif board[i][j]=='1':
                    board[i][j]='O'

        

        