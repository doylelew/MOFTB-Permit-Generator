import os

from dotenv import load_dotenv
import requests

from WebDriver import OpenBrowser, login, projectList, Jump_To_URL, PermitList

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
    load_dotenv(".env")

    session = requests.Session()
    try:
        login_success, response = login(session=session,username=os.getenv('LOG_USERNAME'), password=os.getenv('LOG_PASSWORD') )
        project_list, response = projectList(session=session)
    except Exception as msg:
        print(msg)

    print(project_list)

    session.close()


if __name__ == "__main__":
    main()