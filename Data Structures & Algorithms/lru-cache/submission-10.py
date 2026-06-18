class Node:
    def __init__(self, val=0, key=0, prev=None, next=None):
        self.val = val
        self.key = key
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.size = 0
        self.head = Node(0)
        self.end = Node(0)
        self.head.next = self.end
        self.end.prev = self.head
        self.keyToNode = {}

    def get(self, key: int) -> int:
        if key not in self.keyToNode:
            return -1
        
        curNode = self.keyToNode[key]
        curNode.prev.next = curNode.next
        curNode.next.prev = curNode.prev
        
        curNode.prev = self.head
        curNode.next = self.head.next
        curNode.next.prev = curNode
        self.head.next = curNode

        return curNode.val
        

    def put(self, key: int, value: int) -> None:
        if key not in self.keyToNode:
            newNode = Node(value,key,self.head,self.head.next)
            self.head.next = newNode
            newNode.next.prev = newNode
            self.keyToNode[key] = newNode
            self.size += 1
        else:
            curNode = self.keyToNode[key]
            curNode.val = value
            curNode.prev.next = curNode.next
            curNode.next.prev = curNode.prev

            curNode.prev = self.head
            curNode.next = self.head.next
            curNode.next.prev = curNode
            self.head.next = curNode
        
        if self.size > self.cap:
            self.size -= 1
            poppedNode = self.end.prev
            self.keyToNode.pop(poppedNode.key)
            poppedNode.prev.next = poppedNode.next
            poppedNode.next.prev = poppedNode.prev

