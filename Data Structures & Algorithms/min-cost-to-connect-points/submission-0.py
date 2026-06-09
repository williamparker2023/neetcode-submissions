class US:
    def __init__(self, points):
        self.parent = {tuple(p):tuple(p) for p in points}
        self.rank = {tuple(p):0 for p in points}

    def find(self, x):
        if self.parent[x] == x:
            return x
        return self.find(self.parent[x])

    def join(self, x, y):
        xi = self.find(x)
        yi = self.find(y)
        if xi == yi:
            return
        if self.rank[xi] > self.rank[yi]:
            self.parent[yi] = xi
        elif self.rank[xi] < self.rank[yi]:
            self.parent[xi] = yi
        else:
            self.parent[xi] = yi
            self.rank[yi] += 1
        

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)        
        us = US(points)

        e = []
        for i in range(n-1):
            x1,y1 = points[i]
            for j in range(i+1,n):
                x2,y2 = points[j]
                dist = abs(x2-x1) + abs(y2-y1)
                e.append([dist,x1,y1,x2,y2])
        e.sort()

        ans = 0
        for dist,x1,y1,x2,y2 in e:
            if us.find((x1,y1)) == us.find((x2,y2)):
                continue
            else:
                ans+=dist
                us.join((x1,y1),(x2,y2))
        
        return ans
                

