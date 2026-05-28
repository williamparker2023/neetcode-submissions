class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {}
        ans = 0
        for u,v in edges:
            if u not in adj:
                adj[u] = []
            if v not in adj:
                adj[v] = []
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            if node not in adj:
                return
            for snk in adj[node]:
                dfs(snk)
        
        for i in range(n):
            if i not in visited:
                ans += 1
                dfs(i)
        return ans