import random
import timeit
from matplotlib import pyplot as plt

#1) First Priority Queue Class (uses merge sort after it appends an element to tail of queue)
class SortPriorityQueue:
    def __init__(self, arr):
        self.arr = arr

    def enqueue(self, data):
        #Adds new element to the tail of the queue and then sorts it right after
        self.arr.append(data)
        mergeSort(self.arr, 0, len(self.arr) - 1)

    def dequeue(self):
        #If it is empty, return None
        if(len(self.arr) == 0):
            return None
        
        #Pops and returns value at the beginning of the queue
        return self.arr.pop(0)
    
    #Helper Print Method
    def myPrint(self):
        print(self.arr)

#2) Second Priority Queue Class (inserts value directly to the queue to ensure it is sorted at all times)
class InsertPriorityQueue:
    def __init__(self, arr):
        self.arr = arr

    def enqueue(self, data):
        pos = 0

        #Finds the position to insert the element to queue to keep queue sorted
        for i in range(len(self.arr)):
            if(self.arr[i] > data):
                break
            pos += 1

        self.arr.insert(pos, data)

    def dequeue(self):
        #If it is empty, return None
        if(len(self.arr) == 0):
            return None
        #Pops and returns value at the beginning of the queue
        return self.arr.pop(0)
    
    def myPrint(self):
        print(self.arr)

#Merge Sort
def mergeSort(arr, low, high):
    if low < high:
        mid = (low+high)//2
        mergeSort(arr, low, mid)
        mergeSort(arr, mid + 1, high)
        merge(arr, low, mid, high)

#Combine two sub arrays that are sorted 
def merge(arr, low, mid, high):

    sub_array1 = arr[low:mid + 1]
    sub_array2 = arr[mid + 1:high + 1]

    i = 0
    j = 0
    k = low

    while (i < len(sub_array1)) and (j < len(sub_array2)):
        if sub_array1[i] <= sub_array2[j]:
            arr[k] = sub_array1[i]
            i += 1
        else:
            arr[k] = sub_array2[j]
            j += 1
        k += 1

    while (i < len(sub_array1)):
        arr[k] = sub_array1[i]
        i += 1
        k += 1

    while (j < len(sub_array2)):
        arr[k] = sub_array2[j]
        j += 1
        k += 1

#3) Generates a list of 1000 random tasks and puts task in a list and returns the random tasks to user
def generateRandomTasks():
    # 0 means Enqueue, 1 means Dequeue. 
    # Therefore 70% of time it will enqueue, and 30% it will dequeue
    NUM_OF_TASKS = 1000
    tasks = [0] * 7 + [1] * 3
    randomTasks = []

    for _ in range(NUM_OF_TASKS):
        index = random.randint(0, 9)
        randomTasks.append(tasks[index])

    return randomTasks

#4)
def performanceTestSort(randomTasks):
    sortQueue = SortPriorityQueue([])
    for queue in randomTasks:
        if (queue == 0):
            sortQueue.enqueue(random.randint(0, 2000))
        else:
            sortQueue.dequeue()

def performanceTestInsert(randomTasks):
    insertQueue = InsertPriorityQueue([])
    for queue in randomTasks:
        if (queue == 0):
            insertQueue.enqueue(random.randint(0, 2000))
        else:
            insertQueue.dequeue()

#Set up for testing
ITERATIONS = 100
sortingQueueTime = []
insertingQueueTime = []

#Timing Performance for each iteration
for i in range(ITERATIONS):
    randomTasks = generateRandomTasks()
    sortingQueueTime.append(timeit.timeit(lambda: performanceTestSort(randomTasks), number=1))
    insertingQueueTime.append(timeit.timeit(lambda: performanceTestInsert(randomTasks), number=1))

#Prints out result
print("Sorting Queue: ")
print(sortingQueueTime)
print("Inserting Queue: ")
print(insertingQueueTime)

#Shows a scatter plot for better visualization of the performance doing random tasks
plt.scatter([i + 1 for i in range(ITERATIONS)], sortingQueueTime, label='Sort Queue')
plt.scatter([i + 1 for i in range(ITERATIONS)], insertingQueueTime, label='Insert Queue')
plt.title(label='Timing for Queues with 1000 random Tasks (Append & Sort vs Insert In Correct Spot)')
plt.xlabel('Iteration')
plt.ylabel('Time (s)')
plt.legend(loc='upper left')
plt.show()

#5) Clearly, inserting a new element to the correct position is way faster than sorting the whole queue after appending the element to the end
#   of the queue everytime. To merge sort the array every time after it appends to the end has an O(nlog(n)) complexity while
#   inserting it in the correct position has an O(n) complexity. As long as the queue has more than 10 elements, inserting it in the 
#   correct position will always be faster than sorting it after every tail appending.