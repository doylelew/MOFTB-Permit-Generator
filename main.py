import os

import customtkinter as ctk
import requests

from GUI import MainWindow, LoginPage, ProjectPage, PermitPage1

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
# Entry Point
#################################################################

def main():
# Save States branch

    session = requests.Session()

    window = ctk.CTk()
    app = MainWindow(parent=window, session=session)
    app.build({
        'Login': LoginPage(parent=app, next_frame_name='Project Select'),
        'Project Select': ProjectPage(parent=app,next_frame_name='Permit_Page1'),
        'Permit_Page1': PermitPage1(parent=app),
    })
    app.run('Login')

    session.close()


if __name__ == "__main__":
    main()