from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

#################################################################
# Constants
#################################################################
MOFTBUrl = "https://nyceventpermits.nyc.gov/film/"

UsernameTag = "ctl00$Main$txtUserName"
PasswordTag = "ctl00$Main$txtPassword"
LoginSubmitTag = "ctl00$Main$btnLogin"

ProjectListTag = "ctl00_Main_gvProjectsList"


#################################################################
# Page interactions functions
#################################################################

def OpenBrowser(url, browser_type): #open broswer of userchoice and go to Mayor's office website
    if browser_type == "Firefox":
        browser = webdriver.Firefox()

    if browser_type == "Chrome":
        browser = webdriver.Chrome()
    browser.get(url)
    return browser

def Login(browser, username, password): #Pass user's username and password and enter it into the MOFTB login page
    browser.find_element(By.NAME, UsernameTag).send_keys(username)
    browser.find_element(By.NAME, PasswordTag).send_keys(password)
    browser.find_element(By.NAME, LoginSubmitTag).click()

    input("Press Enter to close....")

#################################################################
# Entry Point
#################################################################

def main():
    load_dotenv('.env')
    browser_choice= ""
    while True:
        browser_choice = input('Please type "Chrome" for Chrome broswer of "Firefox" for Firefox\n')
        if browser_choice in ('Firefox', 'Chrome'):
            break
        print(f"broswer choice of {browser_choice} is invalid")
    browser = OpenBrowser(url= MOFTBUrl, browser_type = browser_choice )
    Login(browser= browser, username=os.getenv('LOG_USERNAME'), password=os.getenv('LOG_PASSWORD'))
    browser.close()

if __name__ == "__main__":
    main()