import os

from dotenv import load_dotenv
from selenium.common.exceptions import WebDriverException

from WebDriver import OpenBrowser, Login, ProjectList, Jump_To_URL, PermitList
#################################################################
# Constants
#################################################################
MOFTBUrl = "https://nyceventpermits.nyc.gov/film/"
Test404 = "https://photos.google.com/meory/"


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
    try:
        Login(browser= browser, username=os.getenv('LOG_USERNAME'), password=os.getenv('LOG_PASSWORD'))
        project_list = ProjectList(browser= browser)
        Jump_To_URL(browser, project_list['SUCCESSION S4 AKA Sourdough Productions LLC 2ND UNIT'])
        permit_list = PermitList(browser=browser, intended_url= project_list['SUCCESSION S4 AKA Sourdough Productions LLC 2ND UNIT'])


    # except WebDriverException as msg:
    #     print(msg)
    #todo test that htis Exception isn't nessary to catch at this level
    except Exception as msg:
        print(msg)
    input("Press Enter to close browser...")
    browser.close()
    #todo figure out when to close the broswer on different exceptions

if __name__ == "__main__":
    main()