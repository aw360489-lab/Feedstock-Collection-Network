# Biogas Feedstock Collection Network

**Data Structures and Algorithms for Sustainable Waste Management**

## 1. Project Overview

This project implements a biogas feedstock collection management prototype using custom data structures and algorithms in Python. It models a transportation network connecting selected farms in southern Western Australia to a proposed biogas hub.

The system consists of four integrated modules:

- **Module 1 – Graph:** Implements an adjacency-list graph, BFS, DFS - cycle detection, and Dijkstra's shortest-path algorithm.
- **Module 2 – Hash Table:** Implements farm record insertion, searching, deletion, linear probing, and resizing.
- **Module 3 – Max Heap:** Schedules feedstock collection requests using priority \(P = F/T\), where \(F\) is estimated feedstock and \(T\) is the shortest transportation time caculated by Dijkstra.
- **Module 4 – Sorting:** Implements top-down Merge Sort and median-of-three Quick Sort to sort collection records by transportation time in ascending order.

## 2. Requirements

- Python 3
- NumPy

Install NumPy:

```bash
py -m pip install numpy
```

## 3. Project Structure

```text
Ass/
├── README.md
├── interactive_menu.py
├── data/
│   └── selected_southern_wa_farms.csv
    └── graph_vertices.csv
    └── transport_network.csv
    └── Data.py
    └── Transport.py
├── module1_graph/
│   └── Graph.py
    └── LinkedList.py
    └── Queue.py
    └── testGraph.py
├── module2_hash/
│   └── Hash.py
    └── FarmRecord.py
    └── testHash.py
├── module3_heap/
│   └── Heap.py
    └── CollectionRequest.py
    └── testHeap.py
├── module4_sorting/
│   └── MergeSort.py
    └── QuickSort.py
    └── CollectionRecord.py
    └── testSorting.py
└── sample_output/
│   └── Graph_Transport_Network.jpg
    └── module1_graph_output.txt
    └── module2_hash_output.txt
    └── module3_heap_output.txt
    └── module4_sorting_output.txt
```

## 4. Dataset

The dataset was obtained from the Farm Transparency website and filtered to a study region in southern Western Australia.

The selected CSV contains **76 farm records**.

The transportation network contains 9 selected farms and 1 hypothetical biogas hub. Edge weights represent estimated travel times.

`selected_southern_wa_farms.csv`: 76 farms

`graph_vertices.csv`: 10 vertices - 9 selected farms + hub 

`transport_network.csv`: 12 edges - Distance + TransportTime

Educational Modelling Data (Simulation data): 

`TransportTime`: Defined in `data/Transport.py`, output in `transport_network.csv`, used for transportation network.

`EstimatedFeedstock` quantity (F): Defined in `module3_heap/CollectionRequest.py, testHeap.py`

`CollectionPriority` (F /T): Caculated in `module3_heap/testHeap.py`, T (Shortest Estimated Transportation Time) was got by Dijkstra in Graph.

## 5. How to Run

Open a terminal in the project root directory (`Ass/`).

Run each module independently:

```bash
python -m module1_graph.testGraph
python -m module2_hash.testHash
python -m module3_heap.testHeap
python -m module4_sorting.testSorting
```

The optional interactive menu is included:

```bash
python interactive_menu.py
```

## 6. Testing

Each module includes a test script covering its main operations and edge cases.

Module 4 benchmarks both sorting algorithms using **100, 500, and 1,000 collection records**, under three conditions:

- Random
- Nearly sorted (no more than 10% displaced)
- Reversed

A fixed random seed (`42`) is used for reproducibility. Transportation times (T) are derived from Module 1 Dijkstra shortest paths.

Actual test results and timings are saved in the `sample_output/` directory.

```bash
python -m module1_graph.testGraph > sample_output/module1_graph_output.txt
python -m module2_hash.testHash > sample_output/module2_hash_output.txt
python -m module3_heap.testHeap > sample_output/module3_heap_output.txt
python -m module4_sorting.testSorting > sample_output/module4_sorting_output.txt
```

## 7. Conclusion

The project demonstrates how graphs, hash tables, heaps, and sorting algorithms can work together to support farm lookup, transportation analysis, collection scheduling, and performance evaluation in a sustainable waste-management system.