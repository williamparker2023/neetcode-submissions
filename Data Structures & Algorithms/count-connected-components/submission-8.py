class DS:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0]*n
    
    def find(self, x):
        if self.parent[x] == x:
            return x
        return self.find(self.parent[x])
    
    def merge(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        if xr == yr:
            return
        if self.rank[xr]<self.rank[yr]:
            self.parent[xr] = yr
        elif self.rank[xr]>self.rank[yr]:
            self.parent[yr] = xr
        else:
            self.parent[xr] = yr
            self.rank[yr] += 1

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ds = DS(n)
        for u,v in edges:
            ds.merge(u,v)
        roots = set()
        for i in range(n):
            roots.add(ds.find(i))
        return len(roots)