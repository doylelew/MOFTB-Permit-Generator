import os

from dotenv import load_dotenv
from selenium.common.exceptions import WebDriverException

from WebDriver import OpenBrowser, Login, ProjectList, Jump_To_URL, PermitList

from GUI import createWindow, ErrorPage, BrowserLogin

#################################################################
# app info
#################################################################
"""
    MOFTB NYC Permit Generator
    An app that submits permits for filming television and movies in the City of New York to bypass having to use the MOFTB website itself.
    The Mayor's Office website often times out not saving your work which requires you to start over which this app bypasses that by saving locally before sending the info over to the MOFTB site.
    The Mayor's Office also will at times make changes from your initial request on the permit without informing you which can be hard to verify without a copy of what you submitted. 
    This will save a plain text version of what you submitted so you can more easily compare your final permit with what you submitted to the Mayor's office.
   
    Author: Doyle Lewis
    Email: odoylerules@pennyworth.network
    
    Version: 0.1.0
    Status: Development   

"""


__author__ = "Doyle Lewis"
__credits__ = ["Doyle Lewis"]
__version__ = "0.1.0"
__maintainer__ = "Doyle Lewis"
__email__ = "odoylerules@pennyworth.network"
__status__ = "Development"

#################################################################
# Constants
#################################################################
MOFTBUrl = "https://nyceventpermits.nyc.gov/film/"
Test404 = "https://photos.google.com/meory/"


#################################################################
# Entry Point
#################################################################

def main():
    window = createWindow()
    error_page = ErrorPage()
    login_page = BrowserLogin()

    window.definePages([error_page,
                        login_page])

    login_page.defineRoutes([('error', error_page)])

    login_page.open()
    window.run()





    # load_dotenv('.env')
    # browser_choice= ""
    # while True:
    #     browser_choice = input('Please type "Chrome" for Chrome broswer of "Firefox" for Firefox\n')
    #     if browser_choice in ('Firefox', 'Chrome'):
    #         break
    #     print(f"broswer choice of {browser_choice} is invalid")
    # browser = OpenBrowser(url= MOFTBUrl, browser_type = browser_choice )
    # try:
    #     Login(browser= browser, username=os.getenv('LOG_USERNAME'), password=os.getenv('LOG_PASSWORD'))
    #     project_list = ProjectList(browser= browser)
    #     Jump_To_URL(browser, project_list['SUCCESSION S4 AKA Sourdough Productions LLC 2ND UNIT'])
    #     permit_list = PermitList(browser=browser, intended_url= project_list['SUCCESSION S4 AKA Sourdough Productions LLC 2ND UNIT'])

    # except WebDriverException as msg:
    #     print(msg)
    #todo test that htis Exception isn't nessary to catch at this level


    # except Exception as msg:
    #     print(msg)
    # input("Press Enter to close browser...")
    # browser.close()


    #todo figure out when to close the broswer on different exceptions
if __name__ == "__main__":
    main()
