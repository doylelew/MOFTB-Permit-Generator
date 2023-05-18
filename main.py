import os

from dotenv import load_dotenv
from selenium.common.exceptions import WebDriverException
import customtkinter as ctk

from WebDriver import OpenBrowser, Login, ProjectList, Jump_To_URL, PermitList
from GUI import MainWindow, SubFrameTemplate, InfoPage, BrowserLogin, ProjectPage

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
# define GUI app lifetime
#################################################################
class App(MainWindow):
    def __init__(self, parent:ctk.CTk):
        super().__init__(parent=parent)
        self.pages = {
            'Info': InfoPage(self.parent),
            'Login': BrowserLogin(self.parent),
            'Project': ProjectPage(self.parent),
        }
        self.current_page = self.pages['Login']

    def openCurrentPage(self, message: str =None):
        self.current_page.open(message)

    def uncheckedChangePage(self,to_page: SubFrameTemplate):
        self.current_page.close()
        self.current_page = to_page
        self.openCurrentPage()

    def checkedChangePage(self, to_page: SubFrameTemplate, exception_to_page: SubFrameTemplate):
        self.current_page.close()
        self.current_page = to_page
        try:
            self.openCurrentPage()
        except Exception as msg:
            self.current_page.close()
            self.current_page = exception_to_page
            self.openCurrentPage(msg)

    def run(self):
        self.openCurrentPage()
        super().run()



#################################################################
# Entry Point
#################################################################

def main():
    window = ctk.CTk()
    app = App(parent=window)
    app.run()

if __name__ == "__main__":
    main()
