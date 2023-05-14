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

def CheckPage(current_url:str, desired_url:str):
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
    raise Exception (f"Website has taken you to {current_url} instead of {login_url} or {home_url}\nPlease log out and retry")
    #todo add logic for if they provide incorrect username or password

# Choose_Project Func Constants
ProjectTableTag = "ctl00_Main_gvProjectsList"

def ProjectSelect(browser):
    # If on the project page find all projects available to choose from
     if CheckPage(current_url=browser.current_url, desired_url= home_url):
         project_table = soup(browser.page_source, 'html.parser').find('table', {'id': ProjectTableTag})
         print(project_table)








