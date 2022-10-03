import heapq

# first create lists
minHeap = []
heapq.heappush(minHeap,3)
# bydefualt heap in python are min heaps
heapq.heappush(minHeap,67)
heapq.heappush(minHeap,69)
heapq.heappush(minHeap,2)

# minimum is always at index 0 
print(minHeap[0])
while len(minHeap):
    print(heapq.heappop(minHeap))
# values will be printed from smallest to largest

# there are no max heaps so
# use min heap and multiply with -1 to use it as maxheap

# push and 

maxHeap = [] 
heapq.heappush(maxHeap,-3)
heapq.heappush(maxHeap,-2)

# Max is always at index 0
# to get real number so we have to multiply it by -1
while len(maxHeap):
    print(-1 * heapq.heappop(maxHeap))

# building heap from initial values
arr = [2,5,2,56,7,145]
heapq.heapify(arr)
while len(arr):
    print(heapq.heappop(arr))
