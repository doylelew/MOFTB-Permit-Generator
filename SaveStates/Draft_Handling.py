import json
import os
import re

from .Permit_Object import DraftPermit, Location

def getSessionData():
    current_session_path = "../sessions/userdata/current_session.json"
    with open(current_session_path, 'r') as data:
        current_session = json.loads(data.read())
    return current_session


def saveLocation(location: Location):
    location_data = {
        "location name": location.name,
        "location type": location.type.value,
        "address type": location.address_type.value,
    }
    return location_data

def saveDraft(permit: DraftPermit):
    session_data = getSessionData()

    permit.addSessionData(owner=session_data["user"])
    # todo implement ID in the addSessionData

    permit_data = {
        "owner": permit.owner,
        "permit_id": permit.id,
        "name": permit.name,
        "type": permit.type.value,
        "locations": list(map(saveLocation, permit.locations))
    }
    print(permit_data)
    with open(f"../{session_data['save locations']['drafts folder']}{permit.name}.json", 'w') as save_data:
        save_data.write(json.dumps(permit_data, indent=2))



