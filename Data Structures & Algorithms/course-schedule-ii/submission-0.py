class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ans = []
        adj = {}
        inCount = [0] * numCourses
        q = deque()

        for snk, src in prerequisites:
            if src not in adj:
                adj[src] = []
            adj[src].append(snk)
            inCount[snk] += 1
        
        for course in range(numCourses):
            if inCount[course] == 0:
                q.append(course)
        
        while q:
            curCourse = q.popleft()
            ans.append(curCourse)
            if curCourse not in adj:
                continue
            for snk in adj[curCourse]:
                inCount[snk] -= 1
                if inCount[snk] <= 0:
                    q.append(snk)

        if len(ans) == numCourses:
            return ans
        return []