import random
import timeit
from matplotlib import pyplot as plt
#1) Stack Class using Arrays
class ArrayStack:
    #Constructor
    def __init__(self, arr):
        self.arr = arr
        self.top = -1

    #Appends an element to the tail
    def push(self, data):
        self.top += 1
        self.arr.append(data)

    #Removes an element from the tail
    def pop(self):
        if len(self.arr) == 0:
            return None
        else:
            self.top -= 1
            return self.arr.pop()
        
#2) Another Stack Class Implementation using a singly Linked List
class LinkedListStack:
    def __init__(self, value):
        if value == None:
            self.head = None
        else:
            self.head = Node(value)

    def push(self, data):
        newNode = Node(data)
        newNode.setNext(self.head)
        self.head = newNode

    def pop(self):
        if self.head == None:
            return None
        else:
            current = self.head.getData()
            self.head = self.head.next
            return current

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

#4) 
def performanceTestArray(randomTasks):
    stackArray = ArrayStack([])
    for task in randomTasks:
        if (task == 0):
            stackArray.push(random.randint(0, 2000))
        else:
            stackArray.pop()

def performanceTestLinkedList(randomTasks):
    stackLinkedList = LinkedListStack(None)
    for task in randomTasks:
        if (task == 0):
            stackLinkedList.push(random.randint(0, 2000))
        else:
            stackLinkedList.pop()

#Set up for testing
ITERATIONS = 100
arrayStackTime = []
linkedListStackTime = []

#Timing Performance for each iteration
for i in range(ITERATIONS):
    randomTasks = generateRandomTasks()
    arrayStackTime.append(timeit.timeit(lambda: performanceTestArray(randomTasks), number=1))
    linkedListStackTime.append(timeit.timeit(lambda: performanceTestLinkedList(randomTasks), number=1))

#5) Scatter Plot for both array and linked list stacks overlayed in same plot
plt.scatter([i + 1 for i in range(ITERATIONS)], arrayStackTime, label='Array')
plt.scatter([i + 1 for i in range(ITERATIONS)], linkedListStackTime, label='Singly Linked List')
plt.title(label='Timing for Stacks with 10000 random Tasks (Array vs LinkedList)')
plt.xlabel('Iteration')
plt.ylabel('Time (s)')
plt.legend(loc='upper left')
plt.show()