class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = [[] for _ in range(numCourses)]
        for x,y in prerequisites:
            g[y].append(x)
        vis = [0]*numCourses
        res = []
        def dfs(x):
            vis[x]=1
            for y in g[x]:
                if vis[y]== 1 or vis[y]==0 and dfs(y):
                    return True
            vis[x]=2
            res.append(x)
            return False

        for i,c in enumerate(vis):
            if c == 0 and dfs(i):
                return []
        return res[::-1]
    
        

        

        