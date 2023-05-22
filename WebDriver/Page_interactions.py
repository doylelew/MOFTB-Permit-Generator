import re

from selenium.webdriver.common.by import By
import requests


from bs4 import BeautifulSoup as soup

#################################################################
# Multifunction Constants
#################################################################

login_url = 'https://nyceventpermits.nyc.gov/film/Login.aspx'
test_url = "https://www.google.com/doesnotexist"
home_url = 'https://nyceventpermits.nyc.gov/film/Home.aspx'

#################################################################
# Page handling functions
#################################################################

def checkPage(current_response:requests.Response, desired_url:str) -> bool:
    """
    Checks that current url is the same or a queried version of the desired url

    :param current_response: the request object of the current session
    :param desired_url: the URL you want to confirm that you are viewing
    :return: None
    """

    if current_response.status_code != 200:
        raise Exception(f"Did not get response from page {current_response.url} Error: {current_response.status_code}")

    if desired_url not in current_response.url:
        raise Exception(f"expected to be at {desired_url} instead was taken to {current_response.url}")



# Login Constants
UsernameTag = "ctl00$Main$txtUserName"
PasswordTag = "ctl00$Main$txtPassword"
LoginSubmitTag = "ctl00$Main$btnLogin"

def login(session, username:str, password:str):
    """
    Pass user's username and password and enter it into the MOFTB login page
    :param session: request session
    :param username: Username used to log into MOFTB
    :param password: Password used to log into MOFTB
    :return: None
    """
    login_page = session.get(login_url)
    checkPage(current_response=login_page, desired_url=login_url)

    form_html = soup(login_page.content, 'html.parser').find('form', {'name': 'aspnetForm'})

    payload = {
        "__EVENTTARGET": "",
        "__EVENTARGUMENT": "",
        "__VIEWSTATE": form_html.find('input', {'name': '__VIEWSTATE'}).get('value'),
        "__VIEWSTATEGENERATOR": form_html.find('input', {'name': '__VIEWSTATEGENERATOR'}).get('value'),
        "__SCROLLPOSITIONX": "0",
        "__SCROLLPOSITIONY": "0",
        "__VIEWSTATEENCRYPTED": "",
        "__EVENTVALIDATION": form_html.find('input', {'name': '__EVENTVALIDATION'}).get('value'),
        "ctl00$Main$txtUserName": username,
        "ctl00$Main$txtPassword": password,
        "ctl00$Main$btnLogin": "Submit",
    }

    response = session.post(login_url, data=payload)
    checkPage(current_response=response, desired_url= home_url)

    print(response.url)



# Choose_Project Func Constants
ProjectTableTag = "ctl00_Main_gvProjectsList"
ProjectRowTag = "grid_border"

# looks at the aviable projects on the home page and return a dictionary of names and hyperlinks
def ProjectList(browser) -> dict[str, str]:
    """
    Searches the Home page for listed projects and returns a dictionary of projects and links
    :param browser: Broswer driver object from Selenium
    :return: Dictionary of Key: Project name, Value: URL to project permit page
    """

    if CheckPage(current_url=browser.current_url, desired_url= home_url):
        project_table = soup(browser.page_source, 'html.parser').find('table', {'id': ProjectTableTag}).findAll('tr', {'class',ProjectRowTag})
        project_list = {}
        for row in project_table:
            a_href = row.find('a')
            project_list[a_href.text] =f"https://nyceventpermits.nyc.gov/film/{a_href['href'].replace('ProjectSummary','PermitSummary')}" #Our app will never need to use the project summary so we jkust change the shortcut to Permit summary
        return  project_list

# PermitList contstants
PermitTableTag = "ctl00_Main_gvUserEvents"
PermitRowTag = "grid_border"
PermitNameTag = re.compile(r'ctl\d+_Main_gvUserEvents_ctl\d+_hlEventName')
PermitStatusTag = re.compile(r'ctl\d+_Main_gvUserEvents_ctl\d+_lblStatus')

# Choose_Project Func Constants
def PermitList(browser, intended_url: str) -> dict[str, str]:
    """
    Searches the Permit list page to return a dictionary of incompleted permits and the links to their first step
    :param browser: Broswer driver object from Selenium
    :param intended_url: The URL of the project that you intend to be viewing
    :return: Dictionary of Key: Permit name, Value: URL to permit Step 1 page
    """
    if CheckPage(current_url=browser.current_url, desired_url=intended_url):
        project_table = soup(browser.page_source, 'html.parser').find('table', {'id': PermitTableTag}).findAll('tr', {'class', PermitRowTag})
        incomplete_permits = {}
        for row in project_table:
            if row.find('span', {'id':PermitStatusTag}).text == "Incomplete":
                a_href = row.find('a', {'id': PermitNameTag})
                href_string = re.sub(r'PermitStep\d','PermitStep1',a_href['href']) #always start on the first step of the permit
                incomplete_permits[a_href.text] = f"https://nyceventpermits.nyc.gov/film/Project/{href_string}"
        return incomplete_permits






