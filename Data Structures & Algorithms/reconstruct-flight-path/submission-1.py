class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {}
        tickets.sort()
        for src, snk in tickets:
            if src not in adj:
                adj[src] = []
            adj[src].append(snk)
        
        ans = ["JFK"]

        def dfs(cur):
            if len(ans) == len(tickets)+1:
                return True
            if cur not in adj or len(adj[cur]) == 0:
                return False
            for i in range(len(adj[cur])):
                snk = adj[cur][i]
                adj[cur] = adj[cur][:i] + adj[cur][i+1:]
                ans.append(snk)
                if dfs(snk):
                    return True
                adj[cur] = adj[cur][:i] + [snk] + adj[cur][i:]
                ans.pop()
        dfs("JFK")
        return ans