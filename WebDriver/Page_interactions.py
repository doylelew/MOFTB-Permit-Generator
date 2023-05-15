import re

from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup as soup

#################################################################
# Multifunction Constants
#################################################################

login_url = 'https://nyceventpermits.nyc.gov/film/Login.aspx'
home_url = 'https://nyceventpermits.nyc.gov/film/Home.aspx'

#################################################################
# Page handling functions
#################################################################

# Login Constants
UsernameTag = "ctl00$Main$txtUserName"
PasswordTag = "ctl00$Main$txtPassword"
LoginSubmitTag = "ctl00$Main$btnLogin"

def CheckPage(current_url:str, desired_url:str) -> bool:
    if desired_url in current_url:
        return True
    raise Exception(f"expected to be at {desired_url} instead was taken to {current_url}")
    return False

def Login(browser, username:str, password:str): #Pass user's username and password and enter it into the MOFTB login page
    # check user is on the login page
    current_url = browser.current_url
    if login_url in current_url:
        # enter username and passwrd them submit
        browser.find_element(By.NAME, UsernameTag).send_keys(username)
        browser.find_element(By.NAME, PasswordTag).send_keys(password)
        browser.find_element(By.NAME, LoginSubmitTag).click()
        current_url = browser.current_url
    # if user ends on home page or started there anyway move forward
    if home_url in current_url:
        return
    # otherwise if they are on some other page
    raise Exception (f"Website has taken you to {current_url} instead of {login_url} or {home_url}\nPlease log out and retry")
    #todo add logic for if they provide incorrect username or password

# Choose_Project Func Constants
ProjectTableTag = "ctl00_Main_gvProjectsList"
ProjectRowTag = "grid_border"

# looks at the aviable projects on the home page and return a dictionary of names and hyperlinks
def ProjectList(browser) -> dict[str, str]:
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
    if CheckPage(current_url=browser.current_url, desired_url=intended_url):
        project_table = soup(browser.page_source, 'html.parser').find('table', {'id': PermitTableTag}).findAll('tr', {'class', PermitRowTag})
        incomplete_permits = {}
        for row in project_table:
            if row.find('span', {'id':PermitStatusTag}).text == "Incomplete":
                a_href = row.find('a', {'id': PermitNameTag})
                href_string = re.sub(r'PermitStep\d','PermitStep1',a_href['href']) #always start on the first step of the permit
                incomplete_permits[a_href.text] = f"https://nyceventpermits.nyc.gov/film/Project/{href_string}"
        return incomplete_permits






