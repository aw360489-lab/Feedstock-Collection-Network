# py -m module1_graph.testGraph

from module1_graph.Graph import DSAGraph
import matplotlib.pyplot as plt

# Build Test Graph
def buildTestGraph():

    graph = DSAGraph()

    # Add 10 vertices: 9 farms + 1 hub

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

    # Add 12 weighted undirected edges
    # Weight = estimated transport time in minutes, from data\Transport.py, transport_network.csv

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

    # One isolated Vertex I intentionally has no edges

    return graph


def displayVisualGraph():
    # Fixed coordinates are used only for visualisation
    positions = {
        "HUB": (0, 2),
        "A": (2, 3),
        "B": (4, 4),
        "C": (5, 3),
        "D": (6, 1),
        "E": (2, 0),
        "F": (4, 0),
        "G": (6, 0),
        "H2": (4, -2),
        "I": (8, 4)
    }

    edges = (
        ("HUB", "A", 4),
        ("HUB", "E", 18),
        ("A", "B", 5),
        ("A", "C", 27),
        ("B", "C", 22),
        ("C", "D", 7),
        ("D", "F", 13),
        ("D", "G", 19),
        ("E", "F", 6),
        ("E", "H2", 16),
        ("F", "G", 8),
        ("G", "H2", 9)
    )

    plt.figure(figsize=(10, 7))

    # Draw edges and edge weights
    edgeIndex = 0

    while edgeIndex < len(edges):

        source = edges[edgeIndex][0]
        destination = edges[edgeIndex][1]
        weight = edges[edgeIndex][2]

        x1 = positions[source][0]
        y1 = positions[source][1]

        x2 = positions[destination][0]
        y2 = positions[destination][1]

        plt.plot((x1, x2), (y1, y2), linewidth=1.5)

        middleX = (x1 + x2) / 2
        middleY = (y1 + y2) / 2

        plt.text(middleX, middleY, str(weight) + " min", fontsize=9)

        edgeIndex = edgeIndex + 1

    # Draw vertices
    vertexLabels = ("HUB", "A", "B", "C", "D", "E", "F", "G", "H2", "I")
    vertexIndex = 0

    while vertexIndex < len(vertexLabels):

        label = vertexLabels[vertexIndex]

        x = positions[label][0]
        y = positions[label][1]

        plt.scatter(x, y, s=900)

        plt.text(x, y, label, ha="center", va="center")

        vertexIndex = vertexIndex + 1

    # Label the isolated location
    plt.text(
        positions["I"][0],
        positions["I"][1] - 0.6,
        "Isolated Location",
        ha="center",
        fontsize=9
    )

    plt.title("Biogas Feedstock Transportation Test Network")

    plt.axis("off")
    plt.tight_layout()
    plt.show()


# Run Tests
def runGraphTests():

    print("=" * 60)    
    print("MODULE 1 - GRAPH-BASED FARM NETWORK")
    print("=" * 60)

    graph = buildTestGraph()

    # Test 1: Graph construction
    print("\nTEST 1: GRAPH CONSTRUCTION\n")

    print("Number of vertices:", graph.getVertexCount())
    print("Number of edges:", graph.getEdgeCount())

    graph.displayAsList()
    displayVisualGraph()

    # Test 2: BFS from the hub
    print()
    print("\nTEST 2: BFS FROM HUB")

    graph.breadthFirstSearch("HUB")

    # Test 3: BFS from isolated vertex
    print()    
    print("\nTEST 3: BFS FROM ISOLATED LOCATION")

    graph.breadthFirstSearch("I")

    # Test 4: DFS cycle detection
    print()
    print("\nTEST 4: DFS CYCLE DETECTION")

    graph.depthFirstCycleDetection()

    # Test 5: Dijkstra reachable destination
    print()
    print("\nTEST 5: DIJKSTRA - REACHABLE LOCATION")

    graph.dijkstra("HUB", "G")

    # Test 6: Dijkstra another reachable destination
    print()
    print("\nTEST 6: DIJKSTRA - ANOTHER ROUTE")

    graph.dijkstra("HUB", "D")

    # Test 7: Dijkstra unreachable destination
    print()
    print("\nTEST 7: DIJKSTRA - UNREACHABLE LOCATION")

    graph.dijkstra("HUB", "I")

    # Test 8: Invalid BFS location
    print()
    print("\nTEST 8: INVALID BFS LOCATION\n")

    graph.breadthFirstSearch("INVALID")

    # Test 9: Invalid Dijkstra destination
    print()
    print("\nTEST 9: INVALID DIJKSTRA LOCATION")

    graph.dijkstra("HUB", "INVALID")

    # Test 10: Duplicate vertex
    print()
    print("\nTEST 10: DUPLICATE VERTEX\n")

    try:
        graph.addVertex("A", "Duplicate Farm")

    except ValueError as error:
        print("Expected error:", error)

    # Test 11: Duplicate edge
    print()
    print("\nTEST 11: DUPLICATE EDGE\n")

    try:
        graph.addEdge("HUB", "A", 10)

    except ValueError as error:
        print("Expected error:", error)

    # Test 12: Invalid edge location
    print()
    print("\nTEST 12: INVALID EDGE LOCATION\n")

    try:
        graph.addEdge("HUB", "UNKNOWN", 10)

    except ValueError as error:
        print("Expected error:", error)

    # Test 13: Invalid edge weight
    print()
    print("\nTEST 13: INVALID EDGE WEIGHT\n")

    try:
        graph.addEdge("A", "D", -5)

    except ValueError as error:
        print("Expected error:", error)


# Main
if __name__ == "__main__":
    runGraphTests()