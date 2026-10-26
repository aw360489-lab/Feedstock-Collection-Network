# export the output of each traversal
import numpy as np

class DSAQueue:
    DEFAULT_CAPACITY = 100

    def __init__(self, maxCapacity=DEFAULT_CAPACITY):
        self.queue = np.empty(maxCapacity, dtype=object)
        self.count = 0
        self.front = 0
        self.rear = -1

    def getCount(self):
        return self.count

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == len(self.queue)

    def enqueue(self, value):
        if self.isFull():
            raise Exception("Queue is full")

        self.rear = (self.rear + 1) % len(self.queue)
        self.queue[self.rear] = value
        self.count += 1

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue is empty")

        frontVal = self.queue[self.front]
        self.queue[self.front] = None

        self.front = (self.front + 1) % len(self.queue)
        self.count -= 1

        return frontVal

    def peek(self):
        if self.isEmpty():
            raise Exception("Queue is empty")

        return self.queue[self.front]