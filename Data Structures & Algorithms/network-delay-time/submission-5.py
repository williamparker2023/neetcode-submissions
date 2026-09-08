class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        shortest = [sys.maxsize] * (n+1)
        shortest[k] = 0

        adj = {i:[] for i in range(n+1)}
        for u,v,t in times:
            adj[u].append([v,t])

        hp = [(0,k)]

        while hp:
            curTime, curNode = heapq.heappop(hp)
            for v,t in adj[curNode]:
                if curTime + t < shortest[v]:
                    heapq.heappush(hp, [curTime + t, v])
                    shortest[v] = curTime + t
        
        big = max(shortest[1:])
        if big == sys.maxsize:
            return -1
        
        return big