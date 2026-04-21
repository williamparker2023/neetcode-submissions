class DynamicArray:
    
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.array = [None]*capacity
        self.size=0

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.size==self.capacity:
            self.resize()
        self.array[self.size]=n
        self.size+=1


    def popback(self) -> int:
        self.size -= 1
        temp = self.array[self.size]
        self.array[self.size] = None
        return temp


    def resize(self) -> None:
        temp = [None]*2*self.capacity

        for i in range(self.capacity):
            temp[i] = self.array[i]

        self.array = temp[:]
        self.capacity *= 2


    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity