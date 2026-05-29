class DS:
    def __init__(self, n):
        self.parent = [_ for _ in range(n)]
        self.rank = [0]*n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if xroot != yroot:
            if self.rank[xroot] < self.rank[yroot]:
                self.parent[xroot] = yroot
            elif self.rank[yroot] > self.rank[xroot]:
                self.parent[yroot] = xroot
            else:
                self.parent[yroot] = xroot
                self.rank[xroot] += 1

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ds = DS(n)
        for u,v in edges:
            ds.union(u,v)
        roots = set()
        for i in range(n):
            roots.add(ds.find(i))
        return len(roots)
