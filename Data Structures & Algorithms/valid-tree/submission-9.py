class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n!=len(edges)+1:
            return False
        
        seen = set()

        adj = {}
        for src, snk in edges:
            if src not in adj:
                adj[src] = []
            adj[src].append(snk)

            if snk not in adj:
                adj[snk] = []
            adj[snk].append(src)

        def dfs(src,prev):
            if src in seen:
                return False
            seen.add(src)
            if src not in adj:
                return True
            for snk in adj[src]:
                if snk!=prev:
                    print(src,snk)
                    if not dfs(snk,src):
                        return False
            return True
        
        noCycle = dfs(0,-1)
        return noCycle and len(seen)==n

