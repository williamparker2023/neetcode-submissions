class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        adj = {}

        for i in range(10000):
            cur = str(i)
            cur = "0" * (4-len(cur)) + cur
            adj[cur] = []

            #it will have 8 connections, one up and one down per digit
            adj[cur].append( cur[:3]+str( (int(cur[3])+1)%10 ) )
            adj[cur].append( cur[:3]+str( (int(cur[3])-1)%10 ) )

            adj[cur].append( cur[:2]+str( (int(cur[2])+1)%10 )+cur[3] )
            adj[cur].append( cur[:2]+str( (int(cur[2])-1)%10 )+cur[3] )

            adj[cur].append( cur[0]+str( (int(cur[1])+1)%10 )+cur[2:] )
            adj[cur].append( cur[0]+str( (int(cur[1])-1)%10 )+cur[2:] )

            adj[cur].append( str( (int(cur[0])+1)%10 )+cur[1:] )
            adj[cur].append( str( (int(cur[0])-1)%10 )+cur[1:] )
        
        hp = [[0,"0000"]]
        best = {i:sys.maxsize for i in adj}
        best["0000"] = 0

        deadSet = set(deadends)
        if "0000" in deadSet:
            return -1

        while hp:
            curLength, curCode = heapq.heappop(hp)
            if curCode == target:
                return curLength
            
            for v in adj[curCode]:
                if v not in deadSet and curLength + 1 < best[v]:
                    best[v] = curLength+1
                    heapq.heappush(hp,[curLength+1,v])
        return -1