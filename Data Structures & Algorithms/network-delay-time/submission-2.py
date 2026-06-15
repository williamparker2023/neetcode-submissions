class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {(i+1):[] for i in range(n)}
        for u,v,t in times:
            adj[u].append([v,t])
        dists = {(i+1):sys.maxsize for i in range(n)}
        dists[k] = 0
        
        hp = [k]
        while hp:
            u = heapq.heappop(hp)
            for v,t in adj[u]:
                if dists[u] + t < dists[v]:
                    dists[v] = dists[u] + t
                    heapq.heappush(hp,v)
        big = 0
        for node in dists:
            if dists[node] == sys.maxsize:
                return -1
            big = max(big,dists[node])
        return big