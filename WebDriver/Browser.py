from selenium import webdriver
from selenium.common.exceptions import WebDriverException

from bs4 import BeautifulSoup as soup

def Jump_To_URL(browser, url: str):
    try:
        browser.get(url)
        page_checker = soup(browser.page_source, 'html.parser')
        page_title = page_checker.findAll('title')[0].text
        if '404' in page_title:
            raise Exception(f"{url} has returned 404 Error, please try again")

    # check that selenium connects to the page and the page does not return 404
    except AssertionError as msg:
        print(msg)
    except WebDriverException as msg:
        print(f"Could not connect to {url}, please check internet connection before trying again\nDetails:\n{msg}")

def OpenBrowser(url:str, browser_type:str): #open broswer of userchoice and go to Mayor's office website
    if browser_type == "Firefox":
        browser = webdriver.Firefox()

    if browser_type == "Chrome":
        browser = webdriver.Chrome()

    Jump_To_URL(browser = browser, url = url)

    return browser

# todo Chrome closes with 'disconnected: not connected to DevTools' exception.



