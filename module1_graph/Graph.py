# Graph: Create Transportation Network
# BFS, DFS - Find cycle, Dijkstra’s Algorithm - Find the Shortest Path

# Define transport time in data\Transport.py

from module1_graph.LinkedList import DSALinkedList
from module1_graph.Queue import DSAQueue

# Weighted Edge - Store vertex + weight
class DSAEdge:

    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight

    def getVertex(self):
        return self.vertex

    def getWeight(self):
        return self.weight


# Graph Node
class DSAGraphNode:

    def __init__(self, inLabel, inValue=None):
        self.label = inLabel
        self.value = inValue

        # Custom linked list used as the adjacency list
        self.links = DSALinkedList()

        # Used by graph traversal algorithms
        self.visited = False

        # Used by Dijkstra's algorithm
        self.distance = float("inf")
        self.previous = None

    def getLabel(self):
        return self.label

    def getValue(self):
        return self.value

    def getAdjacent(self):
        return self.links

    def getVisited(self):
        return self.visited

    def setVisited(self):
        self.visited = True

    def clearVisited(self):
        self.visited = False

    def getDistance(self):
        return self.distance

    def setDistance(self, distance):
        self.distance = distance

    def getPrevious(self):
        return self.previous

    def setPrevious(self, previous):
        self.previous = previous

    def isAdjacent(self, vertex):
        current = self.links.head
        found = False

        while current is not None and not found:
            edge = current.getValue()

            if edge.getVertex().getLabel() == vertex.getLabel():
                found = True
            else:
                current = current.getNext()

        return found

    def addEdge(self, vertex, weight):
        newEdge = DSAEdge(vertex, weight)
        self.links.insertLast(newEdge)

    def __str__(self):
        return str(self.label)


