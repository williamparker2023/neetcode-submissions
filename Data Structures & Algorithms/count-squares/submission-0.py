class CountSquares:

    def __init__(self):
        self.pointFreq = {}
        

    def add(self, point):
        """
        :type point: List[int]
        :rtype: None
        """
        point = (point[0],point[1])
        if point not in self.pointFreq:
            self.pointFreq[point] = 1
        else:
            self.pointFreq[point] = self.pointFreq[point] + 1
        

    def count(self, point):
        """
        :type point: List[int]
        :rtype: int
        """
        ans = 0
        x = point[0]
        y = point[1]
        for diff in range(1,1001):
            #if either of these is true, no positive area square is possible
            if (x+diff,y) not in self.pointFreq and (x-diff,y) not in self.pointFreq:
                continue
            if (x,y+diff) not in self.pointFreq and (x,y-diff) not in self.pointFreq:
                continue
            
            if (x+diff,y) in self.pointFreq:
                if (x+diff,y+diff) in self.pointFreq and (x,y+diff) in self.pointFreq:
                    tempAdd = 1
                    tempAdd*=self.pointFreq[(x+diff,y)]
                    tempAdd*=self.pointFreq[(x,y+diff)]
                    tempAdd*=self.pointFreq[(x+diff,y+diff)]
                    ans += tempAdd
                if (x+diff,y-diff) in self.pointFreq and (x,y-diff) in self.pointFreq:
                    tempAdd = 1
                    tempAdd*=self.pointFreq[(x+diff,y)]
                    tempAdd*=self.pointFreq[(x,y-diff)]
                    tempAdd*=self.pointFreq[(x+diff,y-diff)]
                    ans += tempAdd
            
            if (x-diff,y) in self.pointFreq:
                if (x-diff,y+diff) in self.pointFreq and (x,y+diff) in self.pointFreq:
                    tempAdd = 1
                    tempAdd*=self.pointFreq[(x-diff,y)]
                    tempAdd*=self.pointFreq[(x-diff,y+diff)]
                    tempAdd*=self.pointFreq[(x,y+diff)]
                    ans += tempAdd
                if (x-diff,y-diff) in self.pointFreq and (x,y-diff) in self.pointFreq:
                    tempAdd = 1
                    tempAdd*=self.pointFreq[(x-diff,y)]
                    tempAdd*=self.pointFreq[(x-diff,y-diff)]
                    tempAdd*=self.pointFreq[(x,y-diff)]
                    ans += tempAdd
        return ans
        
