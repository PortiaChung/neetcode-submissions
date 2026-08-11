class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = [[] for _ in range(numCourses)]
        for a,b in prerequisites:
            g[b].append(a)
        vis = [0]*numCourses

        def dfs(x):
            vis[x]=1
            for y in g[x]:
                if vis[y]==1 or vis[y]==0 and dfs(y):
                    return True
            vis[x]=2
            return False

        for i,v in enumerate(vis):
            if v== 0 and dfs(i):
                return False
        return True
        


