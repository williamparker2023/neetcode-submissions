class TimeMap:

    def __init__(self):
        self.dic = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dic:
            self.dic[key] = []
        self.dic[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ""
        n = len(self.dic[key])
        l = 0
        r = n-1
        m = (l+r)//2
        last = [-1,""]

        while l<=r:

            t,k = self.dic[key][m]
            if t<=timestamp and t>=last[0]:
                last = [t,k]
            if t<=last[0]:
                l = m+1
            else:
                r = m-1
            m = (l+r)//2
        return last[1]
