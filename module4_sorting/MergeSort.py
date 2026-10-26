# Sorting Key: T (Shortest Estimated Transportation Time) in Ascending order
# Merge Sort: Top-down

import numpy as np

def mergeSort(A):
    # Start by sorting the whole array
    mergeSortRecurse(A, 0, len(A) - 1)


# Recursive Splitting
def mergeSortRecurse(A, leftIdx, rightIdx):

    # Continue only when more than one element exists
    if leftIdx < rightIdx:

        # Find the middle index
        midIdx = (leftIdx + rightIdx) // 2

        # Sort the left half
        mergeSortRecurse(A, leftIdx, midIdx)

        # Sort the right half
        mergeSortRecurse(A, midIdx + 1, rightIdx)

        # Merge the sorted halves
        merge(A, leftIdx, midIdx, rightIdx)


# Merge
def merge(A, leftIdx, midIdx, rightIdx):

    tempSize = (rightIdx - leftIdx + 1)
    tempArr = np.empty(tempSize, dtype=object)

    # Index for the left sub-array
    ii = leftIdx

    # Index for the right sub-array
    jj = midIdx + 1

    # Index for the temporary array
    kk = 0

    # Merge the two sorted sub-arrays
    while (ii <= midIdx and jj <= rightIdx):

        leftTime = (A[ii].getTransportTime())
        rightTime = (A[jj].getTransportTime())

        # <= preserves the original order of records with equal transportation times, making Merge Sort stable

        if leftTime <= rightTime:
            tempArr[kk] = A[ii]
            ii = ii + 1

        else:
            tempArr[kk] = A[jj]
            jj = jj + 1

        kk = kk + 1

    # Copy remaining elements from the left half
    while ii <= midIdx:

        tempArr[kk] = A[ii]
        ii = ii + 1
        kk = kk + 1

    # Copy remaining elements from the right half
    while jj <= rightIdx:

        tempArr[kk] = A[jj]
        jj = jj + 1
        kk = kk + 1

    # Copy the sorted temporary array back into A
    kk = leftIdx

    while kk <= rightIdx:
        
        A[kk] = tempArr[kk - leftIdx]
        kk = kk + 1