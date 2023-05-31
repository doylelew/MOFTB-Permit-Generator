import json
import os
import re

from .Permit_Object import DraftPermit, Location

save_path = "../sessions/doylelewisa/drafts/"

def saveLocation(location: Location):
    location_data = {
        "location name": location.name,
        "location type": location.type.value,
        "address type": location.address_type.value,
    }
    return location_data

def saveDraft(permit: DraftPermit):
    permit_data = {
        "name": permit.name,
        "type": permit.type.value,
        "locations": list(map(saveLocation, permit.locations))
    }
    print(permit_data)
    with open(f"{save_path}{permit.name}.json", 'w') as save_data:
        save_data.write(json.dumps(permit_data, indent=2))



