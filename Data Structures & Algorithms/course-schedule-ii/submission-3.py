class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i:[] for i in range(numCourses)}
        inCount = [0]*numCourses
        order = []

        for v,u in prerequisites:
            adj[u].append(v)
            inCount[v] += 1
        
        hp = []
        for i in range(numCourses):
            if inCount[i] == 0:
                heapq.heappush(hp,i)
        
        while hp:
            cur = heapq.heappop(hp)
            order.append(cur)
            for v in adj[cur]:
                inCount[v] -= 1
                if inCount[v] == 0:
                    heapq.heappush(hp, v)
        
        for i in range(numCourses):
            if inCount[i] != 0:
                return []
        return order
