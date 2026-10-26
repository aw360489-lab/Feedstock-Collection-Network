# Define F (Estimated Feedstock) with values
# Get T (Shortest Estimated Transportation Time) with Dijkstra in Graph
# Calculate Priority = F / T

# Command: In Ass folder, py -m module3_heap.testHeap
# Beause import module_1 and module_2

import csv

from module1_graph.Graph import DSAGraph
from module2_hash.Hash import DSAHashTable
from module2_hash.FarmRecord import FarmRecord
from module3_heap.Heap import DSAHeap
from module3_heap.CollectionRequest import CollectionRequest

# Build Transportation Graph

def buildGraph():

    graph = DSAGraph()

    graph.addVertex("HUB", "Proposed Mount Barker Biogas Hub")
    graph.addVertex("A", "Mount Barker Regional Saleyards")
    graph.addVertex("B", "Mt Barker Chicken - Barker Creek")
    graph.addVertex("C", "Unknown Free Range Piggery")
    graph.addVertex("D", "Geza Feedlot")
    graph.addVertex("E", "Mungrup Stud")
    graph.addVertex("F", "Fletcher International Abattoir")
    graph.addVertex("G", "Albany Farm Fresh Eggs")
    graph.addVertex("H2", "Marbelup Pork")
    graph.addVertex("I", "Unknown Grower Piggery - Cranbrook")

    # Add weighted undirected transportation connections

    graph.addEdge("HUB", "A", 4)
    graph.addEdge("HUB", "E", 18)
    graph.addEdge("A", "B", 5)
    graph.addEdge("A", "C", 27)
    graph.addEdge("B", "C", 22)
    graph.addEdge("C", "D", 7)
    graph.addEdge("D", "F", 13)
    graph.addEdge("D", "G", 19)
    graph.addEdge("E", "F", 6)
    graph.addEdge("E", "H2", 16)
    graph.addEdge("F", "G", 8)
    graph.addEdge("G", "H2", 9)

    # Vertex I intentionally remains isolated

    return graph


# Load Farms into Hash Table

def loadHashTable(fileName):

    # Initial size 11 demonstrates resizing

    hashTable = DSAHashTable(11)

    try:
        with open(fileName, "r", encoding="utf-8-sig", newline="") as csvFile:
            reader = csv.reader(csvFile)

            # Ignore header row
            header = next(reader, None)

            for row in reader:
                try:
                    if len(row) >= 20:

                        record = FarmRecord(
                            row[0],
                            row[1],
                            row[2],
                            row[3],
                            float(row[4]),
                            float(row[5]),
                            row[6],
                            row[7],
                            row[8],
                            row[9],
                            row[10],
                            row[11],
                            row[12],
                            row[13],
                            row[14],
                            row[15],
                            row[16],
                            row[17],
                            row[18],
                            row[19]
                        )

                        hashTable.insert(record)

                except ValueError as error:
                    print("Invalid farm record:", error)

    except FileNotFoundError:
        print("Farm CSV file was not found.")

    return hashTable


# Find Graph Vertex Using Farm Name

def findGraphVertex(graph, farmName):

    currentNode = graph.vertices.head
    foundLabel = None

    while (currentNode is not None and foundLabel is None):

        vertex = currentNode.getValue()

        if vertex.getValue() == farmName:
            foundLabel = (vertex.getLabel())

        currentNode = (currentNode.getNext())

    return foundLabel


# Process Collection Request

def processRequest(hashTable, graph, heap, farmID, estimatedFeedstock):

    print()
    print("PROCESSING REQUEST:", farmID, "| Feedstock:", estimatedFeedstock, "kg")


    # Validate EstimatedFeedstock

    if not isinstance(estimatedFeedstock, (int, float)):
        print(
            "REQUEST REJECTED:"
            " Feedstock must be numerical."
        )

        return False

    if estimatedFeedstock <= 0:
        print(
            "REQUEST REJECTED:"
            " Feedstock must be greater than zero."
        )

        return False

    # Check Duplicate Collection Request

    if heap.hasRequest(farmID, estimatedFeedstock):
        print(
            "REQUEST REJECTED:"
            " Duplicate collection request."
        )

        return False
    
    # Retrieve Farm from Hash Table

    farmRecord = (hashTable.search(farmID))

    if farmRecord is None:
        print(
            "REQUEST REJECTED:"
            " Farm record is unavailable."
        )

        return False

    print("Farm:", farmRecord.getName())

    # Find Corresponding Graph Vertex

    graphLabel = findGraphVertex(graph, farmRecord.getName())

    if graphLabel is None:
        print(
            "REQUEST REJECTED:"
            " Farm is not represented"
            " in the transportation network."
        )

        return False

    print("Graph location:", graphLabel)

    # Use Dijkstra in Graph to get the shortest path - shortest estimated transportation time from HUB to Farm

    graph.dijkstra("HUB", graphLabel)

    destinationVertex = (graph.getVertex(graphLabel))

    transportTime = (destinationVertex.getDistance())

    # Handle Unreachable Farm

    if transportTime == float("inf"):
        print(
            "REQUEST REJECTED:"
            " A valid collection route"
            " cannot currently be calculated."
        )

        return False

    # Handle Zero Transportation Time

    if transportTime <= 0:
        print(
            "REQUEST REJECTED:"
            " Transportation time must"
            " be greater than zero."
        )

        return False

    # Calculate Priority = F / T

    priority = (estimatedFeedstock / transportTime)

    print()
    print("PRIORITY CALCULATION:")

    print("F =", estimatedFeedstock, "kg")

    print("T =", transportTime, "minutes")

    print("Priority = F / T =", round(priority, 2))
    print()

    # Create Collection Request

    request = CollectionRequest(farmID, estimatedFeedstock)

    request.setFarmName(farmRecord.getName())
    request.setTransportTime(transportTime)
    request.setPriority(priority)

    # Insert into Max Heap
    heap.insert(request)

    return True


