class Node:
    def __init__(self, val=0, next=None, prev=None, key = -1):
        self.val = val
        self.next = next
        self.prev = prev
        self.key = key

class LRUCache:

    def __init__(self, capacity: int):
        self.start = Node()
        self.end = Node()
        self.start.next = self.end
        self.end.prev = self.start
        #need to get val and node from key
        #move the node to most recent used and return val
        self.keyToVal = {}
        self.keyToNode = {}
        self.cap = capacity
        

    def get(self, key: int) -> int:
        print(self.cap)
        if key not in self.keyToVal:
            return -1
        
        curNode = self.keyToNode[key]
        curNode.prev.next = curNode.next
        curNode.next.prev = curNode.prev

        curNode.next = self.start.next
        curNode.next.prev = curNode
        curNode.prev = self.start
        self.start.next = curNode
        
        return self.keyToVal[key]
        

    def put(self, key: int, value: int) -> None:
        curNode = None
        if key in self.keyToVal:
            curNode = self.keyToNode[key]
            curNode.prev.next = curNode.next
            curNode.next.prev = curNode.prev

        else:
            self.cap-=1
            curNode = Node()
            curNode.key = key
            self.keyToNode[key] = curNode
        self.keyToVal[key] = value
        self.keyToNode[key].val = value

        curNode.next = self.start.next
        curNode.next.prev = curNode
        self.start.next = curNode
        curNode.prev = self.start

        if self.cap < 0:
            delKey = self.end.prev.key
            self.cap = 0
            self.end.prev = self.end.prev.prev
            self.end.prev.next = self.end
            self.keyToVal.pop(delKey)
            self.keyToNode.pop(delKey)
        
