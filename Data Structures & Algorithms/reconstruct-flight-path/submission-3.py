class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {}
        ans = []
        tickets.sort()
        tickets.reverse()
        for src, snk in tickets:
            if src not in adj:
                adj[src] = []
            if snk not in adj:
                adj[snk] = []
            adj[src].append(snk)
        
        def dfs(cur):
            while adj[cur]:
                snk = adj[cur].pop()
                dfs(snk)
            ans.append(cur)

        dfs("JFK")
        ans.reverse()
        return ans