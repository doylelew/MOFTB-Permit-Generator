import os

import requests

from SaveStates import lastUserInfo
from WebDriver import  login, projectList, permitList, readPermit


session = requests.Session()

username, password, browser = lastUserInfo()

success, request = login(session=session, username=username, password=password, browser= browser)

project_list, request = projectList(session=session)
permit_list, request = permitList(session=session, intended_url=project_list['SUCCESSION S4 AKA Sourdough Productions LLC 2ND UNIT'])
readPermit(session=session, permit_id=permit_list['11.11 Helipad Stage'].split('eid=', 1)[1])

session.close()