class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n-1 != len(edges):
            return False
        
        if len(edges) == 0:
            return True

        adj = {}

        for u,v in edges:
            if u not in adj:
                adj[u] = []
            adj[u].append(v)
            if v not in adj:
                adj[v] = []
            adj[v].append(u)
        
        visited = set()
        def dfs(r,seen,prev):
            visited.add(r)
            print(r, seen, prev)
            if r in seen:
                return False
            for snk in adj[r]:
                if snk == prev:
                    continue
                temp = dfs(snk, seen + [r], r)
                if temp == False:
                    return False
            return True
        ans = dfs(edges[0][0],[],None)
        return ans and len(visited) == n