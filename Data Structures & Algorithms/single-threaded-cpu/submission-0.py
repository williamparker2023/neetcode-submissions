class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        for i in range(n):
            #processing time, start time, index
            tasks[i] = [tasks[i][1]] + [tasks[i][0]] + [i]
        tasks.sort(key=lambda x:(x[1],x[0],x[2]))
        i = 1
        hp = [tasks[0]]
        ans = []
        curTime = tasks[0][1]

        while i<n:
            while curTime<tasks[i][1] and hp:
                curLen, curStart, curIx = heapq.heappop(hp)
                ans.append(curIx)
                curTime += curLen
            curTime = max(curTime,tasks[i][1])
            while i<n and curTime >= tasks[i][1]:
                heapq.heappush(hp,tasks[i])
                i+=1
        while hp:
            curLen, curStart, curIx = heapq.heappop(hp)
            ans.append(curIx)
            curTime += curLen
        return ans