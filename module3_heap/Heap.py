# Heap (binary tree): Calculate Priority,
# Insert, Peek, Extract: Remove and return the highest priority, Trickle Up, Trickle Down

# Define F (Estimated Feedstock) - CollectionRequest.py, F values: testHeap.py
# Get T (Shortest Estimated Transportation Time) + Calculate Priority - testHeap.py

import numpy as np

# Heap Entry
class DSAHeapEntry:

    def __init__(self, priority, value):
        self.priority = priority
        self.value = value

    def getPriority(self):
        return self.priority

    def setPriority(self, priority):
        self.priority = priority

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value


# Array-Based Binary Max Heap
class DSAHeap:

    def __init__(self, maxSize):

        self.heap = np.empty(maxSize, dtype=object)
        ii = 0

        while ii < maxSize:
            self.heap[ii] = None
            ii = ii + 1

        self.count = 0


    # Insert
    def insert(self, request):

        if request is None:
            raise ValueError("Collection request cannot be empty")

        if self.count >= len(self.heap):
            raise ValueError("Heap is full")

        priority = request.getPriority()

        newEntry = DSAHeapEntry(priority, request)

        # Insert the new entry at the end
        self.heap[self.count] = newEntry

        # Restore max-heap property
        self.trickleUp(self.count)
        self.count = self.count + 1

        print("Inserted:", request.getFarmID(), "| Priority:", round(priority, 2))

        self.display()


    # Peek
    def peek(self):

        if self.count == 0:
            print("PEEK FAILED: Heap is empty")
            return None

        return self.heap[0].getValue()


    # Remove and return the highest-priority collection request

    def extractPriority(self):

        if self.count == 0:
            print("EXTRACTION FAILED: Heap is empty")
            return None

        # Save the highest-priority entry
        root = self.heap[0]
        self.count = self.count - 1

        if self.count > 0:

            # Move the last element to the root
            self.heap[0] = (self.heap[self.count])
            self.heap[self.count] = None

            # Restore max-heap property
            self.trickleDown(0)

        else:
            self.heap[0] = None

        print("Extracted:", root.getValue().getFarmID(), "| Priority:", round(root.getPriority(), 2))

        self.display()

        return root.getValue()


    # Trickle Up: Percolation after insertion

    def trickleUp(self, curIdx):

        while curIdx > 0:
            parentIdx = (curIdx - 1) // 2

            if (self.heap[curIdx].getPriority() > self.heap[parentIdx].getPriority()):

                # Swap current element with parent element
                temp = self.heap[parentIdx]
                self.heap[parentIdx] = self.heap[curIdx]
                self.heap[curIdx] = temp

                curIdx = parentIdx

            else:
                # Setting the index to zero ends
                curIdx = 0


    # Trickle Down: Percolation after extraction (Remove)

    def trickleDown(self, index):

        curIdx = index
        keepGoing = True

        while keepGoing:
            leftChildIdx = (curIdx * 2) + 1
            rightChildIdx = (leftChildIdx + 1)

            keepGoing = False

            # Trickle down to the child with larger index

            if leftChildIdx < self.count:
                largeIdx = leftChildIdx

                if rightChildIdx < self.count:

                    if (self.heap[rightChildIdx].getPriority() > self.heap[leftChildIdx].getPriority()):

                        largeIdx = (rightChildIdx)

                if (self.heap[largeIdx].getPriority() > self.heap[curIdx].getPriority()):

                    # Swap large element with current element
                    temp = self.heap[curIdx]
                    self.heap[curIdx] = self.heap[largeIdx]
                    self.heap[largeIdx] = temp

                    curIdx = largeIdx
                    keepGoing = True


    # Duplicate Request Check: Same FarmID + Same EstimatedFeedstock
    # If any one is different (same ID + different stock or different ID + same stock), it is not duplicate

    def hasRequest(self, farmID, estimatedFeedstock):

        found = False
        ii = 0

        while (ii < self.count and not found):
            request = (self.heap[ii].getValue())

            if (request.getFarmID() == farmID and request.getEstimatedFeedstock() == estimatedFeedstock):

                found = True

            ii = ii + 1

        return found


    # Heap Information
    def isEmpty(self):
        return self.count == 0


    def getCount(self):
        return self.count


    # Display Heap Array
    def display(self):

        print("Heap Array:")

        if self.count == 0:

            print("[EMPTY]")

        else:
            ii = 0

            while ii < self.count:

                request = (self.heap[ii].getValue())

                print("Index", ii, "|", request.getFarmID(), "| Priority:", round(self.heap[ii].getPriority(), 2))

                ii = ii + 1

        print("--------------------------------")