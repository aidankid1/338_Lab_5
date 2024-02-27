import random
import timeit
from matplotlib import pyplot as plt
#First Priority Queue Class
class SortPriorityQueue:
    def __init__(self, arr):
        self.arr = arr

    def enqueue(self, data):
        self.arr.insert(len(self.arr) - 1, data)
        mergeSort(self.arr, 0, len(self.arr) - 1)

    def dequeue(self):
        #If it is empty, return None
        if(len(self.arr) == 0):
            return None
        
        return self.arr.pop()
    
    def myPrint(self):
        print(self.arr)


#Second Priority Queue Class
class InsertPriorityQueue:
    def __init__(self, arr):
        self.arr = arr

    def enqueue(self, data):
        pos = 0

        #Finds the position to insert the element on queue
        for i in range(len(self.arr)):
            if(self.arr[i] > data):
                break
            pos += 1

        self.arr.insert(pos, data)

    def dequeue(self):
        #If it is empty, return None
        if(len(self.arr) == 0):
            return None
        
        return self.arr.pop()
    
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

#Generates a list of 1000 random tasks and puts task in list and returns the random task list to user
def generateRandomTasks():
    # Dequeue = 0, Enqueue = 1
    NUM_OF_TASKS = 1000
    tasks = [0] * 7 + [1] * 3
    randomTasks = []

    for _ in range(1000):
        index = random.randint(0, 9)
        randomTasks.append(tasks[index])

    return randomTasks

def performanceTestSort(randomTasks):
    sortQueue = SortPriorityQueue([])
    for i, queue in enumerate(randomTasks):
        if (queue == 0):
            sortQueue.enqueue(i + 1)
        else:
            sortQueue.dequeue()

def performanceTestInsert(randomTasks):
    insertQueue = InsertPriorityQueue([])
    for i, queue in enumerate(randomTasks):
        if (queue == 0):
            insertQueue.enqueue(i + 1)
        else:
            insertQueue.dequeue()

#Main
sortingQueueTime = []
insertingQueueTime = []

for i in range(100):
    randomTasks = generateRandomTasks()
    sortingQueueTime.append(timeit.timeit(lambda: performanceTestSort(randomTasks), number=1))
    insertingQueueTime.append(timeit.timeit(lambda: performanceTestInsert(randomTasks), number=1))

print("Sorting Queue: ",sortingQueueTime)
print("Inserting Queue: ", insertingQueueTime)

plt.scatter([i + 1 for i in range(100)], sortingQueueTime, label='Sort Queue')
plt.scatter([i + 1 for i in range(100)], insertingQueueTime, label='Insert Queue')
plt.legend()
plt.show()

#5) Clearly, inserting it in the correct position is way faster than sorting the whole list after appending the element to the end
#   of the list everytime. To merge sort the array every time after it appends to the end has a O(nlog(n)) complexity while
#   inserting it in the correct position has a O(n) complexity. As long as the queue has more than 10 elements, inserting it in the 
#   correct position will always be faster than sorting it after every append.