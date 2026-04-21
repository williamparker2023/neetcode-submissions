class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        adj = {}
        count = 0
        for n1, n2 in edges:
            if n1 not in adj:
                adj[n1] = []
            if n2 not in adj:
                adj[n2] = []
            adj[n1].append(n2)
            adj[n2].append(n1)

        
        def dfs(node):
            visited.add(node)
            if node not in adj:
                return
            for i in range(len(adj[node])):
                if adj[node][i] not in visited:
                    dfs(adj[node][i])
        
        for i in range(n):
            if i not in visited:
                count+=1
                dfs(i)

        return count 