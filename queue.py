# queues are doubly ended queues by default in python

from collection import deque

queue = deque()
queue.append(2)
queue.append(69)
print(queue)

# using it as a stack also
queue.popleft()
print(queue)

queue.appendleft(32)
print(queue)

queue.pop()
print(queue)


