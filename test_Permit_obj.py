from SaveStates import DraftPermit, Location, PermitType, LocationType, AddressType, saveDraft


permit = DraftPermit(name="TestPermit", permit_type=PermitType.SHOOT)

locations = [
    Location(name="INT Mall", location_type=LocationType.INT, address_type=AddressType.ADDRESS),
    Location(name="EXT Mall", location_type=LocationType.EXT, address_type=AddressType.ADDRESS),
    Location(name="INT Apple Store", location_type=LocationType.INT, address_type=AddressType.STAGE),
]
permit.addLocations(locations)

saveDraft(permit)