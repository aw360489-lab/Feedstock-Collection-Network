# py interactive_menu.py

import subprocess
import sys


def runModule(moduleName):

    subprocess.run(
        [sys.executable, "-m", moduleName],
        check=False
    )


def main():

    running = True

    while running:

        print("\nBIOGAS FEEDSTOCK COLLECTION SYSTEM")
        print("1. Graph - Transport Network")
        print("2. Hash Table")
        print("3. Heap-Based Feedstock Collection Scheduling")
        print("4. Sorting Collection Records")
        print("5. Run All Modules")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            runModule("module1_graph.testGraph")

        elif choice == "2":
            runModule("module2_hash.testHash")

        elif choice == "3":
            runModule("module3_heap.testHeap")

        elif choice == "4":
            runModule("module4_sorting.testSorting")

        elif choice == "5":

            runModule("module1_graph.testGraph")
            runModule("module2_hash.testHash")
            runModule("module3_heap.testHeap")
            runModule("module4_sorting.testSorting")

        elif choice == "0":
            running = False

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()