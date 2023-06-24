import requests
from bs4 import BeautifulSoup as soup

from .Page_Handler import checkPage

def readPermit(session: requests.Session, permit_id: str):
    base_url = "https://nyceventpermits.nyc.gov/film/Project/PermitSteps/PermitStep1.aspx?eid="
    intended_url = f"{base_url}{permit_id}"
    permit_page = session.get(intended_url)
    if checkPage(current_response=permit_page, desired_url=intended_url):
        print(f"permit id= {permit_id}")



