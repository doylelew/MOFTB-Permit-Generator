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
# Login Function
#################################################################

# Login Constants
UsernameTag = "ctl00$Main$txtUserName"
PasswordTag = "ctl00$Main$txtPassword"
LoginSubmitTag = "ctl00$Main$btnLogin"

def login(session: requests.Session, username:str, password:str):
    """
    Pass user's username and password and enter it into the MOFTB login page
    :param session: request session
    :param username: Username used to log into MOFTB
    :param password: Password used to log into MOFTB
    :return: bool, True if login was successful, false if not
    """
    login_page = session.get(login_url)
    if checkPage(current_response=login_page, desired_url=login_url):
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
        return checkPage(current_response=response, desired_url= home_url), response







