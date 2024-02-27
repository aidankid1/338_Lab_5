import random
import timeit
from matplotlib import pyplot as plt
class ArrayQueue:
    def __init__(self,arr):
        self.arr = arr
    def enqueue(self,data):
        self.arr.insert(0,data)
    def dequeue(self):
        if len(self.arr) == 0:
            return None
        else:
            return self.arr.pop()
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
class LinkedListQueue:
    def __init__(self,value):
        if value == None:
            self.head = None
            self.tail = None
        else:
            self.head = Node(value)
            self.tail = self.head
    def enqueue(self,data):
        newNode = Node(data)
        if self.head == None:
            newNode.setNext(self.head)
            self.head = newNode
            self.tail = newNode
        else:
            newNode.setNext(self.head)
            self.head = newNode
    def dequeue(self):
        current = self.head
        if current == None:
            return None
        if current.getNext() == None:
            returnValue = current.getData()
            self.head = None
            self.tail = None
        else:

            while current.getNext() != self.tail:
                current = current.getNext()
            returnValue = self.tail.getData()
            current.setNext(None)
            self.tail = current
        return returnValue
def runLinkedListQueue(arr):
    test = LinkedListQueue(None)
    for x in arr:
        if x == 1:
            test.enqueue(0)
        else:
            test.dequeue()
def runArrayQueue(arr):
    test = ArrayQueue([])
    for x in arr:
        if x == 0:
            test.enqueue(0)
        else:
            test.dequeue()
#question 5:
    #Looking at the graph we can see that with this test the linked list implementation runs significantly faster than
    #the array implementation, however this was to be expected, as the array implementation has complexity O(1) to dequeue and 
    #O(n) to enqueue meanwhile the lnked list implementation has the opposite and our test is designed to enqueue far more often than dequeue




generator = [0,1,0,1,0,1,0,0,0,0]
tasks = [0]*10000
arrayResults = [0]*100
linkedResults = [0]*100
for y in range(100):
    for x in range(10000):
        index = random.randint(0,9)
        tasks[x] = generator[index]
    arrayResults[y] = timeit.timeit(lambda: runArrayQueue(tasks),number=1)
    linkedResults[y] = timeit.timeit(lambda: runLinkedListQueue(tasks),number=1)
xAxis = [x for x in range(100)]
plt.scatter(xAxis,arrayResults,color = "red")
plt.scatter(xAxis,linkedResults,color = "blue")
plt.legend(["Array","Linked List"])
plt.xlabel("Run number")
plt.ylabel("Execution Time")
plt.savefig("ex4.png")

    

    


        

            


        