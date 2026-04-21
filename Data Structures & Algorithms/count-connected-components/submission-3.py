class DSU:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0]*size
    
    def find(self, x):
        if self.parent[x] == x:
            return x
        return self.find(self.parent[x])
    
    def join(self, x, y):
        xrep = self.find(x)
        yrep = self.find(y)

        if xrep == yrep:
            return
        if self.rank[xrep]>self.rank[yrep]:
            self.parent[yrep] = xrep
        elif self.rank[xrep]<self.rank[yrep]:
            self.parent[xrep] = yrep
        else:
            self.parent[yrep] = xrep
            self.rank[xrep] += 1

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)

        for src, snk in edges:
            dsu.join(src,snk)
        
        heads = set()
        for p in dsu.parent:
            heads.add(dsu.find(p))
        return len(heads)