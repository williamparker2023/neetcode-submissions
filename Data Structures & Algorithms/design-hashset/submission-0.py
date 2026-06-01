class MyHashSet:

    def __init__(self):
        self.hashArr = []
        self.size = 0

    def add(self, key: int) -> None:
        if key>=self.size:
            self.hashArr = self.hashArr + [0]*(key+1-self.size)
            self.size = len(self.hashArr)
        self.hashArr[key] = 1
        

    def remove(self, key: int) -> None:
        if key>=self.size:
            return
        if self.hashArr[key] == 1:
            self.hashArr[key] = 0

    def contains(self, key: int) -> bool:
        if key>=self.size or self.hashArr[key] == 0:
            return False
        return True


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)