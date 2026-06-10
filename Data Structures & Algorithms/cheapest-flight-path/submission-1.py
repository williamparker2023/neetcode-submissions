class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        cheap = [[sys.maxsize]*(k+2) for _ in range(n)]
        #[node][numFlights]
        cheap[src][0] = 0
        adj = {}
        for u,v,cost in flights:
            if u not in adj:
                adj[u] = []
            adj[u].append((v,cost))
        
        q = deque()
        q.append((src,0))

        while q:
            u,num = q.popleft()
            if num > k:
                break
            if u not in adj:
                continue
            for v,cost in adj[u]:
                if cost + cheap[u][num] < cheap[v][num+1]:
                    cheap[v][num+1] = cost + cheap[u][num]
                    q.append((v,num+1))


        print(cheap)
        ans = min(cheap[dst][:k+2])
        if ans == sys.maxsize:
            return -1
        return ans