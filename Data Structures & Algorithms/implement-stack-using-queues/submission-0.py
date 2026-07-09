class MyStack:

    def __init__(self):
        self.q = deque()
        self.size = 0
        

    def push(self, x: int) -> None:
        self.q.append(x)
        self.size += 1
        

    def pop(self) -> int:
        for i in range(self.size-1):
            self.q.append(self.q.popleft())
        self.size -= 1
        return self.q.popleft()
        

    def top(self) -> int:
        top = -1
        for i in range(self.size):
            top = self.q.popleft()
            self.q.append(top)
        return top

    def empty(self) -> bool:
        if self.size == 0:
            return True
        return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()