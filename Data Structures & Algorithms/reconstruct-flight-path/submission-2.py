class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {}
        ans = ["JFK"]
        tickets.sort()
        for src, snk in tickets:
            if src not in adj:
                adj[src] = []
            adj[src].append(snk)
        
        def dfs(cur):
            if len(ans) == len(tickets) + 1:
                return True
            if cur not in adj or len(adj[cur]) == 0:
                return False
            for i in range(len(adj[cur])):
                snk = adj[cur][i]
                ans.append(snk)
                adj[cur] = adj[cur][:i] + adj[cur][i+1:]
                if dfs(snk):
                    return True
                ans.pop()
                adj[cur] = adj[cur][:i] + [snk] + adj[cur][i:]
        dfs("JFK")
        return ans