# Singly-linked list: head, value + next

class DSAListNode:
    def __init__(self, inValue):
        self.value = inValue
        self.next = None

    def getValue(self):
        return self.value

    def setValue(self, inValue):
        self.value = inValue

    def getNext(self):
        return self.next

    def setNext(self, newNext):
        self.next = newNext


class DSALinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None
    
    def insertFirst(self, newValue):
        newNd = DSAListNode(newValue)

        if self.isEmpty():
            self.head = newNd
        else:
            newNd.setNext(self.head)
            self.head = newNd

    def insertLast(self, newValue):
        newNd = DSAListNode(newValue)

        if self.isEmpty():
            self.head = newNd
        else:
            currNd = self.head

            while currNd.getNext() is not None:
                currNd = currNd.getNext()

            currNd.setNext(newNd)

    def peekFirst(self):
        if self.isEmpty():
            raise Exception("List is empty")
        return self.head.getValue()

    def peekLast(self):
        if self.isEmpty():
            raise Exception("List is empty")
        
        currNd = self.head

        while currNd.getNext() is not None:
            currNd = currNd.getNext()

        return currNd.getValue()

    def removeFirst(self):
        if self.isEmpty():
            raise Exception("List is empty")
        
        nodeValue = self.head.getValue()
        self.head = self.head.getNext()

        return nodeValue

    def removeLast(self):
        if self.isEmpty():
            raise Exception("List is empty")

        # Case 1: only one node
        if self.head.getNext() is None:
            nodeValue = self.head.getValue()
            self.head = None

        # Case 2: multiple nodes
        else:
            prevNd = None
            currNd = self.head

            # Traverse to the last node
            while currNd.getNext() is not None:
                prevNd = currNd
                currNd = currNd.getNext()

            prevNd.setNext(None)
            nodeValue = currNd.getValue()

        return nodeValue
