import time

import customtkinter as ctk
import requests

from .GUI_Framework import SubFrameTemplate, MainWindow
from WebDriver import login
from SaveStates import lastUserInfo


#################################################################
# Constants
#################################################################
MOFTBUrl = "https://nyceventpermits.nyc.gov/film/"
Test404 = "https://photos.google.com/meory/"


class LoginPage(SubFrameTemplate):
    def __init__(self, parent: MainWindow | ctk.CTk, next_frame_name: str | None):
        self.login_data: tuple[str,str] | None
        self.frame: ctk.CTkFrame | None
        super().__init__(parent, next_frame_name)

        self.header = ctk.CTkLabel(self.frame,
                                   text="Please enter your MOFTB Login information and choose a prefered broswer")

        self.browser_values = ["Firefox", "Chrome"]
        self.browser_choicebox = ctk.CTkOptionMenu(self.frame, values=self.browser_values,
                                                   command=self.changeBroswerOption, width=300, height=40)
        self.browser_choice = self.browser_values[0]

        self.login_text = ctk.CTkLabel(self.frame, text="Email Address")

        self.login_entry = ctk.CTkEntry(self.frame, width=300, height=40)
        # todo make a autocomplete or past user dropdown

        self.password_text = ctk.CTkLabel(self.frame, text="MOFTB password")

        self.password_entry = ctk.CTkEntry(self.frame, show="*", width=300, height=40)

        self.sumbit_button = ctk.CTkButton(self.frame, text="Submit", command=self.submit, fg_color="blue",
                                           hover_color="lightblue")


    def open(self):

        username, password, browser = lastUserInfo()

        self.browser_choice = browser

        self.header.place(relx=0.5, rely=0.15, anchor='center')

        self.browser_choicebox.place(relx=0.5, rely=0.2, anchor='center')
        self.browser_choicebox.set(self.browser_choice)

        self.login_text.place(relx=0.5, rely=0.25, anchor='center')
        self.login_entry.insert(0, username)
        self.login_entry.place(relx=0.5, rely=0.3, anchor='center')

        self.password_text.place(relx=0.5, rely=0.35, anchor='center')
        self.password_entry.insert(0, password)
        self.password_entry.place(relx=0.5, rely=0.4, anchor='center')

        self.sumbit_button.place(relx=0.5, rely=0.5, anchor='center')

        super().open()


    def changeBroswerOption(self, choice):
        self.browser_choice = choice

    def submit(self):
        self.login_data = (self.login_entry.get(), self.password_entry.get(), self.browser_choice)
        self.close()

        self.parent_wrapper.loadingStart("Loading...\n Please wait while we receive information from MOFTB website")

        try:
            success, response =login(session=self.parent_wrapper.session, username=self.login_data[0], password=self.login_data[1], browser=self.login_data[2])
        except Exception as msg:
            self.header.configure(text=msg, text_color='red')
            if "Page Request Exception" in str(msg):
                self.header.configure(text="Username or password is incorrect please check both and try again", text_color='red')
            self.parent_wrapper.loadingEnd()
            self.open()
            return
            #todo seperate out types of exceptions and responses

        if success:
            self.parent_wrapper.jumpToFrame(self.next_frame_name)
            self.parent_wrapper.loadingEnd()
            return
        self.header.configure(text="something mysterious happend please try again",
                              text_color='red')
        self.open()
        return




