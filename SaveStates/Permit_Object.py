from enum import Enum


class PermitType(Enum):
    SHOOT = 39
    RIG = 40
    SCOUT = 41
    DCAS = 42
    THEATER = 44


class LocationType(Enum):
    NONE = 0
    INT = 1
    EXT = 2
    BOTH = 3


class AddressType(Enum):
    ADDRESS = 14
    FREQ = 21
    STAGE = 17
    THEATER = 15


class Location:
    def __init__(self, name: str, location_type: LocationType, address_type: AddressType):
        self.name = name
        self.type = location_type
        self.address_type = address_type


class DraftPermit:
    def __init__(self, name: str, permit_type: PermitType):
        self.name = name
        self.type = permit_type
        self.locations: list[Location] | None = None

    def addLocations(self, location_list: list[Location]):
        if not self.locations:
            self.locations = []
        for location in location_list:
            self.locations.append(location)