# Run Tests
def runHeapTests():

    print("=" * 65)
    print(
        "MODULE 3 - HEAP-BASED"
        " FEEDSTOCK COLLECTION SCHEDULING"
    )
    print("=" * 65)

    # Build Previous Modules

    graph = buildGraph()
    hashTable = loadHashTable("data/selected_southern_wa_farms.csv")
    heap = DSAHeap(20)

    # Define the values of Estimated Feedstock

    # Test 1: Ten Valid Heap Insertions
    print()
    print("\nTEST 1: TEN HEAP INSERTIONS")

    processRequest(hashTable, graph, heap, "c37f4", 2400)
    processRequest(hashTable, graph, heap, "b8ffa", 1800)
    processRequest(hashTable, graph, heap, "mh4jw", 3200)
    processRequest(hashTable, graph, heap, "x7jvy", 4100)
    processRequest(hashTable, graph, heap, "c2vzt", 2800)
    processRequest(hashTable, graph, heap, "bdcc7", 3500)
    processRequest(hashTable, graph, heap, "b51b4", 4000)
    processRequest(hashTable, graph, heap, "df2e4", 2200)

    # Same farm + different feedstock quantity represents a different collection request (not duplicate)

    processRequest(hashTable, graph, heap, "c37f4", 1500)
    processRequest(hashTable, graph, heap, "c2vzt", 4500)


    # Test 2: Peek Highest Priority
    print()
    print("\nTEST 2: PEEK HIGHEST PRIORITY")

    highestRequest = heap.peek()

    if highestRequest is not None:
        print("Highest-priority request:")
        print(highestRequest)


    # Test 3: Unreachable Farm
    print()
    print("\nTEST 3: UNREACHABLE FARM")

    processRequest(hashTable, graph, heap, "bo79t", 3000)


    # Test 4: Invalid FarmID
    print()
    print("\nTEST 4: INVALID FARM ID")

    processRequest(hashTable, graph, heap, "INVALID", 2000)


    # Test 5: Invalid Feedstock - Zero
    print()
    print("\nTEST 5: ZERO FEEDSTOCK")

    processRequest(hashTable, graph, heap, "c37f4", 0)


    # Test 6: Invalid Feedstock - Negative
    print()
    print("\nTEST 6: NEGATIVE FEEDSTOCK")

    processRequest(hashTable, graph, heap, "c37f4", -500)


    # Test 7: Invalid Feedstock Type
    print()
    print("\nTEST 7: NON-NUMERICAL FEEDSTOCK")

    processRequest(hashTable, graph, heap, "c37f4", "invalid")


    # Test 8: Duplicate Collection Request
    print()
    print("\nTEST 8: DUPLICATE COLLECTION REQUEST")

    processRequest(hashTable, graph, heap, "c37f4", 2400)


    # Test 9: Deleted Farm Record
    print()
    print("\nTEST 9: DELETED FARM RECORD")

    hashTable.delete("mh4jw")

    # Check the deleted record - should not be found
    processRequest(hashTable, graph, heap, "mh4jw", 2500)


    # Test 10: Five Priority Extractions
    print()
    print("\nTEST 10: FIVE PRIORITY EXTRACTIONS")

    extractionNumber = 1

    while extractionNumber <= 5:

        print()
        print("Collection Order", extractionNumber)

        request = (heap.extractPriority())

        if request is not None:
            print("Scheduled:", request)

        extractionNumber = (extractionNumber + 1)


    # Test 11: Remaining Heap
    print()
    print("\nTEST 11: REMAINING HEAP")

    heap.display()


    # Test 12: Empty Heap
    print()
    print("\nTEST 12: EMPTY HEAP")

    while not heap.isEmpty():
        heap.extractPriority()

    # Attempt extraction from empty heap
    heap.extractPriority()

    # Attempt peek from empty heap
    heap.peek()


# Main
if __name__ == "__main__":
    runHeapTests()