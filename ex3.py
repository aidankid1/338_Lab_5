import random
import timeit
from matplotlib import pyplot as plt
#1) Stack Class using Arrays
class ArrayStack:
    #Constructor
    def __init__(self, arr):
        self.arr = arr

    #Appends an element to the tail
    def push(self, data):
        self.arr.append(data)

    #Removes an element from the tail
    def pop(self):
        if len(self.arr) == 0:
            return None
        else:
            return self.arr.pop()
        
#2) Another Stack Class Implementation using a singly Linked List
class LinkedListStack:
    def __init__(self, value):
        if value == None:
            self.head = None
            self.tail = None
        else:
            self.head = Node(value)
            self.tail = self.head

    def push(self, data):
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

#Node class
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

#3) Generates a list of 10000 random tasks and puts each task in a list and returns the list to user
def generateRandomTasks():
    # 0 means Push, 1 means Pop
    NUM_OF_TASKS = 10000
    tasks = [0] * 7 + [1] * 3
    randomTasks = []

    for _ in range(NUM_OF_TASKS):
        index = random.randint(0, 9)
        randomTasks.append(tasks[index])

    return randomTasks

#4) #Set up for testing
ITERATIONS = 100
arrayStackTime = []
linkedListStackTime = []

#Doesn't use repeat cause we don't want to consider the amount of time it takes to generate the random tasks
for i in range(ITERATIONS):
    randomTasks = generateRandomTasks()
    arrayStackTime.append()
    linkedListStackTime.append()

#5) Scatter Plot for both array and linked list stacks overlayed in same plot
plt.scatter([i + 1 for i in range(ITERATIONS)], arrayStackTime, label='Array')
plt.scatter([i + 1 for i in range(ITERATIONS)], linkedListStackTime, label='Singly Linked List')
plt.legend()
plt.show()