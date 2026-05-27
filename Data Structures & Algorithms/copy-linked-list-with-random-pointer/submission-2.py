"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        oldNodeList = []
        temp = head
        while temp:
            oldNodeList.append(temp)
            temp = temp.next
        n = len(oldNodeList)


        def findNodeIndex(arr, node):
            length = len(arr)
            if not node:
                return -1
            for i in range(length):
                if node == arr[i]:
                    return i
            return -1
        

        newHead = Node(head.val)
        newNodeList = [newHead]
        temp1 = newHead
        temp2 = head.next
        while temp2:
            newNode = Node(temp2.val)
            temp1.next = newNode
            temp1 = newNode
            newNodeList.append(temp1)
            temp2 = temp2.next

        temp1 = newHead
        temp2 = head
        while temp2:
            oldRand = temp2.random
            oldRandIx = findNodeIndex(oldNodeList, oldRand)
            temp1.random = None
            if oldRandIx != -1:
                temp1.random = newNodeList[oldRandIx]
            temp1 = temp1.next
            temp2 = temp2.next

        return newHead