class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        numIn = [0] * numCourses
        for snk,src in prerequisites:
            if src not in adj:
                adj[src] = []
            adj[src].append(snk)
            numIn[snk] += 1

        q = deque()
        for i in range(numCourses):
            if numIn[i] == 0:
                q.append(i)
        
        while q:
            curCourse = q.popleft()
            if curCourse not in adj:
                continue
            for snk in adj[curCourse]:
                numIn[snk] -= 1
                if numIn[snk] <= 0:
                    q.append(snk)
        
        for num in numIn:
            if num>0:
                return False
        return True