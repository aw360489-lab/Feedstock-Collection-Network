# Get execution time with Python’s timeit module
# py -m module4_sorting.testSorting

import random
import time
import numpy as np

from module1_graph.Graph import DSAGraph
from module4_sorting.CollectionRecord import CollectionRecord
from module4_sorting.MergeSort import mergeSort
from module4_sorting.QuickSort import quickSort

# Experiment Settings
RANDOM_SEED = 42
NUMBER_OF_TRIALS = 5


# Build Transportation Graph from Module 1
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

    # Weighted undirected edges

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

    # Vertex I remains isolated

    return graph


# Get shortest transportation time (T) using Dijkstra
def getTransportTime(graph, vertexLabel):

    graph.dijkstra("HUB", vertexLabel)

    vertex = graph.getVertex(vertexLabel)

    return vertex.getDistance()


# Build Farm Information from Module 1
# Each row contains: index 0 = FarmID, index 1 = Graph vertex, index 2 = Dijkstra transportation time

def buildFarmData(graph):

    farmCount = 8
    farmData = np.empty((farmCount, 3), dtype=object)

    # Farm IDs correspond to the graph farms
    farmData[0][0] = "c37f4"
    farmData[0][1] = "A"

    farmData[1][0] = "b8ffa"
    farmData[1][1] = "B"

    farmData[2][0] = "mh4jw"
    farmData[2][1] = "C"

    farmData[3][0] = "x7jvy"
    farmData[3][1] = "D"

    farmData[4][0] = "c2vzt"
    farmData[4][1] = "E"

    farmData[5][0] = "bdcc7"
    farmData[5][1] = "F"

    farmData[6][0] = "b51b4"
    farmData[6][1] = "G"

    farmData[7][0] = "df2e4"
    farmData[7][1] = "H2"

    # Calculate transportation times using Dijkstra

    ii = 0

    while ii < farmCount:

        vertexLabel = (farmData[ii][1])
        transportTime = (getTransportTime(graph, vertexLabel))

        farmData[ii][2] = (transportTime)

        ii = ii + 1

    return farmData


# Display Dijkstra Transportation Times
def displayFarmData(farmData):

    print()
    print("=" * 65)
    print("DIJKSTRA TRANSPORTATION TIMES")
    print("=" * 65)

    ii = 0

    while ii < len(farmData):
        print("FarmID:", farmData[ii][0], "| Vertex:", farmData[ii][1], "| T:", farmData[ii][2], "minutes")
        ii = ii + 1


# Generate Collection Records
def generateRecords(size, farmData, seed):

    # Use a fixed random seed for reproducibility
    random.seed(seed)

    records = np.empty(size, dtype=object)

    ii = 0

    while ii < size:

        # Randomly select one of the reachable farms
        farmIdx = random.randint(0, len(farmData) - 1)
        farmID = (farmData[farmIdx][0])
        transportTime = (farmData[farmIdx][2])

        # Educational modelling value for estimated feedstock in kilograms
        estimatedFeedstock = (random.randint(500, 5000))

        recordID = ("R" + str(ii + 1))
        records[ii] = (CollectionRecord(recordID, farmID, estimatedFeedstock, transportTime))
        ii = ii + 1

    return records


# Copy Array - Used for Random Input
def copyArray(source):

    copied = np.empty(len(source), dtype=object)
    ii = 0

    while ii < len(source):
        copied[ii] = source[ii]
        ii = ii + 1

    return copied


# Reverse Array Manually
def reverseArray(A):

    leftIdx = 0
    rightIdx = len(A) - 1

    while leftIdx < rightIdx:

        temp = A[leftIdx]
        A[leftIdx] = A[rightIdx]
        A[rightIdx] = temp

        leftIdx = leftIdx + 1
        rightIdx = rightIdx - 1


# Test Three conditions: Random, Nearly sorted (≤ 10% of records displaced), Reversed

# Create Random Input
def createRandomInput(baseRecords):
    # The generated dataset is already in random order
    return copyArray(baseRecords)


