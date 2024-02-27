import random
import timeit
from matplotlib import pyplot as plt
#Class for a Stack using Arrays
class ArrayStack:
    def __init__(self, arr):
        self.arr = arr

    def push(self, data):
        self.arr.insert(len(self.arr) - 1, data)

    def pop(self):
        if len(self.arr) == 0:
            return None
        else:
            return self.arr.pop()
        
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def getData(self):
        return self.data
    def setData(self, value):
        self.data = value
    def getNext(self):
        return self.next
    def setNext(self, next):
        self.next = next

class LinkedListStack:
    def __init__(self, value):
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

def performanceTestSort(randomTasks):
    sortQueue = ArrayStack([])
    for i, queue in enumerate(randomTasks):
        if (queue == 0):
            sortQueue.enqueue(i + 1)
        else:
            sortQueue.dequeue()

def runLinkedListQueue(arr):
    test = LinkedListStack(None)
    for x in arr:
        if x == 1:
            test.enqueue(0)
        else:
            test.dequeue()

#Generates a list of 1000 random tasks and puts task in list and returns the random task list to user
def generateRandomTasks():
    # Dequeue = 0, Enqueue = 1
    NUM_OF_TASKS = 1000
    tasks = [0] * 7 + [1] * 3
    randomTasks = []

    for _ in range(NUM_OF_TASKS):
        index = random.randint(0, 9)
        randomTasks.append(tasks[index])

    return randomTasks