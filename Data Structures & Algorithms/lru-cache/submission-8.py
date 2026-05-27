class Node():
    def __init__(self, val=0, key=-1, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.head = Node(-1,-1,None,None)
        self.end = Node(-1,-1,None,self.head)
        self.head.next = self.end
        self.valDic = {}
        self.nodeDic = {}
        

    def get(self, key: int) -> int:
        if key not in self.valDic or key not in self.nodeDic:
            return -1

        cur = self.nodeDic[key]
        cur.prev.next = cur.next
        cur.next.prev = cur.prev
        cur.prev = self.head
        cur.next = self.head.next
        self.head.next.prev = cur
        self.head.next = cur
        
        return self.valDic[key]
        
        
    def put(self, key: int, value: int) -> None:
        if key in self.valDic:
            self.valDic[key] = value
            self.get(key)
            return
        self.valDic[key] = value
        newNode = Node(value, key, self.head.next, self.head)
        self.head.next.prev = newNode
        self.head.next = newNode
        self.nodeDic[key] = newNode

        #delete logic
        if len(self.valDic) > self.cap:
            remNode = self.end.prev
            self.valDic.pop(remNode.key)
            self.nodeDic.pop(remNode.key)
            remNode.prev.next = self.end
            self.end.prev = remNode.prev
            

        return
