class Node:
    def __init__(self, val=0,prev=None,next=None):
        self.val = val
        self.next = next
        self.prev = prev
class Deque:
    
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head


    def isEmpty(self) -> bool:
        return self.head.next == self.tail
        

    def append(self, value: int) -> None:
        newNode = Node(value)
        lastNode = self.tail.prev
        lastNode.next = newNode
        newNode.prev = lastNode
        newNode.next = self.tail
        self.tail.prev = newNode
        

    def appendleft(self, value: int) -> None:
        newNode = Node(value)
        firstNode = self.head.next
        self.head.next = newNode
        newNode.prev = self.head
        newNode.next = firstNode
        firstNode.prev = newNode
        

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        lastNode = self.tail.prev
        val = lastNode.val
        prevNode = lastNode.prev

        prevNode.next = self.tail
        self.tail.prev = prevNode
        return val

        

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        firstNode = self.head.next
        val = firstNode.val
        nextNode = firstNode.next

        self.head.next = nextNode
        nextNode.prev = self.head
        return val

        
