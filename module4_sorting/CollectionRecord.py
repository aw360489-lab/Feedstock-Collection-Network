class CollectionRecord:

    def __init__(self, recordID, farmID, estimatedFeedstock, transportTime):
        
        self.recordID = recordID
        self.farmID = farmID
        self.estimatedFeedstock = estimatedFeedstock
        self.transportTime = transportTime


    def getRecordID(self):
        return self.recordID


    def getFarmID(self):
        return self.farmID


    def getEstimatedFeedstock(self):
        return self.estimatedFeedstock


    def getTransportTime(self):
        return self.transportTime


    def __str__(self):

        return (
            "RecordID=" + str(self.recordID)
            + ", FarmID=" + str(self.farmID)
            + ", Feedstock="
            + str(self.estimatedFeedstock)
            + " kg"
            + ", TransportTime="
            + str(self.transportTime)
            + " min"
        )