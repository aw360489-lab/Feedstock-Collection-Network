# Define F (Estimated Feedstock)

class CollectionRequest:

    def __init__(self, farmID, estimatedFeedstock):

        self.farmID = farmID
        self.estimatedFeedstock = estimatedFeedstock

        # These values are calculated by the system
        self.farmName = ""
        self.transportTime = 0
        self.priority = 0.0


    def getFarmID(self):
        return self.farmID

    def getEstimatedFeedstock(self):
        return self.estimatedFeedstock


    def getFarmName(self):
        return self.farmName

    def setFarmName(self, farmName):
        self.farmName = farmName


    def getTransportTime(self):
        return self.transportTime

    def setTransportTime(self, transportTime):
        self.transportTime = transportTime


    def getPriority(self):
        return self.priority

    def setPriority(self, priority):
        self.priority = priority


    def __str__(self):

        return (
            "FarmID=" + str(self.farmID)
            + ", Farm=" + str(self.farmName)
            + ", Feedstock="
            + str(self.estimatedFeedstock)
            + " kg"
            + ", Time="
            + str(self.transportTime)
            + " min"
            + ", Priority="
            + str(round(self.priority, 2))
        )