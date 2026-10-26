# Hash Table: Store and Retrieve farm information
# Insert, Search, Delete, Handle collision - Linear Probing, Load Factor, Resize - Use Prime for table size

import numpy as np

# Hash Table Entry
# State: 0 = never used, 1 = currently used, -1 = formerly used

class DSAHashEntry:

    def __init__(self):
        self.key = ""
        self.value = None
        self.state = 0


# Hash Table
# Collision Strategy: Open Addressing with Linear Probing

class DSAHashTable:

    MAX_LOAD_FACTOR = 0.7

    def __init__(self, tableSize):

        actualSize = self._nextPrime(tableSize)

        # Use NumPy array
        self.hashArray = np.empty(actualSize, dtype=object)

        ii = 0

        while ii < actualSize:
            self.hashArray[ii] = DSAHashEntry()
            ii = ii + 1

        self.count = 0


    # Hash Function
    def _hash(self, inKey):

        hashValue = 0
        ii = 0

        # Convert FarmID (String) to numeric hash (Integer)
        while ii < len(inKey):
            hashValue = (hashValue * 31 + ord(inKey[ii]))
            ii = ii + 1

        # Modulo-based hash function
        hashIdx = (hashValue % len(self.hashArray))

        return hashIdx


    # Load Factor
    def getLoadFactor(self):
        return (self.count / len(self.hashArray))


    # Insert
    # Check load factor, if out of range, rezise table
    def insert(self, record):

        self._validateRecord(record)
        farmID = record.getFarmID()

        # FarmID must be unique
        if self.hasKey(farmID):
            raise ValueError("Duplicate FarmID: " + str(farmID))

        # Determine whether insertion would exceed the maximum load factor
        futureLoadFactor = ((self.count + 1) / len(self.hashArray))

        # Resize when load factor exceeds the threshold - 0.7
        if (futureLoadFactor > self.MAX_LOAD_FACTOR):

            oldSize = len(self.hashArray)
            self._resize(oldSize * 2)

            print("RESIZE:", oldSize, "->", len(self.hashArray))

        self._insertNoResize(farmID, record, True)


    # Internal Insert
    # Only insert data into hash table, no check load factor, no resize
    def _insertNoResize(self, inKey, inValue, showCollision):

        hashIdx = self._hash(inKey)
        originalIdx = hashIdx

        firstDeletedIdx = -1

        searching = True
        inserted = False
        collisionOccurred = False

        if showCollision:
            print("Insert", inKey, "| Initial index:", hashIdx)

        while searching:

            entry = self.hashArray[hashIdx]

            # Never-used position
            if entry.state == 0:
                insertIdx = hashIdx

                if firstDeletedIdx != -1:
                    insertIdx = firstDeletedIdx

                self.hashArray[insertIdx].key = inKey
                self.hashArray[insertIdx].value = inValue
                self.hashArray[insertIdx].state = 1

                self.count = self.count + 1

                inserted = True
                searching = False

                if collisionOccurred and showCollision:
                    print("Collision resolved at index", insertIdx)

            # Duplicate key
            elif (entry.state == 1 and entry.key == inKey):
                raise ValueError("Duplicate FarmID: " + str(inKey))
         
            else:
                if (entry.state == -1 and firstDeletedIdx == -1):
                    firstDeletedIdx = hashIdx

                    if showCollision:
                        print("Index", hashIdx, "is a deleted slot")

                elif entry.state == 1:
                    collisionOccurred = True

                    if showCollision:
                        print("Collision at index", hashIdx, "- occupied by", entry.key)

                # Linear probing
                hashIdx = (hashIdx + 1) % len(self.hashArray)

                if showCollision:
                    print("Probe next index:", hashIdx)

                if hashIdx == originalIdx:
                    searching = False

        # Reuse a deleted position if necessary
        if (not inserted and firstDeletedIdx != -1):

            self.hashArray[firstDeletedIdx].key = inKey
            self.hashArray[firstDeletedIdx].value = inValue
            self.hashArray[firstDeletedIdx].state = 1

            self.count = self.count + 1

            inserted = True

        if not inserted:
            raise ValueError("Hash table is full")


    # Search
    def search(self, farmID):

        if not self._validFarmID(farmID):
            print("SEARCH FAILED: Invalid FarmID")
            return None

        hashIdx = self._hash(farmID)
        originalIdx = hashIdx

        found = False
        searching = True

        while searching and not found:

            entry = self.hashArray[hashIdx]

            if entry.state == 0:
                searching = False

            elif (entry.state == 1 and entry.key == farmID):
                found = True

            else:
                hashIdx = (hashIdx + 1) % len(self.hashArray)

                if hashIdx == originalIdx:
                    searching = False

        if found:
            print("SEARCH SUCCESS:", farmID, "found at index", hashIdx)
            return self.hashArray[hashIdx].value

        else:
            print("SEARCH FAILED:", farmID, "not found")
            return None


    # Check Whether FarmID Exists
    def hasKey(self, farmID):

        hashIdx = self._hash(farmID)
        originalIdx = hashIdx

        found = False
        searching = True

        while searching and not found:

            entry = self.hashArray[hashIdx]

            if entry.state == 0:
                searching = False

            elif (entry.state == 1 and entry.key == farmID):
                found = True

            else:
                hashIdx = (hashIdx + 1) % len(self.hashArray)

                if hashIdx == originalIdx:
                    searching = False

        return found


    # Delete
    def delete(self, farmID):

        if not self._validFarmID(farmID):
            print("DELETE FAILED: Invalid FarmID")
            return False

        hashIdx = self._hash(farmID)
        originalIdx = hashIdx

        found = False
        searching = True

        while searching and not found:

            entry = self.hashArray[hashIdx]

            if entry.state == 0:
                searching = False

            elif (entry.state == 1 and entry.key == farmID):
                found = True

            else:
                hashIdx = (hashIdx + 1) % len(self.hashArray)

                if hashIdx == originalIdx:
                    searching = False

        if found:
            # Tombstone deletion
            self.hashArray[hashIdx].key = ""
            self.hashArray[hashIdx].value = None
            self.hashArray[hashIdx].state = -1

            self.count = self.count - 1

            print("DELETE SUCCESS:", farmID, "removed from index", hashIdx)

            return True

        else:
            print("DELETE FAILED:", farmID, "not found")

            return False


    # Record Validation
    def _validateRecord(self, record):

        if record is None:
            raise ValueError("Farm record cannot be empty")

        farmID = record.getFarmID()

        if not self._validFarmID(farmID):
            raise ValueError("Invalid FarmID")

        if (record.getName() is None or record.getName() == ""):
            raise ValueError("Farm name cannot be empty")

        latitude = record.getLatitude()
        longitude = record.getLongitude()

        if not isinstance(latitude, (int, float)):
            raise ValueError("Latitude must be numerical")

        if not isinstance(longitude, (int, float)):
            raise ValueError("Longitude must be numerical")

        if (latitude < -90 or latitude > 90):
            raise ValueError("Latitude must be between -90 and 90")

        if (longitude < -180 or longitude > 180):
            raise ValueError("Longitude must be between -180 and 180")


    def _validFarmID(self, farmID):

        valid = True

        if farmID is None:
            valid = False

        elif farmID == "":
            valid = False

        return valid


    # Resize
    def _resize(self, newSize):

        actualSize = self._nextPrime(newSize)
        oldArray = self.hashArray

        self.hashArray = np.empty(actualSize, dtype=object)
        
        ii = 0

        while ii < actualSize:
            self.hashArray[ii] = (DSAHashEntry())
            ii = ii + 1

        self.count = 0

        # Rehash all active entries
        ii = 0

        while ii < len(oldArray):
            if oldArray[ii].state == 1:
                self._insertNoResize(oldArray[ii].key, oldArray[ii].value, False)
                
            ii = ii + 1


    # Prime Number Functions
    def _nextPrime(self, startVal):

        if startVal < 2:
            primeVal = 2

        else:
            primeVal = startVal

            if (primeVal != 2 and primeVal % 2 == 0):
                primeVal = primeVal + 1

            foundPrime = False

            while not foundPrime:

                if self._isPrime(primeVal):
                    foundPrime = True

                else:
                    primeVal = (primeVal + 2)

        return primeVal


    def _isPrime(self, value):

        result = True

        if value < 2:
            result = False

        elif value == 2:
            result = True

        elif value % 2 == 0:
            result = False

        else:
            ii = 3

            while (ii * ii <= value and result):
                if value % ii == 0:
                    result = False

                else:
                    ii = ii + 2

        return result


    # Utility Methods
    def getCount(self):
        return self.count


    def getTableSize(self):
        return len(self.hashArray)


    def display(self):

        print("\nHASH TABLE")
        print("Table Size:", len(self.hashArray))
        print("Record Count:", self.count)
        print("Load Factor:", round(self.getLoadFactor(), 3))
        print("--------------------------------")

        ii = 0

        while ii < len(self.hashArray):

            entry = self.hashArray[ii]

            if entry.state == 1:
                print("Index:", ii, "| FarmID:", entry.key, "| Name:", entry.value.getName())

            elif entry.state == -1:
                print("Index:", ii, "| DELETED")

            ii = ii + 1