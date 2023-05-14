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

def Login(browser, username, password): #Pass user's username and password and enter it into the MOFTB login page
    # check user is on the login page
    current_url = browser.current_url
    if login_url in current_url:
        # enter username and passwrd them submit
        browser.find_element(By.NAME, UsernameTag).send_keys(username)
        browser.find_element(By.NAME, PasswordTag).send_keys(password)
        browser.find_element(By.NAME, LoginSubmitTag).click()
        return
    # if user is on home page instead
    if home_url in current_url:
        return
    raise Exception (f"Website has taken you to {current_url} instead of {login_url} or {home_url}\nPlease log out and retry")

# Choose_Project Func Constants
ProjectListTag = "ctl00_Main_gvProjectsList"