# Weighted Undirected Graph
class DSAGraph:

    def __init__(self):
        self.vertices = DSALinkedList()


    # Basic Graph Operations
    def addVertex(self, label, value=None):

        if label is None or label == "":
            raise ValueError("Invalid vertex label")

        if self.hasVertex(label):
            raise ValueError("Vertex " + str(label) + " already exists")

        newVertex = DSAGraphNode(label, value)
        self.vertices.insertLast(newVertex)


    def hasVertex(self, label):

        current = self.vertices.head
        found = False

        while current is not None and not found:

            vertex = current.getValue()

            if vertex.getLabel() == label:
                found = True
            else:
                current = current.getNext()

        return found


    def getVertex(self, label):

        current = self.vertices.head
        result = None

        while current is not None and result is None:

            vertex = current.getValue()

            if vertex.getLabel() == label:
                result = vertex
            else:
                current = current.getNext()

        return result


    def getVertexCount(self):

        count = 0
        current = self.vertices.head

        while current is not None:

            count = count + 1
            current = current.getNext()

        return count


    def getEdgeCount(self):

        count = 0
        current = self.vertices.head

        while current is not None:

            vertex = current.getValue()
            adjacent = vertex.getAdjacent().head

            while adjacent is not None:

                count = count + 1
                adjacent = adjacent.getNext()

            current = current.getNext()

        # Each undirected edge is stored twice
        return count // 2


    def isAdjacent(self, label1, label2):

        vertex1 = self.getVertex(label1)
        vertex2 = self.getVertex(label2)

        result = False

        if vertex1 is not None and vertex2 is not None:
            result = vertex1.isAdjacent(vertex2)

        return result


    def addEdge(self, label1, label2, weight):

        vertex1 = self.getVertex(label1)
        vertex2 = self.getVertex(label2)

        if vertex1 is None:
            raise ValueError("Vertex " + str(label1) + " does not exist")

        if vertex2 is None:
            raise ValueError("Vertex " + str(label2) + " does not exist")
        
        if label1 == label2:
            raise ValueError("A vertex cannot be connected to itself")

        if weight <= 0:
            raise ValueError("Transportation time must be positive")

        if vertex1.isAdjacent(vertex2):
            raise ValueError(
                "Edge between "
                + str(label1)
                + " and "
                + str(label2)
                + " already exists"
            )

        # Store the undirected edge in both directions
        vertex1.addEdge(vertex2, weight)
        vertex2.addEdge(vertex1, weight)


    def clearVisited(self):

        current = self.vertices.head

        while current is not None:

            vertex = current.getValue()
            vertex.clearVisited()

            current = current.getNext()


    # Display Graph
    def displayAsList(self):

        print("\nTRANSPORTATION NETWORK:\n")

        current = self.vertices.head

        while current is not None:

            vertex = current.getValue()

            print(
                vertex.getLabel(),
                "(" + str(vertex.getValue()) + ")",
                end=": "
            )

            adjacent = vertex.getAdjacent().head

            if adjacent is None:
                print("[ISOLATED]", end="")

            else:

                while adjacent is not None:

                    edge = adjacent.getValue()

                    print(
                        edge.getVertex().getLabel()
                        + "("
                        + str(edge.getWeight())
                        + " min)",
                        end=""
                    )

                    if adjacent.getNext() is not None:
                        print(" -> ", end="")

                    adjacent = adjacent.getNext()

            print()

            current = current.getNext()


    # BFS: Search by Level
    def breadthFirstSearch(self, sourceLabel):

        source = self.getVertex(sourceLabel)

        if source is None:
            print("BFS error: source location " + str(sourceLabel) + " does not exist.")

        else:
            self.clearVisited()

            queue = DSAQueue()

            source.setVisited()
            queue.enqueue(source)

            level = 0

            print("\nBREADTH-FIRST SEARCH")
            print("Source:", sourceLabel)

            while not queue.isEmpty():

                # All items currently in the queue belong to the same BFS level
                levelSize = queue.getCount()

                print("Level " + str(level) + ": ", end="")

                processed = 0

                while processed < levelSize:

                    vertex = queue.dequeue()
                    print(vertex.getLabel(), end=" ")

                    adjacent = vertex.getAdjacent().head

                    while adjacent is not None:

                        edge = adjacent.getValue()
                        neighbour = edge.getVertex()

                        if not neighbour.getVisited():

                            neighbour.setVisited()
                            queue.enqueue(neighbour)

                        adjacent = adjacent.getNext()

                    processed = processed + 1

                print()

                level = level + 1


    # DFS: Cycle Detection
    def depthFirstCycleDetection(self):

        self.clearVisited()

        cyclePath = DSALinkedList()

        current = self.vertices.head
        cycleFound = False

        print("\nDEPTH-FIRST SEARCH - CYCLE DETECTION")

        # Restart DFS for each disconnected component
        while current is not None and not cycleFound:

            vertex = current.getValue()

            if not vertex.getVisited():
                activePath = DSALinkedList()
                cycleFound = self._dfsCycle(vertex, None, activePath, cyclePath)

            current = current.getNext()

        if cycleFound:
            print("Cycle exists: Yes")
            print("Detected cycle: ", end="")

            self._displayVertexPath(cyclePath)

        else:
            print("Cycle exists: No")

        return cycleFound


    def _dfsCycle(self, vertex, parent, activePath, cyclePath):

        vertex.setVisited()
        activePath.insertLast(vertex)
        adjacent = vertex.getAdjacent().head
        cycleFound = False

        while adjacent is not None and not cycleFound:

            edge = adjacent.getValue()
            neighbour = edge.getVertex()

            if not neighbour.getVisited():
                cycleFound = self._dfsCycle(neighbour, vertex, activePath, cyclePath)

            else:
                isParent = False

                if parent is not None:

                    if (neighbour.getLabel() == parent.getLabel()):
                        isParent = True

                if not isParent:

                    if self._vertexInPath(activePath, neighbour):

                        self._copyCycle(activePath, neighbour, cyclePath)
                        cycleFound = True

            adjacent = adjacent.getNext()

        if not cycleFound:
            activePath.removeLast()

        return cycleFound


    def _vertexInPath(self, path, targetVertex):

        current = path.head
        found = False

        while current is not None and not found:

            vertex = current.getValue()

            if (vertex.getLabel() == targetVertex.getLabel()):
                found = True

            else:
                current = current.getNext()

        return found


    def _copyCycle(self, activePath, startVertex, cyclePath):

        current = activePath.head
        copying = False

        while current is not None:

            vertex = current.getValue()

            if (vertex.getLabel() == startVertex.getLabel()):
                copying = True

            if copying:
                cyclePath.insertLast(vertex)

            current = current.getNext()

        # Repeat the first vertex to show cycle closure
        cyclePath.insertLast(startVertex)


    def _displayVertexPath(self, path):

        current = path.head

        while current is not None:

            vertex = current.getValue()
            print(vertex.getLabel(), end="")

            if current.getNext() is not None:
                print(" -> ", end="")

            current = current.getNext()

        print()


    # Dijkstra's Algorithm: Find the Shortest Path
    def dijkstra(self, sourceLabel, destinationLabel):

        source = self.getVertex(sourceLabel)
        destination = self.getVertex(destinationLabel)
        valid = True

        if source is None:

            print("\nDijkstra error: source location " + str(sourceLabel) + " does not exist.")
            valid = False

        if destination is None:

            print("\nDijkstra error: destination location " + str(destinationLabel) + " does not exist.")
            valid = False

        resultDistance = None
        resultPath = None

        if valid:

            self._initialiseDijkstra()
            source.setDistance(0)
            searching = True

            while searching:

                currentVertex = (self._getMinimumDistanceVertex())

                if currentVertex is None:
                    searching = False

                elif (currentVertex.getDistance() == float("inf")):
                    searching = False

                else:

                    currentVertex.setVisited()

                    if (currentVertex.getLabel()== destination.getLabel()):
                        searching = False

                    else:

                        adjacent = (
                            currentVertex
                            .getAdjacent()
                            .head
                        )

                        while adjacent is not None:

                            edge = adjacent.getValue()
                            neighbour = edge.getVertex()

                            if not neighbour.getVisited():

                                newDistance = (currentVertex.getDistance() + edge.getWeight())

                                if (newDistance < neighbour.getDistance()):

                                    neighbour.setDistance(newDistance)
                                    neighbour.setPrevious(currentVertex)

                            adjacent = (adjacent.getNext())

            if (destination.getDistance() == float("inf")):

                print("\nDIJKSTRA SHORTEST PATH")
                print("Source:", sourceLabel)
                print("Destination:", destinationLabel)
                print("Result: destination is unreachable from the source.")

                resultDistance = float("inf")

            else:

                resultPath = (self._constructPath(destination))
                resultDistance = (destination.getDistance())

                print("\nDIJKSTRA SHORTEST PATH")
                print("Source:", sourceLabel)
                print("Destination:", destinationLabel)
                print("Shortest path: ", end="")

                self._displayLabelPath(resultPath)

                print("Shortest transportation time:", resultDistance, "minutes")

        return resultDistance, resultPath


    def _initialiseDijkstra(self):

        current = self.vertices.head

        while current is not None:

            vertex = current.getValue()

            vertex.setDistance(float("inf"))
            vertex.setPrevious(None)
            vertex.clearVisited()

            current = current.getNext()


    def _getMinimumDistanceVertex(self):

        current = self.vertices.head

        minimumVertex = None
        minimumDistance = float("inf")

        while current is not None:

            vertex = current.getValue()

            if not vertex.getVisited():

                if (vertex.getDistance() < minimumDistance):

                    minimumDistance = (vertex.getDistance())
                    minimumVertex = vertex

            current = current.getNext()

        return minimumVertex


    def _constructPath(self, destination):

        path = DSALinkedList()
        current = destination

        while current is not None:
            # Insert at the front to avoid reversing a list
            path.insertFirst(current.getLabel())

            current = current.getPrevious()

        return path


    def _displayLabelPath(self, path):

        current = path.head

        while current is not None:

            print(current.getValue(), end="")

            if current.getNext() is not None:
                print(" -> ", end="")

            current = current.getNext()

        print()