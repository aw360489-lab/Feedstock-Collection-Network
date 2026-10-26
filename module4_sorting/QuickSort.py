# Sort T (Shortest Estimated Transportation Time) in Ascending order
# Quick Sort: Pivot Selection - Median of three

def quickSort(A):
    quickSortMedian3Recurse(A, 0, len(A) - 1)


# Median-of-Three Quick Sort
def quickSortMedian3Recurse(A, leftIdx, rightIdx):

    if rightIdx > leftIdx:

        midIdx = (leftIdx + rightIdx) // 2

        # Obtain transportation times for: first, middle, and last records

        leftTime = (A[leftIdx].getTransportTime())
        midTime = (A[midIdx].getTransportTime())
        rightTime = (A[rightIdx].getTransportTime())


        # Select the median of first, middle, and last
        if leftTime <= midTime:

            if midTime <= rightTime:
                pivotIdx = midIdx

            elif leftTime <= rightTime:
                pivotIdx = rightIdx

            else:
                pivotIdx = leftIdx

        else:
            if leftTime <= rightTime:
                pivotIdx = leftIdx

            elif midTime <= rightTime:
                pivotIdx = rightIdx

            else:
                pivotIdx = midIdx

        # Partition
        newPivotIdx = doPartitioning(A, leftIdx, rightIdx, pivotIdx)

        # Sort the left partition
        quickSortMedian3Recurse(A, leftIdx, newPivotIdx - 1)

        # Sort the right partition
        quickSortMedian3Recurse(A, newPivotIdx + 1, rightIdx)


# Partitioning
def doPartitioning(A, leftIdx, rightIdx, pivotIdx):

    # Save the pivot record
    pivotRecord = A[pivotIdx]
    pivotTime = (pivotRecord.getTransportTime())

    # Move the pivot to the right-most position
    A[pivotIdx] = A[rightIdx]
    A[rightIdx] = pivotRecord

    currIdx = leftIdx
    ii = leftIdx

    # Move records with smaller transportation times to the left side of the pivot
    while ii < rightIdx:

        currentTime = (A[ii].getTransportTime())

        if currentTime < pivotTime:

            temp = A[ii]
            A[ii] = A[currIdx]
            A[currIdx] = temp

            currIdx = currIdx + 1

        ii = ii + 1

    # Move pivot into its correct position
    newPivotIdx = currIdx

    A[rightIdx] = A[newPivotIdx]
    A[newPivotIdx] = pivotRecord

    return newPivotIdx