class FarmRecord:

    def __init__(
        self,
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
    ):

        self.farmID = farmID
        self.name = name
        self.categories = categories
        self.species = species
        self.latitude = latitude
        self.longitude = longitude
        self.latLng = latLng
        self.addressOverride = addressOverride
        self.streetNum = streetNum
        self.street = street
        self.suburb = suburb
        self.state = state
        self.postcode = postcode
        self.country = country
        self.lastKnownStatus = lastKnownStatus
        self.tags = tags
        self.ownedBy = ownedBy
        self.contractedTo = contractedTo
        self.mapURL = mapURL
        self.profileURL = profileURL


    def getFarmID(self):
        return self.farmID

    def getName(self):
        return self.name

    def getCategories(self):
        return self.categories

    def getSpecies(self):
        return self.species

    def getLatitude(self):
        return self.latitude

    def getLongitude(self):
        return self.longitude

    def getLatLng(self):
        return self.latLng

    def getAddressOverride(self):
        return self.addressOverride

    def getStreetNum(self):
        return self.streetNum

    def getStreet(self):
        return self.street

    def getSuburb(self):
        return self.suburb

    def getState(self):
        return self.state

    def getPostcode(self):
        return self.postcode

    def getCountry(self):
        return self.country

    def getLastKnownStatus(self):
        return self.lastKnownStatus

    def getTags(self):
        return self.tags

    def getOwnedBy(self):
        return self.ownedBy

    def getContractedTo(self):
        return self.contractedTo

    def getMapURL(self):
        return self.mapURL

    def getProfileURL(self):
        return self.profileURL


    def __str__(self):

        return (
            "FarmID: " + str(self.farmID)
            + "\nName: " + str(self.name)
            + "\nCategories: " + str(self.categories)
            + "\nSpecies: " + str(self.species)
            + "\nLatitude: " + str(self.latitude)
            + "\nLongitude: " + str(self.longitude)
            + "\nSuburb: " + str(self.suburb)
            + "\nState: " + str(self.state)
            + "\nPostcode: " + str(self.postcode)
            + "\nCountry: " + str(self.country)
            + "\nLast Known Status: "
            + str(self.lastKnownStatus)
        )