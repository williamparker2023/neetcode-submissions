class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i:[] for i in range(1,n+1)}

        for u,v,t in times:
            adj[u].append([t,v])
        
        inTimes = [sys.maxsize]*(n+1)
        inTimes[k] = 0
        hp = [[0,k]]

        while hp:
            curT, curU = heapq.heappop(hp)
            for t,v in adj[curU]:
                if curT + t < inTimes[v]:
                    heapq.heappush(hp,[curT+t,v])
                    inTimes[v] = curT + t
        
        big = 0

        for i in range(1,n+1):
            if inTimes[i] == sys.maxsize:
                return -1
            big = max(big,inTimes[i])
        return big


