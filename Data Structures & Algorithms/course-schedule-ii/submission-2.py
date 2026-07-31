class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i:[] for i in range(numCourses)}
        numIn = [0] * numCourses
        for u,v in prerequisites:
            adj[v].append(u)
            numIn[u] += 1
        
        q = deque()
        for i in range(numCourses):
            if numIn[i] == 0:
                q.append(i)

        ans = []
        while q:
            cur = q.popleft()
            for v in adj[cur]:
                numIn[v] -= 1
                if numIn[v] == 0:
                    q.append(v)
            ans.append(cur)
        if len(ans) < numCourses:
            return []
        return ans