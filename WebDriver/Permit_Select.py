import re

import requests
from bs4 import BeautifulSoup as soup

from .Page_Handler import checkPage


#################################################################
# Multifunction Constants
#################################################################

login_url = 'https://nyceventpermits.nyc.gov/film/Login.aspx'
test_url = "https://www.google.com/doesnotexist"
home_url = 'https://nyceventpermits.nyc.gov/film/Home.aspx'


#################################################################
# Functions for getting the project and permit lists from MOFTB
#################################################################

# Choose_Project Func Constants
ProjectTableTag = "ctl00_Main_gvProjectsList"
ProjectRowTag = "grid_border"

def projectList(session:requests.Session) -> dict[str, str]:
    """
    Searches the Home page for listed projects and returns a dictionary of projects and links
    :param session: request session
    :return: Dictionary of Key: Project name, Value: URL to project permit page
    """
    home_page = session.get(home_url)
    if checkPage(current_response= home_page, desired_url= home_url):
        project_table = soup(home_page.content, 'html.parser').find('table', {'id': ProjectTableTag}).findAll('tr', {'class',ProjectRowTag})
        project_list = {}
        for row in project_table:
            a_href = row.find('a')
            project_list[a_href.text] =f"https://nyceventpermits.nyc.gov/film/{a_href['href'].replace('ProjectSummary','PermitSummary')}" #Our app will never need to use the project summary so we just change the shortcut to permit summary
        return  project_list, home_page



# PermitList contstants
PermitTableTag = "ctl00_Main_gvUserEvents"
PermitRowTag = "grid_border"
PermitNameTag = re.compile(r'ctl\d+_Main_gvUserEvents_ctl\d+_hlEventName')
PermitStatusTag = re.compile(r'ctl\d+_Main_gvUserEvents_ctl\d+_lblStatus')

# Choose_Project Func Constants
def permitList(session: requests.Session, intended_url: str) -> dict[str, str]:
    """
    Searches the Permit list page to return a dictionary of incompleted permits and the links to their first step
    :param session: request session
    :param intended_url: The URL of the project that you intend to be viewing
    :return: Dictionary of Key: Permit name, Value: URL to permit Step 1 page
    """
    project_page = session.get(intended_url)
    if checkPage(current_response=project_page, desired_url=intended_url):
        project_table = soup(project_page.content, 'html.parser').find('table', {'id': PermitTableTag}).findAll('tr', {'class', PermitRowTag})
        incomplete_permits = {}
        for row in project_table:
            if row.find('span', {'id':PermitStatusTag}).text == "Incomplete":
                a_href = row.find('a', {'id': PermitNameTag})
                href_string = re.sub(r'PermitStep\d','PermitStep1',a_href['href']) #always start on the first step of the permit
                incomplete_permits[a_href.text] = f"https://nyceventpermits.nyc.gov/film/Project/{href_string}"
        return incomplete_permits, project_page
