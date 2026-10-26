# py -m module2_hash.testHash

import csv

from module2_hash.FarmRecord import FarmRecord
from module2_hash.Hash import DSAHashTable

# Load Farm Records from CSV
def loadFarmData(fileName, hashTable):

    print("LOADING FARM RECORDS")
    print()

    insertedCount = 0
    invalidCount = 0

    try:
        with open(fileName, "r", encoding="utf-8-sig", newline="") as csvFile:

            reader = csv.reader(csvFile)

            # Read and ignore the header row
            header = next(reader, None)

            for row in reader:

                try:
                    # The selected farm CSV contains exactly 20 columns
                    if len(row) >= 20:

                        farmID = row[0]
                        name = row[1]
                        categories = row[2]
                        species = row[3]

                        # Convert latitude and longitude to numerical values
                        latitude = float(row[4])
                        longitude = float(row[5])

                        latLng = row[6]
                        addressOverride = row[7]
                        streetNum = row[8]
                        street = row[9]
                        suburb = row[10]
                        state = row[11]
                        postcode = row[12]
                        country = row[13]
                        lastKnownStatus = row[14]
                        tags = row[15]
                        ownedBy = row[16]
                        contractedTo = row[17]
                        mapURL = row[18]
                        profileURL = row[19]

                        record = FarmRecord(
                            farmID,
                            name,
                            categories,
                            species,
                            latitude,
                            longitude,
                            latLng,
                            addressOverride,
                            streetNum,
                            street,
                            suburb,
                            state,
                            postcode,
                            country,
                            lastKnownStatus,
                            tags,
                            ownedBy,
                            contractedTo,
                            mapURL,
                            profileURL
                        )

                        hashTable.insert(record)
                        insertedCount = (insertedCount + 1)

                        # Display load factor after every 10 successful insertions
                        if (insertedCount % 10 == 0):

                            print()
                            print("LOAD FACTOR SUMMARY")
                            print("After", insertedCount, "insertions:")
                            print("Table size:", hashTable.getTableSize())
                            print("Load factor:", round(hashTable.getLoadFactor(), 3))
                            print()

                    else:
                        invalidCount = (invalidCount + 1)
                        print("Invalid CSV row:", "fewer than 20 columns")

                except ValueError as error:
                    invalidCount = (invalidCount + 1)
                    print("Invalid farm record:", error)

                except Exception as error:
                    invalidCount = (invalidCount + 1)
                    print("Record could not be inserted:", error)

    except FileNotFoundError:
        print("ERROR: File not found:", fileName)

    print()
    print("=" * 65)
    print("CSV LOAD SUMMARY")
    print("=" * 65)

    print("Successfully inserted:", insertedCount)
    print("Invalid records:", invalidCount)
    print("Final table size:", hashTable.getTableSize())
    print("Final load factor:", round(hashTable.getLoadFactor(), 3))

    return insertedCount


# Find One Existing FarmID for Testing
def getFirstFarmID(hashTable):

    ii = 0
    farmID = None

    while (ii < hashTable.getTableSize() and farmID is None):

        entry = hashTable.hashArray[ii]

        if entry.state == 1:
            farmID = entry.key

        ii = ii + 1

    return farmID


# Find Another Existing FarmID
def getSecondFarmID(hashTable, firstFarmID):

    ii = 0
    farmID = None

    while (ii < hashTable.getTableSize() and farmID is None):

        entry = hashTable.hashArray[ii]

        if (entry.state == 1 and entry.key != firstFarmID):
            farmID = entry.key

        ii = ii + 1

    return farmID


