class circularQueue:
    def __init__(self,size):
        self.arr = [0]*size
        for x in range(size):
            self.arr[x] = None
        self.head = 0
        self.tail = 0
        self.size = size
    def enqueue(self,data):
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
            return None
        elif self.tail == self.head:
            returnValue = self.arr[self.tail]
            self.arr[self.tail] = None
            print("Dequeued ",returnValue)
        else:
            returnValue = self.arr[self.tail]
            self.arr[self.tail] = None
            self.tail = (self.tail+1)%self.size
            print("Dequeued ",returnValue)
        return returnValue
    def peek(self):
        if self.arr[self.tail] == None:
            print("Peeked None")    
            return None
        else:
            print("Peeked ",self.arr[self.tail])
            return self.arr[self.tail]
    


    