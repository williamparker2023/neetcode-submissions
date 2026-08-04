class StockSpanner:

    def __init__(self):
        #we want a decreasing stack
        #each item will be [value,index]
        self.stack = []
        self.ix = 0

    def next(self, price: int) -> int:
        print(price,self.stack)
        cur = 1
        while self.stack and self.stack[-1][0]<=price:
            self.stack.pop()
        if self.stack:
            cur = self.ix-self.stack[-1][1]
        else:
            cur = self.ix
        self.ix += 1
        self.stack.append([price,self.ix])
        return cur+1
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)