# Create Nearly Sorted Input - No more than 10% of records are displaced
def createNearlySortedInput(baseRecords, seed):

    records = copyArray(baseRecords)

    # Create sorted baseline using Merge Sort
    mergeSort(records)

    random.seed(seed)

    # 10% of the records are selected for displacement
    displacedCount = (len(records) // 10)

    # Ensure an even number so records can be displaced in pairs
    if displacedCount % 2 != 0:
        displacedCount = (displacedCount - 1)

    swapCount = (displacedCount // 2)

    ii = 0

    while ii < swapCount:
        firstIdx = (ii * 2)
        secondIdx = (firstIdx + 1)

        # Move one of the selected positions to another position in the array
        randomIdx = random.randint(secondIdx, len(records) - 1)

        temp = records[firstIdx]
        records[firstIdx] = (records[randomIdx])
        records[randomIdx] = temp

        temp = records[secondIdx]
        records[secondIdx] = (records[len(records) - 1 - ii])
        records[len(records) - 1 - ii] = temp

        ii = ii + 1

    return records


# Create Reversed Input
def createReversedInput(baseRecords):

    records = copyArray(baseRecords)

    # Create sorted baseline using Merge Sort
    mergeSort(records)

    # Reverse array
    reverseArray(records)

    return records


# Check Whether Records Are Correctly Sorted
def isSorted(A):

    sortedCorrectly = True
    ii = 1

    while (ii < len(A) and sortedCorrectly):
        previousTime = (A[ii - 1].getTransportTime())
        currentTime = (A[ii].getTransportTime())

        if previousTime > currentTime:
            sortedCorrectly = False

        ii = ii + 1

    return sortedCorrectly


# Benchmark Merge Sort
def benchmarkMergeSort(original, trials):

    totalTime = 0.0
    ii = 0

    while ii < trials:

        testData = copyArray(original)

        startTime = (time.perf_counter())
        mergeSort(testData)
        endTime = (time.perf_counter())

        totalTime = (totalTime + (endTime - startTime))

        ii = ii + 1

    averageTime = (totalTime / trials)

    return (averageTime, isSorted(testData))


# Benchmark Quick Sort
def benchmarkQuickSort(original, trials):

    totalTime = 0.0
    ii = 0

    while ii < trials:

        testData = copyArray(original)

        startTime = (time.perf_counter())
        quickSort(testData)
        endTime = (time.perf_counter())
        
        totalTime = (totalTime + (endTime - startTime))

        ii = ii + 1

    averageTime = (totalTime / trials)

    return (averageTime, isSorted(testData))


# Run One Benchmark Condition
def runCondition(size, conditionName, records):

    mergeTime, mergeCorrect = (benchmarkMergeSort(records, NUMBER_OF_TRIALS))
    quickTime, quickCorrect = (benchmarkQuickSort(records, NUMBER_OF_TRIALS))

    print(
        str(size).ljust(8),
        conditionName.ljust(18),
        format(mergeTime * 1000, ".6f").ljust(18),
        format(quickTime * 1000, ".6f").ljust(18),
        str(mergeCorrect and quickCorrect)
    )


# Display Sorted Records
def displaySortedSample(records, numberToDisplay):

    sample = copyArray(records)
    mergeSort(sample)

    print()
    print("=" * 65)
    print("SAMPLE OF CORRECTLY SORTED RECORDS")
    print("=" * 65)

    previousTime = None
    ii = 0

    while ii < len(sample):
        record = sample[ii]
        currentTime = record.getTransportTime()

        if previousTime is None or currentTime != previousTime:
            print(record)
            previousTime = currentTime

        ii += 1
        

# Run Sorting Experiments
def runSortingTests():

    print("=" * 60)
    print("MODULE 4 - COLLECTION RECORDS")
    print("=" * 60)

    # Build graph and calculate shortest-path times
    graph = buildGraph()
    farmData = buildFarmData(graph)

    displayFarmData(farmData)

    # Benchmark Header
    print()
    print("=" * 60)
    print("SORTING PERFORMANCE RESULTS")
    print("=" * 60)

    print(
        "Size".ljust(8),
        "Condition".ljust(18),
        "Merge Sort (ms)".ljust(18),
        "Quick Sort (ms)".ljust(18),
        "Correct"
    )

    print("-" * 60)

    # Dataset size: 100
    base100 = generateRecords(100, farmData, RANDOM_SEED)

    random100 = (createRandomInput(base100))
    nearly100 = (createNearlySortedInput(base100, RANDOM_SEED))
    reversed100 = (createReversedInput(base100))

    runCondition(100, "Random", random100)
    runCondition(100, "Nearly Sorted", nearly100)
    runCondition(100, "Reversed", reversed100)

    # Dataset size: 500
    base500 = generateRecords(500, farmData, RANDOM_SEED)

    random500 = (createRandomInput(base500))
    nearly500 = (createNearlySortedInput(base500, RANDOM_SEED))
    reversed500 = (createReversedInput(base500))

    runCondition(500, "Random", random500)
    runCondition(500, "Nearly Sorted", nearly500)
    runCondition(500, "Reversed", reversed500)

    # Dataset size: 1000
    base1000 = generateRecords(1000, farmData, RANDOM_SEED)

    random1000 = (createRandomInput(base1000))
    nearly1000 = (createNearlySortedInput(base1000, RANDOM_SEED))
    reversed1000 = (createReversedInput(base1000))

    runCondition(1000, "Random", random1000)
    runCondition(1000, "Nearly Sorted", nearly1000)
    runCondition(1000, "Reversed", reversed1000)

    # Display correctly sorted sample
    displaySortedSample(random100, 15)


# Main
if __name__ == "__main__":
    runSortingTests()