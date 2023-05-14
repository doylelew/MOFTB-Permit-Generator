import os

from dotenv import load_dotenv

from WebDriver import OpenBrowser, Login
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

    Login(browser= browser, username=os.getenv('LOG_USERNAME'), password=os.getenv('LOG_PASSWORD'))
    input("Press Enter to close browser...")
    browser.close()

if __name__ == "__main__":
    main()