class arrayCircularQueue:
    def __init__(self,size):
        self.arr = [0]*size
        for x in range(size):
            self.arr[x] = None
        self.head = 0
        self.tail = 0
        self.size = size
    def enqueue(self,data):
        if self.arr[self.head] == None:
            self.arr[self.head] = data
            print("Enqueued ",data)
        else:
            newHead = (self.head+1)%self.size
            if newHead == self.tail:
                print("Enqueued None")
            else:
                self.head = newHead
                self.arr[self.head] = data
                print("Enqueued ",data)
    def dequeue(self):
        if self.arr[self.tail] == None:
            print("Dequeued None")
        elif self.tail == self.head:
            returnValue = self.arr[self.tail]
            self.arr[self.tail] = None
            print("Dequeued ",returnValue)
        else:
            returnValue = self.arr[self.tail]
            self.arr[self.tail] = None
            self.tail = (self.tail+1)%self.size
            print("Dequeued ",returnValue)
    def peek(self):
        if self.arr[self.tail] == None:
            print("Peeked None")    
        else:
            print("Peeked ",self.arr[self.tail])
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def getData(self):
        return self.data
    def setData(self, value):
        self.data = value
    def getNext(self):
        return self.next
    def setNext(self,next):
        self.next = next
class linkedCircularQueue:
    def __init__(self,max):
        self.head = None
        self.tail = None
        newNode = Node(None)
        self.tail = newNode
        self.head = newNode
        for x in range(1,max):
            newNode2 = Node(None)
            newNode2.setNext(self.head)
            self.head = newNode2
        self.tail.setNext(self.head)
        self.tail = self.head
    def enqueue(self,data):
        if self.head.getNext() == self.tail:
            print("Enqueued None")
        elif self.head.getData() == None:
            self.head.setData(data)
            print("Enqueued ",data)
        else:
            self.head = self.head.getNext()
            self.head.setData(data)
            print("Enqueued ",data)
    def dequeue(self):
        if self.tail.getData() == None:
            print("Dequeued None")
        elif self.tail==self.head:
            returnValue = self.tail.getData()
            self.tail.setData(None)
            print("Dequeued ", returnValue)
        else:
            returnValue = self.tail.getData()
            self.tail.setData(None)
            self.tail = self.tail.getNext()
            print("Dequeued ", returnValue)
    def peek(self):
        if self.tail.getData() == None:
            print("Peeked None")
        else:
            returnValue = self.tail.getData()
            print("Peeked ", returnValue)
linked = linkedCircularQueue(10)
arr = arrayCircularQueue(10)

#commands
print("expected: dequeued none")
arr.dequeue()
linked.dequeue()
print("expected: peeked none")
arr.peek()
linked.peek()
print("expected: enqueued 1")
arr.enqueue(1)
linked.enqueue(1)
print("expected: enqueued 2")
arr.enqueue(2)
linked.enqueue(2)
print("expected: enqueued 3")
arr.enqueue(3)
linked.enqueue(3)
print("expected: enqueued 4")
arr.enqueue(4)
linked.enqueue(4)
print("expected: enqueued 5")
arr.enqueue(5)
linked.enqueue(5)
print("expected: enqueued 6")
arr.enqueue(6)
linked.enqueue(6)
print("expected: peeked 1")
arr.peek()
linked.peek()
print("expected: dequeued 1")
arr.dequeue()
linked.dequeue()
print("expected: enqueued 7")
arr.enqueue(7)
linked.enqueue(7)
print("expected: enqueued 8")
arr.enqueue(8)
linked.enqueue(8)
print("expected: enqueued 9")
arr.enqueue(9)
linked.enqueue(9)
print("expected: peeked 2")
arr.peek()
linked.peek()
print("expected: enqueued 10")
arr.enqueue(10)
linked.enqueue(10)
print("expected: enqueued 11")
arr.enqueue(11)
linked.enqueue(11)
print("expected: enqueued None")
arr.enqueue(12)
linked.enqueue(12)
print("expected: dequeued 2")
arr.dequeue()
linked.dequeue()
print("expected: dequeued 3")
arr.dequeue()
linked.dequeue()
print("expected: dequeued 4")
arr.dequeue()
linked.dequeue()
print("expected: dequeued 5")
arr.dequeue()
linked.dequeue()
print("expected: dequeued 6")
arr.dequeue()
linked.dequeue()
print("expected: dequeued 7")
arr.dequeue()
linked.dequeue()
print("expected: dequeued 8")
arr.dequeue()
linked.dequeue()
print("expected: enqueued 12")
arr.enqueue(12)
linked.enqueue(12)
print("expected: enqueued 13")
arr.enqueue(13)
linked.enqueue(13)
print("expected: enqueued 14")
arr.enqueue(14)
linked.enqueue(14)
print("expected: enqueued 15")
arr.enqueue(15)
linked.enqueue(15)
print("expected: Peeked 9")
arr.peek()
linked.peek()
print("expected: dequeued 9")
arr.dequeue()
linked.dequeue()
print("expected: dequeued 10")
arr.dequeue()
linked.dequeue()
print("expected: dequeued 11")
arr.dequeue()
linked.dequeue()
print("expected: dequeued 12")
arr.dequeue()
linked.dequeue()
print("expected: dequeued 13")
arr.dequeue()
linked.dequeue()
print("expected: dequeued 14")
arr.dequeue()
linked.dequeue()
print("expected: dequeued 15")
arr.dequeue()
linked.dequeue()
print("expected: dequeued None")
arr.dequeue()
linked.dequeue()
print("expected: enqueued 16")
arr.enqueue(16)
linked.enqueue(16)
print("expected: Peeked 16")
arr.peek()
linked.peek()
print("expected: enqueued 17")
arr.enqueue(17)
linked.enqueue(17)
print("expected: dequeued 16")
arr.dequeue()
linked.dequeue()



    

    