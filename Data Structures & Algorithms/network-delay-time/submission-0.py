class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        seen = set()
        seen.add(k-1)
        hp = [[0,k-1]]
        fast = [sys.maxsize]*n
        fast[k-1] = 0
        adj = {}

        for u,v,t in times:
            if u-1 not in adj:
                adj[u-1] = []
            adj[u-1].append([v-1,t])
        
        while len(hp)>0:
            time,u = heapq.heappop(hp)
            if u not in adj:
                continue
            for v,t in adj[u]:
                if fast[u] + t < fast[v]:
                    seen.add(v)
                    fast[v] = fast[u] + t
                    heapq.heappush(hp,[fast[v],v])


        big = max(fast)
        if big == sys.maxsize:
            return -1
        return big