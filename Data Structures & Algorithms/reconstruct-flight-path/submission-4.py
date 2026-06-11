class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        tickets.reverse()
        adj = {}
        for u,v in tickets:
            if u not in adj:
                adj[u] = []
            if v not in adj:
                adj[v] = []
            adj[u].append(v)
        
        ans = []

        def dfs(cur):
            while adj[cur]:
                dst = adj[cur].pop()
                dfs(dst)
            ans.append(cur)
        
        dfs("JFK")
        ans.reverse()
        return ans