# Run Hash Table Tests
def runHashTests():

    print("=" * 65)
    print("MODULE 2 - HASH-BASED FARM LOOKUP")
    print("=" * 65)

    # Create Hash Table
    # A small initial prime table is used so that collisions and resizing can be demonstrated.
    hashTable = DSAHashTable(11)


    # Test 1: Load at least 40 farm records
    print()
    print("TEST 1: LOAD FARM RECORDS")
    print()

    totalInserted = loadFarmData("data/selected_southern_wa_farms.csv", hashTable)

    print()
    print("Total records currently stored:", hashTable.getCount())

    # Obtain existing IDs for later tests
    firstFarmID = getFirstFarmID(hashTable)
    secondFarmID = getSecondFarmID(hashTable, firstFarmID)


    # Test 2: Successful Search
    print()
    print("\nTEST 2: SUCCESSFUL SEARCH")

    record = hashTable.search(firstFarmID)

    if record is not None:
        print()
        print("Complete Farm Record:")
        print(record)


    # Test 3: Another Successful Search
    print()
    print("\nTEST 3: ANOTHER SUCCESSFUL SEARCH")

    record = hashTable.search(secondFarmID)

    if record is not None:
        print()
        print("Complete Farm Record:")
        print(record)


    # Test 4: Unsuccessful Search
    print()
    print("\nTEST 4: UNSUCCESSFUL SEARCH")

    hashTable.search("NOT_EXIST")


    # Test 5: Successful Delete
    print()
    print("\nTEST 5: SUCCESSFUL DELETE")

    deleteFarmID = secondFarmID

    hashTable.delete(deleteFarmID)


    # Test 6: Search After Deletion
    print()
    print("\nTEST 6: SEARCH AFTER DELETION")

    hashTable.search(deleteFarmID)


    # Test 7: Unsuccessful Delete
    print()
    print("\nTEST 7: UNSUCCESSFUL DELETE")

    hashTable.delete("NOT_EXIST")


    # Test 8: Duplicate FarmID
    print()
    print("\nTEST 8: DUPLICATE FARM ID")

    existingRecord = hashTable.search(firstFarmID)

    if existingRecord is not None:
        try:
            hashTable.insert(existingRecord)

        except ValueError as error:
            print("Expected error:", error)


    # Test 9: Empty FarmID
    print()
    print("\nTEST 9: INVALID EMPTY FARM ID")

    invalidRecord = FarmRecord(
        "",
        "Invalid Farm",
        "Farm",
        "Cattle",
        -34.5,
        117.5,
        "",
        "",
        "",
        "",
        "Test Suburb",
        "WA",
        "6000",
        "Australia",
        "",
        "",
        "",
        "",
        "",
        ""
    )

    try:
        hashTable.insert(invalidRecord)

    except ValueError as error:
        print("Expected error:", error)


    # Test 10: Empty Farm Name
    print()
    print("\nTEST 10: INVALID EMPTY FARM NAME")

    invalidRecord = FarmRecord(
        "TEST01",
        "",
        "Farm",
        "Cattle",
        -34.5,
        117.5,
        "",
        "",
        "",
        "",
        "Test Suburb",
        "WA",
        "6000",
        "Australia",
        "",
        "",
        "",
        "",
        "",
        ""
    )

    try:
        hashTable.insert(invalidRecord)

    except ValueError as error:
        print("Expected error:", error)


    # Test 11: Invalid Latitude
    print()
    print("\nTEST 11: INVALID LATITUDE")

    invalidRecord = FarmRecord(
        "TEST02",
        "Invalid Latitude Farm",
        "Farm",
        "Cattle",
        -100.0,
        117.5,
        "",
        "",
        "",
        "",
        "Test Suburb",
        "WA",
        "6000",
        "Australia",
        "",
        "",
        "",
        "",
        "",
        ""
    )

    try:
        hashTable.insert(invalidRecord)

    except ValueError as error:
        print("Expected error:", error)


    # Test 12: Invalid Longitude
    print()
    print("\nTEST 12: INVALID LONGITUDE")

    invalidRecord = FarmRecord(
        "TEST03",
        "Invalid Longitude Farm",
        "Farm",
        "Cattle",
        -34.5,
        200.0,
        "",
        "",
        "",
        "",
        "Test Suburb",
        "WA",
        "6000",
        "Australia",
        "",
        "",
        "",
        "",
        "",
        ""
    )

    try:
        hashTable.insert(invalidRecord)

    except ValueError as error:
        print("Expected error:", error)


    # Test 13: Final Hash Table Summary
    print()
    print("\nTEST 13: FINAL HASH TABLE SUMMARY")

    print("Records:", hashTable.getCount())

    print("Table size:", hashTable.getTableSize())

    print(
        "Load factor:",
        round(hashTable.getLoadFactor(), 3)
    )


# Main
if __name__ == "__main__":
    runHashTests()