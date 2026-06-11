class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        ans = [-1]*len(queries)
        queries = [[queries[i],i] for i in range(len(queries))]
        print(queries)
        queries.sort()
        intervals.sort(key=lambda x:(x[0],x[1]))
        #size, start, end
        hp = []
        iIx = 0

        for i in range(len(queries)):
            while (iIx<len(intervals) and intervals[iIx][0]<=queries[i][0]):
                s,e = intervals[iIx]
                heapq.heappush(hp, [e-s+1,s,e])
                iIx+=1
            while hp and hp[0][2]<queries[i][0]:
                heapq.heappop(hp)
            
            print(i,hp)
            if not hp:
                ans[i] = -1
            else:
                ans[i] = hp[0][0]
        orderedAns = [0]*len(queries)
        for i in range(len(ans)):
            ix = queries[i][1]
            orderedAns[ix] = ans[i]
        return orderedAns