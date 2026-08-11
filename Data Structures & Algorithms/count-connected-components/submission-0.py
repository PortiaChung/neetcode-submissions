class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = list(range(n))
        cnt = n

        def find(x):
            if parents[x]!= x:
                parents[x] = find(parents[x])
            return parents[x]
        
        for u,v in edges:
            root_u,root_v = find(u),find(v)
            if root_u != root_v:
                parents[root_u] = root_v
                cnt -=1
        return cnt 


        