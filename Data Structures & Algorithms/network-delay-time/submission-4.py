class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        bestTime = [sys.maxsize]*(n+1)
        bestTime[k] = 0
        adj = {(i+1):[] for i in range(n)}

        for u,v,c in times:
            adj[u].append([c,v])
        
        hp = [[0,k]]

        while hp:
            curCost, curNode = heapq.heappop(hp)
            for cost, nei in adj[curNode]:
                if curCost + cost < bestTime[nei]:
                    bestTime[nei] = curCost + cost
                    heapq.heappush(hp, [ bestTime[nei], nei ])

        big = max(bestTime[1:])
        if big == sys.maxsize:
            return -1
        return big